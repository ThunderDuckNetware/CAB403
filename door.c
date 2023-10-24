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
#include "safety_funcs.h"


int main(int argc, char **argv)
{
    /* check arguments */
    if (argc < 7)
    {
        fprintf(stderr, "usage: {id} {address:port} {FAIL_SAFE | FAIL_SECURE} {shared memory path} {shared memory offset} {overseer address:port}");
        return -1;
    }

    /* Read arguments */
    int id = strToInt(argv[1]);
    char *address_port = argv[2];
    char *mode = argv[3];
    const char *shm_path = argv[4];
    int shm_offset = strToInt(argv[5]);
    const char *overseer_addr_port = argv[6];

    /* Open and map shared memory */
    char *shm = open_shared_memory(shm_path);
    shm_door_t *shm_dr =  (shm_door_t *)(shm + shm_offset);

    /* Parse overseer address and port */
    char overseer_addr_str[100];
    int overseer_port;
    int itemsParsed = sscanf(overseer_addr_port, "%99[^:]:%d", overseer_addr_str, &overseer_port); /* 99 to prevent buffer overflow */
    if (itemsParsed != 2) {
        fprintf(stderr, "Invalid address:port format: %s\n", overseer_addr_port);
        return -2;
    }

    /* Create TCP socket and connect to the overseer address and port */
    int overseer_fd = create_tcp_connection(overseer_addr_port, 0);

    /* Send message depending on mode. If mode is neither FAIL_SAFE nor FAIL_SECURE, exit with error. */
    char door_init_msg[100];
    if (sprintf(door_init_msg, "DOOR %d %s %s#", id, address_port, mode) < 0)
    {
        perror("sprintf");
        return -2;
    }
    if (strncmp(mode, "FAIL_SAFE", 9) == 0)
    {
        send_tcp_message(overseer_fd, door_init_msg);
    }
    else if (strncmp(mode, "FAIL_SECURE", 11) == 0)
    {
        send_tcp_message(overseer_fd, door_init_msg);
    }
    else
    {
        fprintf(stderr, "Invalid mode: %s\n", mode);
        return -3;
    }

    /* Close connection to overseer */
    if (close(overseer_fd) == -1)
    {
        perror("close");
        return -9;
    }

    /* Create tcp listening socket on the given address and port */
    int listen_fd = create_listening_tcp_socket(address_port, 10);  /* Queue size of 10 */
    
    /* Loop variables */
    int emergency_mode = 0;         /* 1 for emergency */
    int read_door_status_flag = 0;   
    char door_status;

    /* Initialise door_status */
    if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
        perror("pthread_mutex_lock");
        return -8;
    }
    door_status = shm_dr->status;
    if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
        perror("pthread_mutex_unlock");
        return -8;
    }

    for (;;)
    {
        if (read_door_status_flag)
        {
            if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
                perror("pthread_mutex_lock");
                return -8;
            }
            door_status = shm_dr->status;
            if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                perror("pthread_mutex_unlock");
                return -8;
            }
        }

        /* Accept the next TCP connection */
        int conn_fd = accept(listen_fd, NULL, NULL);
        if (conn_fd == -1)
        {
            perror("accept");
            return -3;
        }

        /* read the message from the client */
        char msg[100];
        int len = recv(conn_fd, msg, sizeof(msg), 0);
        if (len == -1)
        {
            perror("recv");
            return -6;
        }
        msg[len] = '\0';

        if (emergency_mode)
        {
            send_tcp_message(conn_fd, "EMERGENCY_MODE#");
            if (close(conn_fd) == -1)
            {
                perror("close");
                return -9;
            }

        } else
        {
            if ( (strncmp(msg, "OPEN#", 5) == 0) && (door_status == 'O'))
            {
                send_tcp_message(conn_fd, "ALREADY#");
                if (close(conn_fd) == -1)
                {
                    perror("close");
                    return -9;
                }

                read_door_status_flag = 0;

            } else if ( (strncmp(msg, "CLOSE#", 5) == 0) && (door_status == 'C')) {
                send_tcp_message(conn_fd, "ALREADY#");
                if (close(conn_fd) == -1)
                {
                    perror("close");
                    return -9;
                }

                read_door_status_flag = 0;

            } else if ((strncmp(msg, "OPEN#", 5) == 0) && (door_status == 'C')) {
                /* Change door status to opening */
                send_tcp_message(conn_fd, "OPENING#");
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) 
                {
                    perror("pthread_mutex_lock");
                    return -8;
                }
                shm_dr->status = 'o';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    return -8;
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    return -8;
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    return -8;
                }
                send_tcp_message(conn_fd, "OPENED#");

                if (close(conn_fd) == -1)
                {
                    perror("close");
                    return -9;
                }
                read_door_status_flag = 1;

            } else if ((strncmp(msg, "CLOSE#", 5) == 0) && (door_status == 'O')) {
                /* Change door status to closing */
                send_tcp_message(conn_fd, "CLOSING#");
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_lock");
                    return -8;
                }
                shm_dr->status = 'c';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    return -8;
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    return -8;
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    return -8;
                }
                send_tcp_message(conn_fd, "CLOSED#");

                if (close(conn_fd) == -1)
                {
                    perror("close");
                    return -9;
                }
                read_door_status_flag = 1;

            } else if ((strncmp(msg, "OPEN_EMERG#", 11) == 0) && (door_status == 'C')) {
                /* set emergency mode */
                emergency_mode = 1;

                /* Change door status to opening */
                if (pthread_mutex_lock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_lock");
                    return -8;
                }
                shm_dr->status = 'o';
                if (pthread_cond_signal(&shm_dr->cond_start) != 0) {
                    perror("pthread_cond_signal");
                    return -8;
                }
                if (pthread_cond_wait(&shm_dr->cond_end, &shm_dr->mutex) != 0) {
                    perror("pthread_cond_wait");
                    return -8;
                }
                if (pthread_mutex_unlock(&shm_dr->mutex) != 0) {
                    perror("pthread_mutex_unlock");
                    return -8;
                }

                read_door_status_flag = 1;

            } else if ((strncmp(msg, "OPEN_EMERG#", 11) == 0) && (door_status == 'O')) {
                /* set emergency mode */
                emergency_mode = 1;
                read_door_status_flag = 0;
            }
        }
    }

    return 0;
}