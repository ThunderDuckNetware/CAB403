//door struct
typedef struct{
    int door_id;
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
    int *floors;
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
