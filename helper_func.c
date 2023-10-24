#include <stdio.h>     
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>    
#include <string.h>    
#include <stddef.h>

#include "shm_units.h"
#include "device_structs.h"
#include "overseer_structs.h"
#include "helper_func.h"    


//split the config string into words
void splitStringBySpaces(const char* str, char output[][MAX_CONFIG_WORD_LEN], int* count) {
    int i = 0;
    const char* token = strtok((char*)str, " \r\n"); //] ensure original string isn't const

    while (token != NULL && i < MAX_CONFIG_WORDS) {
        strncpy(output[i], token, MAX_CONFIG_WORD_LEN);
        output[i][MAX_CONFIG_WORD_LEN-1] = '\0'; // ensure null-termination
        token = strtok(NULL, " \r\n");
        i++;
    }
    *count = i;
}

void splitByColon(const char *str, char result[][MAX_CONFIG_WORD_LEN], int *count) {
    char *token;
    char *input = strdup(str);  // Create a copy of the input string, because strtok modifies the original string

    token = strtok(input, ":\r\n");
    while (token != NULL) {
        strncpy(result[*count], token, MAX_CONFIG_WORD_LEN - 1);
        result[*count][MAX_CONFIG_WORD_LEN - 1] = '\0'; // Make sure it's null-terminated
        (*count)++;
        token = strtok(NULL, ":\r\n");
    }
    
    free(input);
}

door_access_t* appendValueDoor(door_access_t* arr, int size) {
    // Reallocate memory to increase size by 1
    door_access_t* newArr = realloc(arr, (size + 1) * sizeof(door_access_t));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

deviceDoor_t* appendDeviceDoor(deviceDoor_t* arr, int size) {
    // Reallocate memory to increase size by 1
    deviceDoor_t* newArr = realloc(arr, (size + 1) * sizeof(deviceDoor_t));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

deviceCardReader_t* appendDeviceCardReader(deviceCardReader_t* arr, int size) {
    // Reallocate memory to increase size by 1
    deviceCardReader_t* newArr = realloc(arr, (size + 1) * sizeof(deviceCardReader_t));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

deviceFireAlarm_t* appendFireAlarm(deviceFireAlarm_t* arr, int size) {
    // Reallocate memory to increase size by 1
    deviceFireAlarm_t* newArr = realloc(arr, (size + 1) * sizeof(deviceFireAlarm_t));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

int* appendValueInt(int* arr, int size) {
    // Reallocate memory to increase size by 1
    int* newArr = realloc(arr, (size + 1) * sizeof(int));
    if (newArr == NULL) {
        perror("Failed to reallocate memory");
        exit(1);
    }
    return newArr;
}

int countLines(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Failed to open the file");
        return -1;
    }

    int ch;
    long lines = 0;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            lines++;
        }
    }

    fclose(file);
    return lines;
}

void *handle_client(void *arg) {
    client_thread_data_t* client_data = (client_thread_data_t*) arg;
    int sock = client_data->client_socket;
    char buffer[60];
    int bytes_read;
    overseer_thread_data_t* shared_data = client_data->shared_data;


    //now we have shared access to the database we can populate it with data received over TCP

    while ((bytes_read = read(sock, buffer, sizeof(buffer) - 1)) > 0) {
        buffer[bytes_read] = '\0';
        printf("Received: %s\n", buffer);

        //split the buffer by the spaces
        char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
        int count = 0;
        splitStringBySpaces(buffer, words, &count);
        printf("type: .%s. id: .%s. msg:.%s.\n", words[0], words[1], words[2]);

        if (strcmp("CARDREADER", words[0]) == 0) {
            printf("is card reader\n");
            //device is starting up
            if (strcmp("HELLO#", words[2])==0){
                //get the id
                int id = atoi(words[1]);

                //lock the thread
                pthread_mutex_lock(&shared_data->cardReaders_mutex);
                deviceCardReader_t* this_device = &shared_data->cardReaders->devices[shared_data->cardReaders->num_devices];
                this_device->id = id;
                printf("saved id: %d\n", this_device->id);
                this_device->port = -1; // Unused.

                //print the actual values
                printf("OVERSEER TCP: Card Reader with id: %d initialized.\n", 
                    shared_data->cardReaders->devices[shared_data->cardReaders->num_devices].id);

                //unlock the data
                shared_data->cardReaders->num_devices++;
                pthread_mutex_unlock(&shared_data->cardReaders_mutex);
            }

        } else if (strcmp("DOOR", words[0]) == 0) {

            //new door lets add it into the database
            if(strcmp("FAIL_SAFE#", words[3]) == 0 || strcmp("FAIL_SECURE#", words[3]) == 0){

                //get the port number
                char substrings[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
                int count = 0;
                splitByColon(words[2], substrings, &count);
                int port = atoi(substrings[1]);

                //lock the thread
                pthread_mutex_lock(&shared_data->doors_mutex);
                deviceDoor_t* this_device = &shared_data->doors->devices[shared_data->doors->num_devices];
                this_device->id = atoi(words[1]);
                this_device->port = port; // port from address_port
                this_device->fail_type = words[3];

                //print the real values to test
                printf("OVERSEER TCP: Door with id: %d at port: %d with fail type: %s initialized.\n",
                shared_data->doors->devices[shared_data->doors->num_devices].id, 
                shared_data->doors->devices[shared_data->doors->num_devices].port, 
                shared_data->doors->devices[shared_data->doors->num_devices].fail_type);

                //unlocked the database
                shared_data->doors->num_devices++;
                pthread_mutex_unlock(&shared_data->doors_mutex);
            }


        } else if (strcmp("FIREALARM", words[0]) == 0) {

            if(strcmp("HELLO#", words[3]) == 0 )
            {
                //get the port number
                char substrings[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
                int count = 0;
                splitByColon(words[1], substrings, &count);
                int port = atoi(substrings[1]);

                //lock the thread
                pthread_mutex_lock(&shared_data->fireAlarms_mutex);
                deviceFireAlarm_t* this_device = &shared_data->fireAlarms->devices[shared_data->fireAlarms->num_devices];
                this_device->port = port; // Or extract port from address_port

                //print the actual value
                printf("OVERSEER TCP: Fire Alarm at address: %d initialized.\n", 
                    shared_data->fireAlarms->devices[shared_data->fireAlarms->num_devices].port);
                
                //unlock
                shared_data->fireAlarms->num_devices++;
                pthread_mutex_unlock(&shared_data->fireAlarms_mutex);
            }

        }
    }

    close(sock);
    return NULL;
}

void *TCP_server_thread(overseer_thread_data_t *thread_data) {
    
    int port = thread_data->port;
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    // Create socket
    int optval = 1;

    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval));
    if (server_socket == -1) {
        perror("Could not create socket");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen
    if (listen(server_socket, MAX_CLIENTS) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Listening on port %d...\n", port);

    while (1) {
        // Accept
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_len);
        if (client_socket < 0) {
            perror("Accept failed");
            continue;
        }

        printf("Connection accepted from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        //dynamically allocate memory for the client socket
        client_thread_data_t* client_data = (client_thread_data_t*)malloc(sizeof(client_thread_data_t));
        client_data->client_socket = client_socket; //new instance of client socket
        client_data->shared_data = thread_data; //ptr to our main database
        pthread_t client_thread;

        if (pthread_create(&client_thread, NULL, handle_client, client_data) < 0) {
            perror("Could not create client thread");
            free(client_data);
            continue;
        }

        //breakaway thread
        pthread_detach(client_thread);
    }

    close(server_socket);
    return NULL;
}

