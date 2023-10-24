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
    int num_receivers = argc - 7;               // The number of receivers is all the arguments beyond the first 7
    char *receiver_address_port[num_receivers];
    for (int i = 0; i < num_receivers; i++)
    {
        receiver_address_port[i] = argv[7 + i];
    }

    // // Print all arguments
    // printf("Printing all arguments:\n");
    // for (int i = 0; i < argc; i++)
    // {
    //     printf("argv[%d] = %s\n", i, argv[i]);
    // }    

    // Open shared memory
    int shm_fd = shm_open(shm_path, O_RDWR, 0);
    if (shm_fd == -1)
    {
        perror("shm_open");
        exit(1);
    }
    // Get shared memory size
    struct stat shm_stat;
    if (fstat(shm_fd, &shm_stat) == -1)
    {
        perror("fstat");
        exit(1);
    }
    // Map shared memory
    char *shm = mmap(NULL, shm_stat.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm == MAP_FAILED)
    {
        perror("mmap");
        exit(1);
    }
    shm_tempsensor *shm_ts = (shm_tempsensor *)(shm + shm_offset);

    // Parse address and port of this sensor
    char ts_addr_str[100];
    int ts_port;
    sscanf(address_port, "%[^:]:%d", ts_addr_str, &ts_port);

    // Create UDP socket and bind
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

            // printf("Temperature in here: %f\n", temperature);

            // Update old_temperature
            old_temperature = temperature;

            // printf("The old temperature is: %f\n", old_temperature);
            // printf("Total update waittime: %d\n", total_update_waittime);
        }

        // Get a temp reading off this sensor
        pthread_mutex_lock(&shm_ts->mutex);
        temperature = shm_ts->temperature;
        pthread_mutex_unlock(&shm_ts->mutex);

        // printf("Temperature: %f\n", temperature);
        // printf("Old Temperature: %f\n", old_temperature);
        // printf("First Iteration: %d\n", first_iteration);
        // printf("Total Update Waittime: %d\n", total_update_waittime);
        // printf("Max Update Wait: %d\n", max_update_wait);

        if ((first_iteration) || (temperature != old_temperature) || (total_update_waittime > max_update_wait))
        {
            if (!first_iteration)
            {
                printf("Temperature changed or max update waittime exceeded\n");
            }
            // printf("Sending update\n");
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
                sscanf(receiver_address_port_str, "%[^:]:%d", receiver_addr_str, &receiver_port);

                // printf("Receiver address: %s\n", receiver_addr_str);
                // printf("Receiver port: %d\n", receiver_port);

                // Create Address and send the temp update
                struct sockaddr_in receiver_addr;
                memset(&receiver_addr, 0, sizeof(receiver_addr));
                receiver_addr.sin_family = AF_INET;
                receiver_addr.sin_port = htons(receiver_port);
                if (inet_pton(AF_INET, receiver_addr_str, &receiver_addr.sin_addr) != 1)
                {
                    perror("inet_pton");
                    exit(1);
                }
                int len = sendto(ts_fd, &temp_update, sizeof(temp_update), 0, (struct sockaddr *)&receiver_addr, sizeof(receiver_addr));
                if (len == -1)
                {
                    perror("sendto");
                    exit(1);
                }
                // printf("Sent %d bytes\n", len);
                // printf("From address %s:%d\n", inet_ntoa(receiver_addr.sin_addr), ntohs(receiver_addr.sin_port));
                // printf("To address %s:%d\n", inet_ntoa(temp_update.address_list[0].sensor_addr), ntohs(temp_update.address_list[0].sensor_port));
            }

            // Get the current time for calculating the total wait time since the last update
            gettimeofday(&last_update_time, NULL);
            // printf("Time in seconds: %ld\n", last_update_time.tv_sec);
            // printf("Time in microseconds: %ld\n", last_update_time.tv_usec);

            // Set first_iteration to 0 after first iteration
            if (first_iteration)
            {
                // printf("First iteration\n");
                first_iteration = 0;
            }
        }

    
        // Receive a temp update and the address of the sending sensor. Use Non-blocking recvfrom (MSG_DONTWAIT)
        temp_update_datagram temp_update;
        struct sockaddr_in sender_addr;
        socklen_t sender_addr_len = sizeof(sender_addr);

        int len = recvfrom(ts_fd, &temp_update, sizeof(temp_update), MSG_DONTWAIT, (struct sockaddr *)&sender_addr, &sender_addr_len);

        if (len > 0)
        {
            printf("Received update\n");

            // get the temperature, timestamp and address list from it
            float recv_temp = temp_update.temperature;
            struct timeval recv_timestamp = temp_update.timestamp;
            int recv_address_count = temp_update.address_count;
            struct addr_entry recv_addr_list[recv_address_count];
            for (int i = 0; i < recv_address_count; i++)
            {
                recv_addr_list[i] = temp_update.address_list[i];
            }

            // Construct a new datagram, adding this sensor's address and port to the address list
            temp_update_datagram temp_update_response;
            temp_update_response.header[0] = 'T';
            temp_update_response.header[1] = 'E';
            temp_update_response.header[2] = 'M';
            temp_update_response.header[3] = 'P';
            temp_update_response.id = id;
            temp_update_response.timestamp = recv_timestamp;
            temp_update_response.temperature = recv_temp;
            temp_update_response.address_count = recv_address_count + 1;                            // Add this sensor to the count
            for (int i = 0; i < recv_address_count; i++)
            {
                temp_update_response.address_list[i] = recv_addr_list[i];
            }
            temp_update_response.address_list[recv_address_count].sensor_addr = ts_addr.sin_addr;
            temp_update_response.address_list[recv_address_count].sensor_port = ts_addr.sin_port;

            // // Print the addresses on the datagram
            // printf("Addresses on the datagram:\n");
            // for (int i = 0; i < temp_update_response.address_count; i++)
            // {
            //     printf("%s:%d\n", inet_ntoa(temp_update_response.address_list[i].sensor_addr), ntohs(temp_update_response.address_list[i].sensor_port));
            // }

            // // Print the addresses on this sensors receiver list
            // printf("Addresses on this sensors receiver list:\n");
            // for (int i = 0; i < num_receivers; i++)
            // {
            //     printf("%s\n", receiver_address_port[i]);
            // }

            // Send the datagram to each receiver that does not appear on the datagram's address list
            for (int i = 0; i < num_receivers; i++)
            {
                // Parse receiver address and port
                char *receiver_address_port_str = receiver_address_port[i];
                char receiver_addr_str[100];
                int receiver_port;
                sscanf(receiver_address_port_str, "%[^:]:%d", receiver_addr_str, &receiver_port);

                // Create Address and send the temp update
                struct sockaddr_in receiver_addr;
                memset(&receiver_addr, 0, sizeof(receiver_addr));
                receiver_addr.sin_family = AF_INET;
                receiver_addr.sin_port = htons(receiver_port);
                if (inet_pton(AF_INET, receiver_addr_str, &receiver_addr.sin_addr) != 1)
                {
                    perror("inet_pton");
                    exit(1);
                }
                int found = 0;
                for (int j = 0; j < recv_address_count; j++)
                {
                    if ((recv_addr_list[j].sensor_port == receiver_addr.sin_port))
                    {
                        found = 1;
                        break;
                    }
                }
                if (!found)
                {
                    int len = sendto(ts_fd, &temp_update_response, sizeof(temp_update_response), 0, (struct sockaddr *)&receiver_addr, sizeof(receiver_addr));
                    if (len == -1)
                    {
                        perror("sendto");
                        exit(1);
                    }
                    printf("Sent %d bytes. From recv msg\n", len);
                }

                // Get the current time
                gettimeofday(&last_update_time, NULL);
                
            }
        } else if (len == -1)
        {
            // printf("errno is %d\n", errno);
            if (errno == EAGAIN || errno == EWOULDBLOCK) 
            {
            // No data available right now, can try again later
            // printf("No data available right now, can try again later\n");
            } else {
                printf("Error receiving datagram\n");
                perror("recvfrom");
            }
        }

        // Lock the mutex and wait on cond using pthread_cond_timedwait to ensure that the maximum waiting time is the max condvar wait
        pthread_mutex_lock(&shm_ts->mutex);
        // printf("Waiting on cond\n");
        struct timespec ts;
        clock_gettime(CLOCK_REALTIME, &ts);
        ts.tv_nsec += max_condvar_wait * 1000;
        pthread_cond_timedwait(&shm_ts->cond, &shm_ts->mutex, &ts);
        // printf("Woke up from cond\n");
    }

    return 0;
}