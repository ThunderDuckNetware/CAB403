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
#include "helper_func.h"


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

    // Open and map shared memory
    void *shm = open_shared_memory(shm_path);
    shm_cardreader *shm_cr =  (shm_cardreader *)(shm + shm_offset);

    // Create TCP socket and connect to the overseer address and port
    int overseer_fd = create_tcp_connection(overseer_addr_port, 0);

    // send hello msg to overseer and close connection
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
            overseer_fd = create_tcp_connection(overseer_addr_port, waittime);

            // send scanned message to overseer containing id and scan code
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
            recv_msg[len] = '\0';   // Null-terminate the received message

            // Interpret message and set shm_cr->response appropriately
            if (strcmp(recv_msg, "ALLOWED#") == 0)
            {
                shm_cr->response = 'Y';     // Approved access
            }
            else
            {
                shm_cr->response = 'N';     // Access denied
            }

            pthread_cond_signal(&shm_cr->response_cond);
        }

        pthread_cond_wait(&shm_cr->scanned_cond, &shm_cr->mutex);
    }

    return 0;
}