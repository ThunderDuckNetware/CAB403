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

#include "shm_units.h"
#include "datagrams.h"
#include "helper_func.h"

int main(int argc, char **argv)
{
    // Check arguments
    if (argc != 9)
    {
        fprintf(stderr, "Usage: {address:port} {temperature threshold} {min detections} {detection period (in microseconds)} {reserved argument} {shared memory path} {shared memory offset} {overseer address:port}");
        exit(1);
    }

    // Read arguments
    const char *fire_alarm_address_port = argv[1];
    int temperature_threshold = strToInt(argv[2]);
    int min_detections = strToInt(argv[3]);
    int detection_period = strToInt(argv[4]);
    const char *reserved_argument = argv[5];
    const char *shm_path = argv[6];
    int shm_offset = strToInt(argv[7]);
    const char *overseer_addr_port = argv[8];

    // Open and map shared memory
    void *shm = open_shared_memory(shm_path);
    shm_firealarm_t *shm_fire =  (shm_firealarm_t *)(shm + shm_offset);

    // Bind UDP socket
    int fire_unit_fd = bind_udp_socket(fire_alarm_address_port);

    // Open TCP socket to overseer
    int overseer_fd = create_tcp_connection(overseer_addr_port, 0);

    // Send Init message to overseer and close connection
    char init_msg[100];
    sprintf(init_msg, "FIREALARM %s HELLO#", fire_alarm_address_port);
    if (send(overseer_fd, init_msg, strlen(init_msg), 0) == -1)
    {
        perror("send");
        exit(1);
    }
    close(overseer_fd);

    // Init lists. Max 100 failsafe doors and 50 detections.
    const int MAX_DOOR = 100;
    door_reg_dgram failsafe_doors[MAX_DOOR];
    memset(failsafe_doors, 0, sizeof(failsafe_doors));
    const int MAX_DETECTIONS = 50;
    struct timeval detections[MAX_DETECTIONS];
    memset(detections, 0, sizeof(detections));

    // Normal Operation
    for (;;)
    {
        // Receive the next UDP datagram
        char recv_msg[100];
        int len = recvfrom(fire_unit_fd, recv_msg, 100, 0, NULL, NULL);
        if (len == -1)
        {
            perror("recvfrom");
            exit(1);
        } else if (len < 4) {
            fprintf(stderr, "Received datagram is too short\n");
            continue;
        }

        int emergency_flag = 0;
        // Check the datagram and act accordingly
        if (strncmp(recv_msg, "FIRE", 4) == 0)
        {
            emergency_flag = 1;

        }else if (strncmp(recv_msg, "TEMP", 4) == 0)
        {
            // Cast the datagram to a temp_update_datagram struct
            temp_update_datagram *temp_update = (temp_update_datagram *)recv_msg;

            // If the temperature is below the temperature threshold, loop back
            if (temp_update->temperature < temperature_threshold)
            {
                continue;
            }

            // Get current time
            struct timeval now;
            if (gettimeofday(&now, NULL) == -1)
            {
                perror("gettimeofday");
                exit(1);
            }

            // Calculate the time difference between the current time and the timestamp in the datagram
            const int MICROSECONDS_IN_SECOND = 1000000;
            int delta_seconds = now.tv_sec - temp_update->timestamp.tv_sec;
            int delta_microseconds = now.tv_usec - temp_update->timestamp.tv_usec;
            int total_delta_microseconds = (delta_seconds * MICROSECONDS_IN_SECOND) + delta_microseconds;

            // If the timestamp is more than {detection period} microseconds old, loop back
            if (total_delta_microseconds > detection_period)
            {
                continue;
            }

            // Delete all timestamps older than {detection period} microseconds from the detection list
            int j = 0;
            for (int i = 0; i < MAX_DETECTIONS; i++)
            {
                int delta_seconds = now.tv_sec - detections[i].tv_sec;
                int delta_microseconds = now.tv_usec - detections[i].tv_usec;
                int total_delta_microseconds = (delta_seconds * MICROSECONDS_IN_SECOND) + delta_microseconds;
                if (total_delta_microseconds < detection_period)
                {
                    detections[j] = detections[i];  // Shift the timestamp to the front of the list
                    j++;
                }
            }

            // Add the new timestamp to the detection list at the end of the sorted list
            detections[j] = temp_update->timestamp;

            // Zero out the rest of the detection list
            for (; j < MAX_DETECTIONS; j++) {
                detections[j].tv_sec = 0;
            }

            // If there are now at least {min detections} entries in the detection list, skip to 6
            int detection_count = 0;
            for (int i = 0; i < MAX_DETECTIONS; i++)
            {
                if (detections[i].tv_sec != 0)  // If the timestamp is not zeroed out
                {
                    detection_count++;
                }
            }
            if (detection_count >= min_detections) // If there are at least {min detections} entries in the detection list
            {
                emergency_flag = 1;
            }

        } else if (strncmp(recv_msg, "DOOR", 4) == 0) {
            // Cast the datagram to a door_reg_dgram struct
            door_reg_dgram *new_door = (door_reg_dgram *)recv_msg;

            // If the door is not already on the door list, add it
            int doorExists = 0;
            for (int i = 0; i < MAX_DOOR; i++)
            {
                if (failsafe_doors[i].door_port == new_door->door_port) // If the door is already on the door list
                {
                    doorExists = 1;
                    break;
                }
            }
            if (!doorExists)
            {
                for (int i = 0; i < MAX_DOOR; i++)
                {
                    if (failsafe_doors[i].door_port == 0) // Where there is an empty slot in the door list
                    {
                        failsafe_doors[i] = *new_door;
                        break;
                    }
                }

                // Send a door confirmation datagram to the overseer
                door_confirm_dgram confirm_door;
                confirm_door.header[0] = 'D';
                confirm_door.header[1] = 'R';
                confirm_door.header[2] = 'E';
                confirm_door.header[3] = 'G';
                confirm_door.door_addr = new_door->door_addr;
                confirm_door.door_port = new_door->door_port;

                // Open UDP socket to overseer and send confirmation datagram
                int overseer_udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                if (overseer_udp_fd == -1)
                {
                    perror("socket");
                    exit(1);
                }
                udp_send_to(overseer_udp_fd, &confirm_door, sizeof(confirm_door), overseer_addr_port);

                // // Close UDP socket to overseer
                close(overseer_udp_fd);
            }
        }

        // Step 6. Emergency Condition.
        if (emergency_flag)
        {
            pthread_mutex_lock(&shm_fire->mutex);
            shm_fire->alarm = 'A';
            pthread_mutex_unlock(&shm_fire->mutex);
            pthread_cond_signal(&shm_fire->cond);

            // For each door on the door list, open a TCP connection to it, send OPEN_EMERG#, then close the connection
            for (int i = 0; i < MAX_DOOR; i++)
            {
                if (failsafe_doors[i].door_port != 0)
                {
                    int door_fd = socket(AF_INET, SOCK_STREAM, 0);
                    if (door_fd == -1)
                    {
                        perror("socket");
                        exit(1);
                    }

                    struct sockaddr_in door_addr;
                    memset(&door_addr, 0, sizeof(door_addr));
                    door_addr.sin_family = AF_INET;
                    door_addr.sin_addr = failsafe_doors[i].door_addr;
                    door_addr.sin_port = failsafe_doors[i].door_port;

                    if (connect(door_fd, (struct sockaddr *)&door_addr, sizeof(door_addr)) == -1)
                    {
                        perror("connect");
                        exit(1);
                    }

                    // Send Init message to overseer and close connection
                    char emergency_msg[100] = "OPEN_EMERG#";
                    if (send(door_fd, emergency_msg, strlen(emergency_msg), 0) == -1)
                    {
                        perror("send");
                        exit(1);
                    }
                    close(door_fd);
                }
            }

            // Enter Emergency Loop
            for (;;) 
            {
                // Receive the next UDP datagram
                int len = recvfrom(fire_unit_fd, recv_msg, 100, 0, NULL, NULL);
                if (len == -1)
                {
                    perror("recvfrom");
                    exit(1);
                } else if (len < 4) {
                    fprintf(stderr, "Received datagram is too short\n");
                    continue;
                }

                if (strncmp(recv_msg, "DOOR", 4) == 0)
                {
                    // Open a TCP connection to the newly-registered door, send OPEN_EMERG#, then close the connection
                    door_reg_dgram *new_door = (door_reg_dgram *)recv_msg;

                    int door_fd = socket(AF_INET, SOCK_STREAM, 0);
                    if (door_fd == -1)
                    {
                        perror("socket");
                        exit(1);
                    }

                    struct sockaddr_in door_addr;
                    memset(&door_addr, 0, sizeof(door_addr));
                    door_addr.sin_family = AF_INET;
                    door_addr.sin_addr = new_door->door_addr;
                    door_addr.sin_port = new_door->door_port;

                    if (connect(door_fd, (struct sockaddr *)&door_addr, sizeof(door_addr)) == -1)
                    {
                        perror("connect");
                        exit(1);
                    }

                    // Send OPEN_EMERG# message to door
                    char emergency_msg[100] = "OPEN_EMERG#";
                    if (send(door_fd, emergency_msg, strlen(emergency_msg), 0) == -1)
                    {
                        perror("send");
                        exit(1);
                    }
                    // Close TCP connection to door
                    close(door_fd);

                    // Send a door confirmation datagram to the overseer
                    door_confirm_dgram confirm_door;
                    confirm_door.header[0] = 'D';
                    confirm_door.header[1] = 'R';
                    confirm_door.header[2] = 'E';
                    confirm_door.header[3] = 'G';
                    confirm_door.door_addr = new_door->door_addr;
                    confirm_door.door_port = new_door->door_port;

                    // Open UDP socket to overseer and send confirmation datagram
                    int overseer_udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                    if (overseer_udp_fd == -1)
                    {
                        perror("socket");
                        exit(1);
                    }
                    udp_send_to(overseer_udp_fd, &confirm_door, sizeof(confirm_door), overseer_addr_port);

                    close(overseer_udp_fd);
                }         
            }
        }
    }

    return 0;
}