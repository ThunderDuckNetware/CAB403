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
#include <errno.h>

#include "shm_units.h"

int main(int argc, char **argv) 
{
    // check arguments
    if (argc < 6)
    {
        fprintf(stderr, "usage: {id} {wait time (in microseconds)} {shared memory path} {shared memory offset} {overseer address:port}");
        exit(1);
    }

    // Read arguments
    int id = atoi(argv[1]);
    int waittime = atoi(argv[2]);
    const char *shm_path = argv[3];
    int shm_offset = atoi(argv[4]);
    const char *overseer_addr_port = argv[5];

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
    shm_cardreader *shm_cr =  (shm_cardreader *)(shm + shm_offset);

    // Pull out overseer address and port
    char overseer_addr_str[40];
    int overseer_port;
    sscanf(overseer_addr_port, "%[^:]:%d", overseer_addr_str, &overseer_port);

    // Create TCP socket
    int overseer_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (overseer_fd == -1)
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in overseer_addr;
    memset(&overseer_addr, 0, sizeof(overseer_addr));
    overseer_addr.sin_family = AF_INET;
    overseer_addr.sin_port = htons(overseer_port);
    if (inet_pton(AF_INET, overseer_addr_str, &overseer_addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }
    
    if (connect(overseer_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
    {
        perror("connect");
        exit(1);
    }

    // send hello msg to overseer
    char init_msg[40];
    sprintf(init_msg, "CARDREADER %d HELLO#", id);
    if (send(overseer_fd, init_msg, strlen(init_msg), 0) == -1)
    {
        perror("send");
        exit(1);
    }
    close(overseer_fd);

    // Normal Operation
    pthread_mutex_lock(&shm_cr->mutex);
    for (;;)
    {
        if (shm_cr->scanned[0] != '\0')
        {
            // open TCP connection to overseer with timeout setting
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

            // set timeout
            struct timeval tv;
            tv.tv_sec = waittime / 1000000;
            tv.tv_usec = waittime % 1000000;

            if (setsockopt(overseer_fd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv)) < 0) {
                perror("setsockopt");
                exit(1);
            }

            if (connect(overseer_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
            {
                perror("connect");
                exit(1);
            }

            // send scanned message to overseer
            char buf[17];
            memcpy(buf, shm_cr->scanned, 16);
            buf[16] = '\0';
            char scanned_msg[100];
            sprintf(scanned_msg, "CARDREADER %d SCANNED %s#", id, buf);
            if (send(overseer_fd, scanned_msg, strlen(scanned_msg), 0) == -1)
            {
                perror("send");
                exit(1);
            }

            // Receive message from overseer
            char recv_msg[100];
            int len = recv(overseer_fd, recv_msg, 100, 0);
            if (len == -1) {
                if (errno == EWOULDBLOCK || errno == EAGAIN || errno == ECONNREFUSED) {
                    // Timeout
                    shm_cr->response = 'N';
                } else {
                    perror("recv");
                    exit(1);
                }
            }
            recv_msg[len] = '\0';

            // Interpret message and set shm_cr->response
            if (strcmp(recv_msg, "ALLOWED#") == 0)
            {
                shm_cr->response = 'Y';
            }
            else
            {
                shm_cr->response = 'N';
            }

            pthread_cond_signal(&shm_cr->response_cond);
        }

        pthread_cond_wait(&shm_cr->scanned_cond, &shm_cr->mutex);
    }

    // Clean up and exit
    close(shm_fd);
    close(overseer_fd);

    return 0;
}

