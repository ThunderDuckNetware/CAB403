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


int main(int argc, char **argv)
{   
    // Check arguments
    if (argc != 5)
    {
        fprintf(stderr, "Usage: {resend delay (in microseconds)} {shared memory path} {shared memory offset} {fire alarm unit address:port}");
        exit(1);
    }

    // Read arguments
    int resend_delay = atoi(argv[1]);
    const char *shm_path = argv[2];
    int shm_offset = atoi(argv[3]);
    char *fire_alarm_address_port = argv[4];

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
    shm_callpoint *shm_cpt = (shm_callpoint *)(shm + shm_offset);

    // Parse fire alarm unit address and port
    char fire_alarm_addr_str[100];
    int fire_alarm_port;
    sscanf(fire_alarm_address_port, "%[^:]:%d", fire_alarm_addr_str, &fire_alarm_port);

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
    fire_emergency_dgram packet;
    packet.header[0] = 'F';
    packet.header[1] = 'I';
    packet.header[2] = 'R';
    packet.header[3] = 'E';

    // Normal Operation
    pthread_mutex_lock(&shm_cpt->mutex);
    for (;;)
    {
        if (shm_cpt->status == '*') 
        {
            for (;;)
            {
                // Send FIRE packet to fire alarm
                sendto(alarm_fd, &packet, sizeof(packet), 0, (struct sockaddr *)&fire_alarm_addr, sizeof(fire_alarm_addr));

                // Wait for resend_delay
                usleep(resend_delay);
            }
        } else {
            pthread_cond_wait(&shm_cpt->cond, &shm_cpt->mutex);
        }
    }

    return 0;
}