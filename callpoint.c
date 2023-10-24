/**
 * Safety Critical System
 * 
 * 
 * 
 * 
*/
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
#include "safety_funcs.h"


int main(int argc, char **argv)
{   
    /* Check arguments */
    if (argc != 5)
    {
        fprintf(stderr, "Usage: {resend delay (in microseconds)} {shared memory path} {shared memory offset} {fire alarm unit address:port}");
        return -1;
    }

    /* Read arguments */
    int resend_delay = strToInt(argv[1]);
    const char *shm_path = argv[2];
    int shm_offset = strToInt(argv[3]);
    const char *fire_alarm_address_port = argv[4];

    /* Open and map shared memory */
    char *shm = open_shared_memory(shm_path);
    shm_callpoint_t *shm_cpt =  (shm_callpoint_t *)(shm + shm_offset);

    /* Parse fire alarm unit address and port */
    char fire_alarm_addr_str[100];
    int fire_alarm_port;
    int itemsParsed = sscanf(fire_alarm_address_port, "%99[^:]:%d", fire_alarm_addr_str, &fire_alarm_port); /* 99 to prevent buffer overflow */
    if (itemsParsed != 2) {
        fprintf(stderr, "Invalid address:port format: %s\n", fire_alarm_address_port);
        return -2;
    }
    /* Create UDP socket to fire alarm */
    int alarm_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (alarm_fd == -1)
    {
        perror("socket");
        return -3;
    }

    /* Setup fire_alarm_addr */
    struct sockaddr_in fire_alarm_addr;
    memset(&fire_alarm_addr, 0, sizeof(fire_alarm_addr));
	fire_alarm_addr.sin_family = AF_INET;
	fire_alarm_addr.sin_port = htons(fire_alarm_port);
    if (inet_pton(AF_INET, fire_alarm_addr_str, &fire_alarm_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        return -4;
    }	

    /* Set fire_emergency_dgram */
    fire_emergency_dgram fire_emergency_packet;
    fire_emergency_packet.header[0] = 'F';
    fire_emergency_packet.header[1] = 'I';
    fire_emergency_packet.header[2] = 'R';
    fire_emergency_packet.header[3] = 'E';

    /* Normal Operation */
    if (pthread_mutex_lock(&shm_cpt->mutex) != 0)
    {
        perror("pthread_mutex_lock");
        return -8;
    }
    for (;;)
    {
        if (shm_cpt->status == '*')     /* Fire emergency */
        {
            for (;;)
            {
                /* Send FIRE packet to fire alarm */
                if (sendto(alarm_fd, &fire_emergency_packet, sizeof(fire_emergency_packet), 0, (struct sockaddr *)&fire_alarm_addr, sizeof(fire_alarm_addr)) == -1)
                {
                    perror("sendto");
                    return -6;
                }

                /* Wait for resend_delay */
                if (usleep(resend_delay) == -1)
                {
                    perror("usleep");
                    return -9;
                }
            }
        } else {
            if (pthread_cond_wait(&shm_cpt->cond, &shm_cpt->mutex) != 0)
            {
                perror("pthread_cond_wait");
                return -8;
            }
        }
    }

    return 0;
}