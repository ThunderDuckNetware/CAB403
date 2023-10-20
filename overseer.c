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

// Struct for storing id, address and port
typedef struct {
    int id;
    struct in_addr addr;
    in_port_t port;
    char *info[12]; // FAIL_SAFE or FAIL_SECURE for door controllers.
} id_addr_port;

// Struct for storing TCP thread parameters
typedef struct {
    int socket_fd;
} tcp_thread_params_t;

// Struct for storing UDP thread parameters
typedef struct {
    int server_fd;
    int client_fd;
    struct sockaddr_in client_addr;
} udp_thread_params_t;

void *overseer_tcp_accept_thread_func(void *arg);

int main(int argc, char **argv)
{
    // Check arguments
    if (argc < 9)
    {
        fprintf(stderr, "{address:port} {door open duration (in microseconds)} {datagram resend delay (in microseconds)} {authorisation file} {connections file} {layout file} {shared memory path} {shared memory offset}");
        exit(1);
    }

    // Read Arguments
    const char *address_port = argv[1];
    int door_open_duration = atoi(argv[2]);
    int datagram_resend_delay = atoi(argv[3]);
    const char *authorisation_file = argv[4];
    const char *connections_file = argv[5];
    const char *layout_file = argv[6];
    const char *shm_path = argv[7];
    int shm_offset = atoi(argv[8]);

    // Parse address and port
    char overseer_addr_str[100];
    int overseer_port;
    sscanf(address_port, "%[^:]:%d", overseer_addr_str, &overseer_port);

    // Bind and Listen on TCP socket
    int overseer_tcp_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (overseer_tcp_fd == -1)
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

    if (bind(overseer_tcp_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
    {
        perror("bind");
        exit(1);
    }

    if (listen(overseer_tcp_fd, 10) == -1)
    {
        perror("listen");
        exit(1);
    }

    // Bind UDP socket
    int overseer_udp_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (overseer_udp_fd == -1)
    {
        perror("socket");
        exit(1);
    }
    if (bind(overseer_udp_fd, (struct sockaddr *)&overseer_addr, sizeof(overseer_addr)) == -1)
    {
        perror("bind");
        exit(1);
    }

    // Normal Operation
    
    // Containers for Controllers and Units
    id_addr_port card_readers[10];
    id_addr_port door_controllers[10];
    id_addr_port fire_alarm_unit;
    memset(card_readers, 0, sizeof(card_readers));
    memset(door_controllers, 0, sizeof(door_controllers));
    memset(&fire_alarm_unit, 0, sizeof(fire_alarm_unit));

    // Create TCP accept thread
    pthread_t overseer_tcp_accept_thread;
    tcp_thread_params_t *tcp_thread_params = malloc(sizeof(tcp_thread_params_t));
    tcp_thread_params->socket_fd = overseer_tcp_fd;
    tcp_thread_params->addr = overseer_addr;
    if (pthread_create(&overseer_tcp_accept_thread, NULL, overseer_tcp_accept_thread_func, tcp_thread_params) != 0)
    {
        perror("pthread_create");
        free(tcp_thread_params);
        exit(1);
    }

    // Create UDP receive thread
    pthread_t overseer_udp_receive_thread;


    // Main Menu
    for(;;)
    {
 
    }

    return 0;
}

// Function for TCP accept thread
void *overseer_tcp_accept_thread_func(void *params)
{   
    // Cast params
    tcp_thread_params_t *tcp_thread_params = (tcp_thread_params_t *)params;

    // Accept TCP connections
    struct sockaddr_in overseer_client_addr;
    socklen_t overseer_client_addr_len = sizeof(overseer_client_addr);
    for (;;)
    {
        int overseer_client_fd = accept(tcp_thread_params->socket_fd, (struct sockaddr *)&overseer_client_addr, &overseer_client_addr_len);
        if (overseer_client_fd == -1)
        {
            perror("accept");
            exit(1);
        }

        // Read TCP message
        char tcp_msg[100];
        int tcp_msg_len = read(overseer_client_fd, tcp_msg, sizeof(tcp_msg) - 1);
        if (tcp_msg_len == -1)
        {
            perror("read");
            exit(1);
        }
        tcp_msg[tcp_msg_len] = '\0';

        // Print TCP message
        printf("TCP Message: %s\n", tcp_msg);

        // Clean up
        close(overseer_client_fd);
    }
    
    free(tcp_thread_params);
    return NULL;
}