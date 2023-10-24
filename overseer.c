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
#include "device_structs.h"
#include "overseer_structs.h"
#include "helper_func.h"


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
    door_access->num_cardreaders = 0;
    door_access->cardreader_id = calloc(1, sizeof(int));
}

void print_database(database_t* database){
    //print the contents of the user database
    printf("OVERSEER: CHECKING: printing database\n");
    for (int i = 0; i < database->num_persons; i++){
        printf("OVERSEER: person %d: %s\n", i, database->personal_access[i].access_code);
        printf("OVERSEER: person %d: num floors: %d\n", i, database->personal_access[i].num_floors);
        printf("OVERSEER: person %d: num doors: %d\n", i, database->personal_access[i].num_doors);
        printf("OVERSEER: person %d: num sectors: %d\n", i, database->personal_access[i].num_sectors);
        for (int j = 0; j < database->personal_access[i].num_floors; j++){
            printf("OVERSEER: person %d: floor %d: %d\n", i, j, database->personal_access[i].floors[j]);
        }
        for (int j = 0; j < database->personal_access[i].num_doors; j++){
            printf("OVERSEER: person %d: door %d: %d\n", i, j, database->personal_access[i].doors[j].door_id);
            for (int k = 0; k < database->personal_access[i].doors[j].num_cardreaders; k++){
                printf("OVERSEER: person %d: door %d: cardreader %d: %d\n", i, j, k, database->personal_access[i].doors[j].cardreader_id[k]);
            }
        }
        for (int j = 0; j < database->personal_access[i].num_sectors; j++){
            printf("OVERSEER: person %d: sector %d: %d\n", i, j, database->personal_access[i].access_sectors[j]);
        }
    }
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
                            token = strtok(NULL, ":");
                            printf("OVERSEER: adding floor\n");
                            //append it to this persons floor list
                            current_access->floors = appendValueInt(current_access->floors, current_access->num_floors);
                            current_access->floors[current_access->num_floors] = atoi(token);
                            current_access->num_floors++;

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
                //type //card id //door id
                //loop through our existing database and append this card id to the persons door id list
                for (int i = 0; i < database->num_persons; i++){
                    //we have found the person
                    personal_access_t *current_access = &database->personal_access[i];
                    if (strcmp("DOOR", words[0]) == 0){
                        
                        printf("OVERSEER: adding cardreader %s to persons door %s\n", words[1], words[2]);
                        //loop through their doors
                        for (int j = 0; j < database->personal_access[i].num_doors; j++){
                            if (current_access->doors[j].door_id == atoi(words[2])){
                                //we have found the door
                                printf("OVERSEER: adding cardreader %s to door %s\n", words[1], words[2]);
                                //append it to this persons cardreader list
                                current_access->doors[j].cardreader_id = appendValueInt(current_access->doors[j].cardreader_id, current_access->doors[j].num_cardreaders);
                                current_access->doors[j].cardreader_id[current_access->doors[j].num_cardreaders] = atoi(words[1]);
                                current_access->doors[j].num_cardreaders++;
                            }
                        }
                    }else if(strcmp("ELEVATOR", words[0]) == 0){
                        //out of spec
                    }else{
                        printf("Invalid type");
                    }
                }

            } else if (strcmp(type, "layout") == 0) {
                //layout file {type} {cardreader id} {sector}
                //loop through our existing database and append this sector to the persons sector list
                for (int i = 0; i < database->num_persons; i++){
                    //we have found the person
                    personal_access_t *current_access = &database->personal_access[i];
                    if (strcmp("CARDREADER", words[0]) == 0){
                        //loop through their doors
                        for (int j = 0; j < current_access->num_doors; j++){
                            for(int k = 0; k < current_access->doors[j].num_cardreaders; k++){
                                if (current_access->doors[j].cardreader_id[k] == atoi(words[1])){
                                    //we have found the cardreader
                                    printf("OVERSEER: adding sector %s to cardreader %s\n", words[2], words[1]);
                                    //append it to this persons sector list
                                    current_access->access_sectors = appendValueInt(current_access->access_sectors, current_access->num_sectors);
                                    current_access->access_sectors[current_access->num_sectors] = atoi(words[2]);
                                    current_access->num_sectors++;
                                }
                            }

                        }
                    }else if(strcmp("CAMERA", words[0]) == 0){
                        //out of spec
                    }
                    else if(strcmp("DESTSELECT", words[0]) == 0){
                        //out of spec
                    }else{
                        printf("Invalid type");
                    }
                }
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
    printf("OVERSEER: address_port: %d\n", overseer_port);
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
    read_input(connections_file, "connections", &database);
    printf("layout file:%s.\n", layout_file);
    fflush(stdout);
    read_input(layout_file, "layout", &database);
    print_database(&database);

    //create a place to store our devices
    // create mutex for these data structures
    
    fireAlarms_t fireAlarms;
    fireAlarms.num_devices = 0;
    fireAlarms.shm_name = "UNUSED";

    cardReaders_t cardReaders;
    cardReaders.num_devices = 0;
    cardReaders.shm_name = "UNUSED";

    doors_t doors;
    doors.num_devices = 0;
    doors.shm_name = "UNUSED";

    //access the shared memory (testing)
    shm_overseer_t *shm_overseer_ptr;
    int shm_fd = shm_open(shm_path, O_RDWR, 0660); 
    if (shm_fd == -1)
    {
        perror("shm_open");
        exit(1);
    }

    shm_overseer_ptr = mmap(NULL, sizeof(shm_overseer_t), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, shm_offset);
    if (shm_overseer_ptr == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }

    char alarm_status = shm_overseer_ptr->security_alarm;
    printf("alarm status: %c\n", alarm_status);
    //testing  

    //combine our datastores into a struct and pass it to the function
    overseer_thread_data_t thread_data;
    thread_data.database = &database;
    thread_data.fireAlarms = &fireAlarms;
    thread_data.cardReaders = &cardReaders;
    thread_data.doors = &doors;
    thread_data.port = overseer_port;
    thread_data.client_socket_ptr = NULL;
    pthread_mutex_init(&thread_data.fireAlarms_mutex, NULL);
    pthread_mutex_init(&thread_data.cardReaders_mutex, NULL);
    pthread_mutex_init(&thread_data.doors_mutex, NULL);

    TCP_server_thread(&thread_data);

 


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