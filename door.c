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
#include "helper_func.h"


int main(int argc, char **argv)
{
    // check arguments
    if (argc < 7)
    {
        fprintf(stderr, "usage: {id} {address:port} {FAIL_SAFE | FAIL_SECURE} {shared memory path} {shared memory offset} {overseer address:port}");
        exit(1);
    }

    // Read arguments
    int id = strToInt(argv[1]);
    char *address_port = argv[2];
    char *mode = argv[3];
    const char *shm_path = argv[4];
    int shm_offset = strToInt(argv[5]);
    const char *overseer_addr_port = argv[6];

    // Open and map shared memory
    void *shm = open_shared_memory(shm_path);
    shm_door *shm_dr =  (shm_door *)(shm + shm_offset);

    // Parse overseer address and port
    char overseer_addr_str[100];
    int overseer_port;
    int itemsParsed = sscanf(overseer_addr_port, "%99[^:]:%d", overseer_addr_str, &overseer_port); // 99 to prevent buffer overflow
    if (itemsParsed != 2) {
        fprintf(stderr, "Invalid address:port format: %s\n", overseer_addr_port);
        exit(1);
    }

    // Create TCP socket and connect to the overseer address and port
    int overseer_fd = create_tcp_connection(overseer_addr_port, 0);

    // Send message depending on mode. If mode is neither FAIL_SAFE nor FAIL_SECURE, exit with error.
    char door_init_msg[100];
    if (sprintf(door_init_msg, "DOOR %d %s %s#", id, address_port, mode) < 0)
    {
        perror("sprintf");
        exit(1);
    }
    if (strcmp(mode, "FAIL_SAFE") == 0)
    {
        send_tcp_message(overseer_fd, door_init_msg);
    }
    else if (strcmp(mode, "FAIL_SECURE") == 0)
    {
        send_tcp_message(overseer_fd, door_init_msg);
    }
    else
    {
        fprintf(stderr, "Invalid mode: %s\n", mode);
        exit(1);
    }

    // Close connection to overseer
    close(overseer_fd);

    // Create tcp listening socket on the given address and port
    int listen_fd = create_listening_tcp_socket(address_port, 10);  // Queue size of 10
    
    // Loop variables
    int emergency_mode = 0;         // 1 for emergency
    int read_door_status_flag = 0;   
    char door_status;

    // Initialise door_status
    pthread_mutex_lock(&shm_dr->mutex);
    door_status = shm_dr->status;
    pthread_mutex_unlock(&shm_dr->mutex);

    for (;;)
    {
        if (read_door_status_flag)
        {
            pthread_mutex_lock(&shm_dr->mutex);
            door_status = shm_dr->status;
            pthread_mutex_unlock(&shm_dr->mutex);
        }

        // Accept the next TCP connection
        int conn_fd = accept(listen_fd, NULL, NULL);
        if (conn_fd == -1)
        {
            perror("accept");
            exit(1);
        }

        // read the message from the client
        char msg[100];
        int len = recv(conn_fd, msg, sizeof(msg), 0);
        if (len == -1)
        {
            perror("recv");
            exit(1);
        }
        msg[len] = '\0';

        if (emergency_mode)
        {
            send_tcp_message(conn_fd, "EMERGENCY_MODE#");
            close(conn_fd); 

        } else
        {
            if ( (strcmp(msg, "OPEN#") == 0) && (door_status == 'O'))
            {
                send_tcp_message(conn_fd, "ALREADY#");
                close(conn_fd);

                read_door_status_flag = 0;

            } else if ( (strcmp(msg, "CLOSE#") == 0) && (door_status == 'C')) {
                send_tcp_message(conn_fd, "ALREADY#");
                close(conn_fd);

                read_door_status_flag = 0;

            } else if ((strcmp(msg, "OPEN#") == 0) && (door_status == 'C')) {
                // Change door status to opening
                send_tcp_message(conn_fd, "OPENING#");
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) 
                {
                    perror("pthread_mutex_lock");
                    exit(EXIT_FAILURE);
                }
                shm_dr->status = 'o';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    exit(EXIT_FAILURE);
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    exit(EXIT_FAILURE);
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    exit(EXIT_FAILURE);
                }
                send_tcp_message(conn_fd, "OPENED#");

                close(conn_fd);
                read_door_status_flag = 1;

            } else if ((strcmp(msg, "CLOSE#") == 0) && (door_status == 'O')) {
                // Change door status to closing
                send_tcp_message(conn_fd, "CLOSING#");
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_lock");
                    exit(EXIT_FAILURE);
                }
                shm_dr->status = 'c';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    exit(EXIT_FAILURE);
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    exit(EXIT_FAILURE);
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    exit(EXIT_FAILURE);
                }
                send_tcp_message(conn_fd, "CLOSED#");

                close(conn_fd);
                read_door_status_flag = 1;

            } else if ((strcmp(msg, "OPEN_EMERG#") == 0) && (door_status == 'C')) {
                // set emergency mode
                emergency_mode = 1;

                // Change door status to opening
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_lock");
                    exit(EXIT_FAILURE);
                }
                shm_dr->status = 'o';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    exit(EXIT_FAILURE);
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    exit(EXIT_FAILURE);
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    exit(EXIT_FAILURE);
                }

                read_door_status_flag = 1;

            } else if ((strcmp(msg, "OPEN_EMERG#") == 0) && (door_status == 'O')) {
                // set emergency mode
                emergency_mode = 1;
                read_door_status_flag = 0;
            }
        }
    }

    return 0;
}