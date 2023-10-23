#include <stdio.h>     
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>    
#include <string.h>    
#include <stddef.h>    
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

    //now we have shared access to the database we can populate it with data received over TCP

    while ((bytes_read = read(sock, buffer, sizeof(buffer) - 1)) > 0) {
        buffer[bytes_read] = '\0';
        printf("Received: %s\n", buffer);
        //split the buffer by the spaces
        char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
        int count = 0;
        splitStringBySpaces(buffer, words, &count);
        if (strcmp("CARDREADER", words[0]) == 0){
            printf("id: %s\nmessage: %s\n", words[1], words[2]);
            //if hello then create the device object 
        }else if(strcmp("DOOR", words[0]) == 0){
            printf("id: %s\naddress: %s\nfail type: %s\n", words[1], words[2], words[3]);
        }else if(strcmp("FIREALARM ", words[0]) == 0){
            printf("addressport: %s\nmessage: %s\n", words[1], words[2]);
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
