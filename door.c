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

int create_listening_socket(const char *address, int port) {
    int listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (listen_fd == -1) {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(port);
    if (inet_pton(AF_INET, address, &server_address.sin_addr) != 1) {
        perror("inet_pton");
        close(listen_fd);
        exit(1);
    }

    if (bind(listen_fd, (struct sockaddr*)&server_address, sizeof(server_address)) == -1) {
        perror("bind");
        close(listen_fd);
        exit(1);
    }

    int n = 10;
    if (listen(listen_fd, n) == -1) {
        perror("listen");
        close(listen_fd);
        exit(1);
    }

    return listen_fd;
}

int send_message(int sock_fd, const char *msg)
{
    if (send(sock_fd, msg, strlen(msg), 0) == -1)
    {
        perror("send");
        exit(1);
    }

    return 0;
}

char *receive_message(int sock_fd)
{
    char *buf = malloc(100);
    int len = recv(sock_fd, buf, 100, 0);
    if (len == -1)
    {
        perror("recv");
        exit(1);
    }
    buf[len] = '\0';

    return buf;
}

int main(int argc, char **argv)
{
    // check arguments
    if (argc < 7)
    {
        fprintf(stderr, "usage: {id} {address:port} {FAIL_SAFE | FAIL_SECURE} {shared memory path} {shared memory offset} {overseer address:port}");
        exit(1);
    }

    // Read arguments
    int id = atoi(argv[1]);
    char *address_port = argv[2];
    char *mode = argv[3];
    const char *shm_path = argv[4];
    int shm_offset = atoi(argv[5]);
    const char *overseer_addr_port = argv[6];

    // Parse overseer address and port
    char overseer_addr[100];
    int overseer_port;
    sscanf(overseer_addr_port, "%[^:]:%d", overseer_addr, &overseer_port);

    // Open socket to overseer
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1)
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    if (inet_pton(AF_INET, overseer_addr, &addr.sin_addr) != 1)
    {
        perror("inet_pton");
        exit(1);
    }
    addr.sin_family = AF_INET;
    addr.sin_port = htons(overseer_port);

    if (connect(sock_fd, (struct sockaddr *)&addr, sizeof(addr)) == -1)
    {
        perror("connect");
        exit(1);
    }

    // Send message depending on mode. If mode is neither FAIL_SAFE nor FAIL_SECURE, exit with error.
    char init_msg[100];
    sprintf(init_msg, "DOOR %d %s %s#", id, address_port, mode);
    if (strcmp(mode, "FAIL_SAFE") == 0)
    {
        send_message(sock_fd, init_msg);
    }
    else if (strcmp(mode, "FAIL_SECURE") == 0)
    {
        send_message(sock_fd, init_msg);
    }
    else
    {
        fprintf(stderr, "Invalid mode: %s\n", mode);
        exit(1);
    }

    // Close connection to overseer
    close(sock_fd);

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
    shm_door *shared = (shm_door *)(shm + shm_offset);

    // Parse listening address and port
    char listening_addr[100];
    int listening_port;
    sscanf(address_port, "%[^:]:%d", listening_addr, &listening_port);

    // Create listening socket
    int listen_fd = create_listening_socket(listening_addr, listening_port);
    
    for (;;)
    {
        // Lock the mutex, retrieve the current door status, then unlock it
        pthread_mutex_lock(&shared->mutex);
        char door_status = shared->status;
        pthread_mutex_unlock(&shared->mutex);

        for (;;)
        {
            // Accept the next TCP connection
            int conn_fd = accept(listen_fd, NULL, NULL);

            // Variables for Emergency and Secure modes
            int emergency_mode = 0;
            int secure_mode = 0;

            // Receive message and handle it depending on the door status
            char *msg = receive_message(conn_fd);

            if ( (strcmp(msg, "OPEN#") == 0) && (door_status == 'O') && !(secure_mode))
            {
                send_message(conn_fd, "ALREADY#");
                close(conn_fd);
            } else if ( (strcmp(msg, "OPEN#") == 0) && (door_status == 'O') && (secure_mode)) {
                send_message(conn_fd, "SECURE_MODE#");
                close(conn_fd);
            }

            if ( (strcmp(msg, "CLOSE#") == 0) && (door_status == 'C') && !(emergency_mode) )
            {
                send_message(conn_fd, "ALREADY#");
                close(conn_fd);
            } else if ( (strcmp(msg, "CLOSE#") == 0) && (door_status == 'C') && (emergency_mode)) {
                send_message(conn_fd, "EMERGENCY_MODE#");
                close(conn_fd);
            }

            if ( (strcmp(msg, "OPEN#") == 0) && (door_status == 'C') && !(secure_mode) )
            {
                send_message(conn_fd, "OPENING#");

                pthread_mutex_lock(&shared->mutex);
                shared->status = 'o';
                pthread_cond_signal(&shared->cond_start);
                pthread_cond_wait(&shared->cond_end, &shared->mutex);
                pthread_mutex_unlock(&shared->mutex);

                send_message(conn_fd, "OPENED#");

                close(conn_fd);
                break;
            } else if ( (strcmp(msg, "OPEN#") == 0) && (door_status == 'C') && (secure_mode) ) {
                send_message(conn_fd, "SECURE_MODE#");
                close(conn_fd);
                break;
            }

            if ( (strcmp(msg, "CLOSE#") == 0) && (door_status == 'O') && !(emergency_mode) )
            {
                send_message(conn_fd, "CLOSING#");

                pthread_mutex_lock(&shared->mutex);
                shared->status = 'c';
                pthread_cond_signal(&shared->cond_start);
                pthread_cond_wait(&shared->cond_end, &shared->mutex);
                pthread_mutex_unlock(&shared->mutex);

                send_message(conn_fd, "CLOSED#");

                close(conn_fd);
                break;
            } else if ( (strcmp(msg, "CLOSE#") == 0) && (door_status == 'O') && (emergency_mode) ) {
                send_message(conn_fd, "EMERGENCY_MODE#");
                close(conn_fd);
                break;
            }

            if ( (strcmp(msg, "OPEN_EMERG#") == 0) && (door_status == 'C') )
            {
                // set emergency mode
                emergency_mode = 1;

                send_message(conn_fd, "OPENING#");

                pthread_mutex_lock(&shared->mutex);
                shared->status = 'o';
                pthread_cond_signal(&shared->cond_start);
                pthread_cond_wait(&shared->cond_end, &shared->mutex);
                pthread_mutex_unlock(&shared->mutex);

                send_message(conn_fd, "OPENED#");

                close(conn_fd);
                break;
            } else if ( (strcmp(msg, "OPEN_EMERG#") == 0) && (door_status == 'O') ) {
                // set emergency mode
                emergency_mode = 1;

                send_message(conn_fd, "ALREADY#");

                close(conn_fd);
                break;
            }

            // if ( (strcmp(msg, "CLOSE_SECURE#") == 0) && (door_status == 'O') )
            // {
            //     // set secure mode
            //     secure_mode = 1;

            //     send_message(conn_fd, "CLOSING#");

            //     pthread_mutex_lock(&shared->mutex);
            //     shared->status = 'c';
            //     pthread_cond_signal(&shared->cond_start);
            //     pthread_cond_wait(&shared->cond_end, &shared->mutex);
            //     pthread_mutex_unlock(&shared->mutex);

            //     send_message(conn_fd, "CLOSED#");

            //     close(conn_fd);
            //     break;
            // } else if ( (strcmp(msg, "CLOSE_SECURE#") == 0) && (door_status == 'C') ) {
            //     // set secure mode
            //     secure_mode = 1;

            //     send_message(conn_fd, "ALREADY#");

            //     close(conn_fd);
            //     break;
            // }
        }
    }

    return 0;
}