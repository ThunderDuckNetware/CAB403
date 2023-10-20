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
    int temperature_threshold = atoi(argv[2]);
    int min_detections = atoi(argv[3]);
    int detection_period = atoi(argv[4]);
    const char *reserved_argument = argv[5];
    const char *shm_path = argv[6];
    int shm_offset = atoi(argv[7]);
    const char *overseer_addr_port = argv[8];

    // printf("min detections: %d\n", min_detections);
    // printf("detection period: %d\n", detection_period);
    // printf("Overseer Adress: %s\n", overseer_addr_port);


    // Parse fire alarm unit address and port
    char fire_alarm_addr_str[100];
    int fire_alarm_port;
    sscanf(fire_alarm_address_port, "%[^:]:%d", fire_alarm_addr_str, &fire_alarm_port);

    // Bind UDP socket
    int fire_unit_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fire_unit_fd == -1)
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in fire_alarm_addr;
    memset(&fire_alarm_addr, 0, sizeof(fire_alarm_addr));
    fire_alarm_addr.sin_family = AF_INET;
    fire_alarm_addr.sin_port = htons(fire_alarm_port);
    if (inet_pton(AF_INET, fire_alarm_addr_str, &fire_alarm_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }

    if (bind(fire_unit_fd, (struct sockaddr *)&fire_alarm_addr, sizeof(fire_alarm_addr)) == -1)
    {
        perror("bind");
        exit(1);
    }

    // Parse overseer address and port
    char overseer_addr_str[100];
    int overseer_port;
    sscanf(overseer_addr_port, "%[^:]:%d", overseer_addr_str, &overseer_port);

    // Open socket to overseer
    int overseer_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (overseer_fd == -1)
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in overseer_addr;
    memset(&overseer_addr, 0, sizeof(overseer_addr));
    if (inet_pton(AF_INET, overseer_addr_str, &overseer_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }
    overseer_addr.sin_family = AF_INET;
    overseer_addr.sin_port = htons(overseer_port);

    if (connect(overseer_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
    {
        perror("connect");
        exit(1);
    }

    // Send Init message to overseer and close connection
    char init_msg[100];
    sprintf(init_msg, "FIREALARM %s HELLO#", fire_alarm_address_port);
    if (send(overseer_fd, init_msg, strlen(init_msg), 0) == -1)
    {
        perror("send");
        exit(1);
    }
    close(overseer_fd);

    // Open shared memory
    int shm_fd = shm_open(shm_path, O_RDWR, 0);
    if (shm_fd == -1) {
        perror("shm_open");
        exit(1);
    }

    // Get shared memory size
    struct stat shm_stat;
    if (fstat(shm_fd, &shm_stat) == -1) {
        perror("fstat");
        close(shm_fd);
        exit(1);
    }

    // Map shared memory
    char *shm = mmap(NULL, shm_stat.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm == MAP_FAILED) {
        perror("mmap");
        close(shm_fd);
        exit(1);
    }
    shm_firealarm *shm_fire =  (shm_firealarm *)(shm + shm_offset);

    // Init lists. 100 failsafe doors and 50 detections.
    const int MAX_DOORS = 100;
    door_reg_dgram *failsafe_doors[MAX_DOORS];
    memset(failsafe_doors, 0, sizeof(failsafe_doors));
    const int MAX_DETECTIONS = 50;
    temp_update_datagram *detections[MAX_DETECTIONS];

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

            int delta_seconds = now.tv_sec - temp_update->timestamp.tv_sec;
            int delta_microseconds = now.tv_usec - temp_update->timestamp.tv_usec;
            int total_delta_microseconds = (delta_seconds * 1000000) + delta_microseconds;
            // If the timestamp is more than {detection period} microseconds old, loop back
            if (total_delta_microseconds > detection_period)
            {
                continue;
            }

            // Delete all timestamps older than {detection period} microseconds from the detection list
            int j = 0;
            for (int i = 0; i < MAX_DETECTIONS; i++)
            {
                int delta_seconds = now.tv_sec - detections[i]->timestamp.tv_sec;
                int delta_microseconds = now.tv_usec - detections[i]->timestamp.tv_usec;
                int total_delta_microseconds = (delta_seconds * 1000000) + delta_microseconds;
                if (total_delta_microseconds < detection_period)
                {
                    detections[j] = detections[i];
                    j++;
                }
            }

            // Add the new timestamp to the detection list
            detections[j] = temp_update;

            // NULL terminate the detection list
            for (; j < MAX_DETECTIONS; j++) {
                detections[j] = NULL;
            }

            // If there are now at least {min detections} entries in the detection list, skip to 6
            int detection_count = 0;
            for (int i = 0; i < MAX_DETECTIONS; i++)
            {
                if (detections[i] != NULL)
                {
                    detection_count++;
                }
            }
            if (detection_count >= min_detections)
            {
                emergency_flag = 1;
            }
        } else if (strncmp(recv_msg, "DOOR", 4) == 0) {
            // Cast the datagram to a door_reg_dgram struct
            door_reg_dgram *new_door = (door_reg_dgram *)recv_msg;

            int doorExists = 0;
            // First, check if the door is already in the list
            for (int i = 0; i < MAX_DOORS; i++)
            {
                if (failsafe_doors[i] != NULL && failsafe_doors[i]->door_port == new_door->door_port)
                {
                    doorExists = 1;
                    break;
                }
            }
            // If not in the list, find an empty spot and add it
            if (!doorExists)
            {
                for (int i = 0; i < MAX_DOORS; i++)
                {
                    if (failsafe_doors[i] == NULL) 
                    {
                        failsafe_doors[i] = new_door;
                        break;
                    }
                }

                // Print received door details for debugging
                printf("Received Door Datagram:\n");
                printf("Address: %s\n", inet_ntoa(new_door->door_addr));  // Converts the IP address to a string format
                printf("Port: %d\n", ntohs(new_door->door_port));  // Converts network byte order to host byte order for the port

                // TODO: Overseer not receiving datagram correctly
                // Send a door confirmation datagram to the overseer
                door_confirm_dgram confirm_door;
                confirm_door.header[0] = 'D';
                confirm_door.header[1] = 'R';
                confirm_door.header[2] = 'E';
                confirm_door.header[3] = 'G';
                confirm_door.door_addr = new_door->door_addr;
                confirm_door.door_port = new_door->door_port;

                // Print confirmation door details for debugging
                printf("Sending Confirmation Datagram:\n");
                printf("Header: %c%c%c%c\n", confirm_door.header[0], confirm_door.header[1], confirm_door.header[2], confirm_door.header[3]);
                printf("Address: %s\n", inet_ntoa(confirm_door.door_addr));  // Converts the IP address to a string format
                printf("Port: %d\n", ntohs(confirm_door.door_port));

                // Open UDP socket to overseer
                int overseer_udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                if (overseer_udp_fd == -1)
                {
                    perror("socket");
                    exit(1);
                }

                // Allow the reuse of the port
                int optval = 1;
                if (setsockopt(overseer_udp_fd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval)) == -1)
                {
                    perror("setsockopt");
                    exit(1);
                }

                if (bind(overseer_udp_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
                {
                    perror("bind");
                    exit(1);
                }

                // Send on UDP overseer_udp_fd
                int len = sendto(overseer_udp_fd, &confirm_door, sizeof(confirm_door), 0, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr));
                if ( len == -1)
                {
                    perror("sendto");
                    exit(1);
                }

                // Close UDP socket to overseer
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
            for (int i = 0; i < MAX_DOORS; i++)
            {
                if (failsafe_doors[i] != NULL)
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
                    door_addr.sin_addr = failsafe_doors[i]->door_addr;
                    door_addr.sin_port = failsafe_doors[i]->door_port;

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

                    printf("Connection refused here?\n");
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

                    // Send a door confirmation datagram to the overseer
                    door_confirm_dgram confirm_door;
                    confirm_door.header[0] = 'D';
                    confirm_door.header[1] = 'R';
                    confirm_door.header[2] = 'E';
                    confirm_door.header[3] = 'G';
                    confirm_door.door_addr = new_door->door_addr;
                    confirm_door.door_port = new_door->door_port;

                    // Open UDP socket to overseer
                    int overseer_udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
                    if (overseer_udp_fd == -1)
                    {
                        perror("socket");
                        exit(1);
                    }

                    // Allow the reuse of the port
                    int optval = 1;
                    if (setsockopt(overseer_udp_fd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval)) == -1)
                    {
                        perror("setsockopt");
                        exit(1);
                    }

                    if (bind(overseer_udp_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
                    {
                        perror("bind");
                        exit(1);
                    }

                    // Send on UDP overseer_udp_fd
                    if (sendto(overseer_udp_fd, &confirm_door, sizeof(confirm_door), 0, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
                    {
                        perror("sendto");
                        exit(1);
                    }

                    close(overseer_udp_fd);
                }         
            }
        }
    }

    return 0;
}