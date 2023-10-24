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

#include "shm_units.h"
#include "datagrams.h"
#include "helper_func.h"


int main(int argc, char **argv)
{   
    // Check arguments
    if (argc != 5)
    {
        fprintf(stderr, "Usage: {resend delay (in microseconds)} {shared memory path} {shared memory offset} {fire alarm unit address:port}");
        exit(1);
    }

    // Read arguments
    int resend_delay = strToInt(argv[1]);
    const char *shm_path = argv[2];
    int shm_offset = strToInt(argv[3]);
    char *fire_alarm_address_port = argv[4];

    // Open and map shared memory
    void *shm = open_shared_memory(shm_path);
    shm_callpoint_t *shm_cpt =  (shm_callpoint_t *)(shm + shm_offset);

    // Parse fire alarm unit address and port
    char fire_alarm_addr_str[100];
    int fire_alarm_port;
    int itemsParsed = sscanf(fire_alarm_address_port, "%99[^:]:%d", fire_alarm_addr_str, &fire_alarm_port); // 99 to prevent buffer overflow
    if (itemsParsed != 2) {
        fprintf(stderr, "Invalid address:port format: %s\n", fire_alarm_address_port);
        exit(1);
    }
    // Create UDP socket to fire alarm
    int alarm_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (alarm_fd == -1)
    {
        perror("socket");
        exit(1);
    }

    // Setup fire_alarm_addr
    struct sockaddr_in fire_alarm_addr;
    memset(&fire_alarm_addr, 0, sizeof(fire_alarm_addr));
	fire_alarm_addr.sin_family = AF_INET;
	fire_alarm_addr.sin_port = htons(fire_alarm_port);
    if (inet_pton(AF_INET, fire_alarm_addr_str, &fire_alarm_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }	

    // Set fire_emergency_dgram
    fire_emergency_dgram fire_emergency_packet;
    fire_emergency_packet.header[0] = 'F';
    fire_emergency_packet.header[1] = 'I';
    fire_emergency_packet.header[2] = 'R';
    fire_emergency_packet.header[3] = 'E';

    // Normal Operation
    pthread_mutex_lock(&shm_cpt->mutex);
    for (;;)
    {
        if (shm_cpt->status == '*')     // Fire emergency
        {
            for (;;)
            {
                // Send FIRE packet to fire alarm
                sendto(alarm_fd, &fire_emergency_packet, sizeof(fire_emergency_packet), 0, (struct sockaddr *)&fire_alarm_addr, sizeof(fire_alarm_addr));

                // Wait for resend_delay
                usleep(resend_delay);
            }
        } else {
            pthread_cond_wait(&shm_cpt->cond, &shm_cpt->mutex);
        }
    }

    return 0;
}