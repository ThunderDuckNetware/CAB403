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

#include "overseer_structs.h"
#include "helper_func.h"
#include "shm_units.h"
#include "datagrams.h"

void *overseer_tcp_accept_thread_func(void *arg);

void init_database(int num_access_code, database_t* database){
    database->max_num_persons = num_access_code;
    database->personal_access = malloc(sizeof(personal_access_t) * num_access_code);
    database->num_persons = 0;
}

void init_personal_access(personal_access_t* personal_access){
    personal_access->access_code = "";
    personal_access->num_floors = 0;
    personal_access->num_doors = 0;
    personal_access->num_sectors = 0;
    personal_access->floors = calloc(1, sizeof(int));
    personal_access->doors = calloc(1, sizeof(door_access_t));
    personal_access->access_sectors = calloc(1, sizeof(int));
}

void init_door(door_access_t* door_access, int token){
    door_access->door_id = token;
    door_access->cardreader_id = calloc(1, sizeof(int));
}

//READ AUTH/CONNECTIONS/DOOR LAYOUT FILES
//function to read in auth  file
void read_input(const char* filename, char* type, database_t* database){
    FILE *file = fopen(filename, "r");  // Open the file for reading
    if (file == NULL) {
        perror("Failed to open file");
        exit(1);
    }

    while (!feof(file)) {
    
        char line_buffer[MAX_LINE_LENGTH];

        while (fgets(line_buffer, sizeof(line_buffer), file) != NULL)  {
            char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
            int wordCount = 0;

            //split the line at " "
            splitStringBySpaces(line_buffer, words, &wordCount);

            if (strcmp(type, "auth") == 0) {
                
                //we have a new access code so add it to our database
                printf("OVERSEER: adding new person: %s\n", words[0]);
                personal_access_t new_person;
                init_personal_access(&new_person);
                database->personal_access[database->num_persons] = new_person;
                personal_access_t *current_access = &database->personal_access[database->num_persons];
                current_access->access_code = words[0];

                for (int i = 1; i < wordCount; i++){

                    //split the word at :
                    const char* token = strtok((char*)words[i], ":");
                    while(token != NULL){
                        if (strcmp(token, "FLOOR") == 0){
                            printf("OVERSEER: adding floor\n");
                        } else if (strcmp(token, "DOOR") == 0){
                            token = strtok(NULL, ":");
                            printf("OVERSEER adding door: %s\n", token);
                            //create our new door
                            door_access_t new_door;
                            init_door(&new_door, atoi(token));

                            //append it to this persons door list
                            current_access->doors = appendValueDoor(current_access->doors, current_access->num_doors);
                            current_access->doors[current_access->num_doors] = new_door;

                            current_access->num_doors++;                        
                        } 
                        //go to the end of the word
                        token = strtok(NULL, ":");
                    }
                }
                database->num_persons++;

            } else if (strcmp(type, "connections") == 0) {
                //do something
            } else if (strcmp(type, "layout") == 0) {
                //do something
            } else {
                printf("Invalid type");
            }    

        }
    }
           
    fclose(file);  // Close the file
}

int main(int argc, char **argv)
{
    // Check arguments
    if (argc < 9)
    {   printf("num args: %d", argc);
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
    printf("test\n");
    fflush(stdout);
    int shm_offset = atoi(argv[8]);

    // Parse address and port
    char overseer_addr_str[100];
    int overseer_port;
    sscanf(address_port, "%[^:]:%d", overseer_addr_str, &overseer_port);

    //// TESTING ////
    printf("OVERSEER: address_port: %s\n", address_port);
    printf("OVERSEER: door_open_duration: %d\n", door_open_duration);
    printf("OVERSEER: datagram_resend_delay: %d\n", datagram_resend_delay);
    printf("OVERSEER: authorisation_file: %s\n", authorisation_file);
    printf("OVERSEER: connections_file: %s\n", connections_file);
    printf("OVERSEER: layout_file: %s\n", layout_file);
    printf("OVERSEER: shm_path: %s\n", shm_path);
    printf("OVERSEER: shm_offset: %d\n", shm_offset);

    //create a place to store our access data.
    database_t database;
    int num_access_code = countLines(authorisation_file);
    init_database(num_access_code, &database);

    read_input(authorisation_file, "auth", &database);

    //TODO (END): free any allocated memory.
    
    //// TESTING ////
/*
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
*/

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