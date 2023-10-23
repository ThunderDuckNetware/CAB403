#ifndef OVERSEER_STRUCTS_H
#define OVERSEER_STRUCTS_H

#include <netinet/in.h>
#include <sys/socket.h>


//door struct
typedef struct{
    int door_id;
    int num_cardreaders;
    int *cardreader_id;
} door_access_t;

//elevators struct
typedef struct{
    //future dev
}elevators_access_t;

//personal access database
typedef struct{
    char* access_code;
    int num_floors;
    int num_doors;
    int num_sectors;
    door_access_t *doors;
    int *access_sectors;
    int *floors; //check
} personal_access_t;

typedef struct{
    int max_num_persons;
    int num_persons;
    personal_access_t *personal_access;
} database_t;

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


//shift these to structs if we get a chance.
typedef struct {
    database_t *database;
    fireAlarms_t *fireAlarms;
    cardReaders_t *cardReaders;
    doors_t *doors;
    int port;
    int* client_socket_ptr;
    pthread_mutex_t fireAlarms_mutex;
    pthread_mutex_t cardReaders_mutex;
    pthread_mutex_t doors_mutex;
} overseer_thread_data_t;

typedef struct {
    int client_socket;
    overseer_thread_data_t* shared_data;
} client_thread_data_t;

#endif //OVERSEER_STRUCTS_H