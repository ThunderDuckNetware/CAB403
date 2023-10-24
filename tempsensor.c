#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <time.h>
#include <errno.h>

#include "shm_units.h"
#include "datagrams.h"
#include "safety_funcs.h"


int main(int argc, char **argv)
{
    // Check arguments
    if (argc < 8)
    {
        fprintf(stderr, "Usage: {id} {address:port} {max condvar wait (microseconds)} {max update wait (microseconds)} {shared memory path} {shared memory offset} {receiver address:port} ...");
        exit(1);
    }

    // Read arguments
    int id = atoi(argv[1]);
    const char *address_port = argv[2];
    int max_condvar_wait = atoi(argv[3]);
    int max_update_wait = atoi(argv[4]);
    const char *shm_path = argv[5];
    int shm_offset = atoi(argv[6]);
    int num_receivers = argc - 7;                   // The number of receivers is all the arguments beyond the first 7
    char *receiver_address_port[num_receivers];
    for (int i = 0; i < num_receivers; i++)
    {
        receiver_address_port[i] = argv[7 + i];
    }

    // Open shared memory
    char *shm = open_shared_memory(shm_path);
    shm_tempsensor_t *shm_ts = (shm_tempsensor_t *)(shm + shm_offset);

    // Parse address and port of this sensor
    char ts_addr_str[100];
    int ts_port;
    sscanf(address_port, "%99[^:]:%d", ts_addr_str, &ts_port);

    // Create UDP socket, setup address and bind
    int ts_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (ts_fd == -1)
    {
        perror("socket");
        exit(1);
    }
    struct sockaddr_in ts_addr;
    memset(&ts_addr, 0, sizeof(ts_addr));
    ts_addr.sin_family = AF_INET;
    ts_addr.sin_port = htons(ts_port);
    if (inet_pton(AF_INET, ts_addr_str, &ts_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }
    if (bind(ts_fd, (struct sockaddr *)&ts_addr, sizeof(ts_addr)) == -1)
    {
        perror("bind");
        exit(1);
    }

    // Loop variables
    float temperature;
    float old_temperature = 0;
    int first_iteration = 1;
    struct timeval last_update_time;    
    int total_update_waittime;

    // Normal Operation
    pthread_mutex_lock(&shm_ts->mutex);
    for (;;)
    {   
        if (!first_iteration)
        {
            // Calculate the total time waited since the last update
            struct timeval current_time;
            gettimeofday(&current_time, NULL);
            int delta_seconds = current_time.tv_sec - last_update_time.tv_sec;
            int delta_microseconds = current_time.tv_usec - last_update_time.tv_usec;
            total_update_waittime = (delta_seconds * 1000000) + delta_microseconds;

            // Update old_temperature
            old_temperature = temperature;
        }

        // Get a temp reading off this sensor
        temperature = shm_ts->temperature;
        pthread_mutex_unlock(&shm_ts->mutex);

        if ((first_iteration) || (temperature != old_temperature) || (total_update_waittime > max_update_wait))
        {
            // Construct a UDP datagram with the sensor's id, the temperature, the
            // current time and with an address list consisting only of this sensor
            temp_update_datagram temp_update;
            temp_update.header[0] = 'T';
            temp_update.header[1] = 'E';
            temp_update.header[2] = 'M';
            temp_update.header[3] = 'P';
            temp_update.id = id;
            gettimeofday(&temp_update.timestamp, NULL);
            temp_update.temperature = temperature;
            temp_update.address_count = 1;
            temp_update.address_list[0].sensor_addr = ts_addr.sin_addr;
            temp_update.address_list[0].sensor_port = ts_addr.sin_port;

            // Send the datagram to each receiver
            for (int i = 0; i < num_receivers; i++)
            {
                // Parse the receiver address and port
                char *receiver_address_port_str = receiver_address_port[i];
                char receiver_addr_str[100];
                int receiver_port;
                sscanf(receiver_address_port_str, "%99[^:]:%d", receiver_addr_str, &receiver_port);

                // Create Address
                struct sockaddr_in receiver_addr;
                memset(&receiver_addr, 0, sizeof(receiver_addr));
                receiver_addr.sin_family = AF_INET;
                receiver_addr.sin_port = htons(receiver_port);
                if (inet_pton(AF_INET, receiver_addr_str, &receiver_addr.sin_addr) != 1)
                {
                    perror("inet_pton");
                    exit(1);
                }

                // Create UDP socket and send the message, then close fd
                int udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                if (udp_fd == -1)
                {
                    perror("socket");
                    exit(1);
                }
                int len = sendto(udp_fd, &temp_update, sizeof(temp_update), 0, (struct sockaddr *)&receiver_addr, sizeof(receiver_addr));
                if (len == -1)
                {
                    perror("sendto");
                    exit(1);
                }
                if (close(udp_fd) == -1)
                {
                    perror("close");
                    exit(1);
                }
            }

            // Get the current time for calculating the total wait time since the last update
            gettimeofday(&last_update_time, NULL);

            // Set first_iteration to 0 after first loop
            if (first_iteration)
            {
                first_iteration = 0;
            }
        }

        // Receive a temp update Use Non-blocking recvfrom (MSG_DONTWAIT)
        temp_update_datagram temp_update;

        int len = recvfrom(ts_fd, &temp_update, sizeof(temp_update), MSG_DONTWAIT, NULL, NULL);
        if (len > 0)
        {
            // Increment the address count and add this sensors address to the address list
            temp_update.address_count += 1;
            temp_update.address_list[temp_update.address_count].sensor_addr = ts_addr.sin_addr;
            temp_update.address_list[temp_update.address_count].sensor_port = ts_addr.sin_port;

            // Send the datagram to each sensor (connected to this sensor) that does not appear on the datagram's address list
            for (int i = 0; i < num_receivers; i++)
            {
                // Parse receiver address and port
                char *receiver_address_port_str = receiver_address_port[i];
                char receiver_addr_str[100];
                int receiver_port;
                sscanf(receiver_address_port_str, "%99[^:]:%d", receiver_addr_str, &receiver_port);

                // Create Address
                struct sockaddr_in receiver_addr;
                memset(&receiver_addr, 0, sizeof(receiver_addr));
                receiver_addr.sin_family = AF_INET;
                receiver_addr.sin_port = htons(receiver_port);
                if (inet_pton(AF_INET, receiver_addr_str, &receiver_addr.sin_addr) != 1)
                {
                    perror("inet_pton");
                    exit(1);
                }

                // Check if the receiver address is in the address list. If not, send the temp update to the receiver
                int found = 0;
                for (int j = 0; j < temp_update.address_count; j++)
                {
                    if ((temp_update.address_list[j].sensor_port == receiver_addr.sin_port))
                    {
                        found = 1;
                        break;
                    }
                }
                if (!found)
                {
                    // Create a UDP socket and send the temp update, then close fd
                    int udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                    if (udp_fd == -1)
                    {
                        perror("socket");
                        exit(1);
                    }
                    int len = sendto(udp_fd, &temp_update, sizeof(temp_update), 0, (struct sockaddr *)&receiver_addr, sizeof(receiver_addr));
                    if (len == -1)
                    {
                        perror("sendto");
                        exit(1);
                    }
                    if (close(udp_fd) == -1)
                    {
                        perror("close");
                        exit(1);
                    }
                }

                // Get the current time used for calculating the total wait time since the last update
                gettimeofday(&last_update_time, NULL);
                
            }
        } else if (len == -1) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) 
            {
                // No data available right now, can try again later
            } else {
                printf("Error receiving datagram\n");
                perror("recvfrom");
            }
        }

        // Lock the mutex and wait on cond using pthread_cond_timedwait to ensure that the maximum waiting time is the max condvar wait
        pthread_mutex_lock(&shm_ts->mutex);
        struct timespec ts;
        clock_gettime(CLOCK_REALTIME, &ts);
        ts.tv_nsec += max_condvar_wait * 1000;
        pthread_cond_timedwait(&shm_ts->cond, &shm_ts->mutex, &ts);
    }

    return 0;
}