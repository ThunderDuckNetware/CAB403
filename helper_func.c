#include <stdio.h>     
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>    
#include <string.h>    
#include <stddef.h> 
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <limits.h>   


#include "shm_units.h"
#include "device_structs.h"
#include "overseer_structs.h"
#include "helper_func.h"  
#include "datagrams.h"  


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


/**
 * open_shared_memory - Open and map a shared memory segment.
 * 
 * This function opens a shared memory segment specified by `shm_path`
 * and maps it into the process's virtual address space. The segment
 * is opened for reading and writing.
 * 
 * Parameters:
 *   - shm_path: The path to the shared memory segment.
 * 
 * Returns:
 *   - A pointer to the start of the mapped shared memory segment on success.
 *   - NULL on failure, with an appropriate error message printed to stderr.
 * 
 * Note: It is the caller's responsibility to unmap the shared memory 
 * (using munmap) when done with it.
 */
void *open_shared_memory(const char *shm_path) 
{
    // Open shared memory
    int shm_fd = shm_open(shm_path, O_RDWR, 0);
    if (shm_fd == -1) 
    {
        perror("shm_open");
        close(shm_fd);
        return NULL;
    }

    // Get shared memory size
    struct stat shm_stat;
    if (fstat(shm_fd, &shm_stat) == -1) 
    {
        perror("fstat");
        close(shm_fd);
        return NULL;
    }

    // Map shared memory
    void *shm = mmap(NULL, shm_stat.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm == MAP_FAILED) 
    {
        perror("mmap");
        close(shm_fd);
        return NULL;
    }

    return shm;
}


/**
 * Create a TCP connection to a specified IP address and port.
 * 
 * This function takes a string in the format "IP:PORT", attempts to establish
 * a TCP connection to the given IP and port, and returns the file descriptor
 * of the connected socket.
 * 
 * @param
 *   - addr_port_str: A string in the format "IP:PORT", e.g., "127.0.0.1:8080".
 *   - timeout: The timeout value in microseconds. If timeout <= 0, no timeout
 * 
 * @return
 *   - An integer representing the file descriptor of the connected socket.
 * 
 * Errors:
 *   - If there's an error in parsing the IP address and port, socket creation, 
 *     address conversion, or connection, the function prints an error message 
 *     and exits the program.
 */
int create_tcp_connection(const char* addr_port_str, int timeout) 
{
    // Extract address and port
    char addr_str[40];
    int port;
    if (sscanf(addr_port_str, "%99[^:]:%d", addr_str, &port) != 2) 
    {
        fprintf(stderr, "Failed to parse address and port from string: %s\n", addr_port_str);
        exit(1);
    }

    // Create TCP socket
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd == -1) 
    {
        perror("socket");
        exit(1);
    }

    // Set timeout
    if (timeout > 0) 
    {
        struct timeval tv;
        tv.tv_sec = timeout / 1000000;
        tv.tv_usec = timeout % 1000000;

        if (setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv)) < 0) {
            perror("setsockopt");
            exit(1);
        }
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    if (inet_pton(AF_INET, addr_str, &addr.sin_addr) != 1) {
        perror("inet_pton");
        close(fd);
        exit(1);
    }

    // Connect
    if (connect(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("connect");
        close(fd);
        exit(1);
    }

    return fd;
}


/**
 * Creates a listening TCP socket on the given address and port.
 *
 * This function takes a string in the format "IP_ADDRESS:PORT", creates a 
 * TCP socket, binds it to the given IP address and port, and then starts
 * listening for incoming connections on that socket.
 *
 * @param
 * - addr_port_str: A string containing the IP address and port in the format "IP_ADDRESS:PORT"
 *                  For example: "192.168.1.10:8080".
 * - queue_size: The maximum number of pending connections the socket can queue.
 *               This is passed directly to the listen() system call.
 *
 * @return
 * - The file descriptor for the created listening socket.
 *
 * Errors:
 * - If there's any error during the socket creation, binding, or listening processes, 
 *   this function will print an error message to stderr and then exit the program.
 * - If the addr_port_str is not in the expected format, the program will also exit with an error message.
 */
int create_listening_tcp_socket(const char* addr_port_str, int queue_size) {
    // Extract address and port
    char addr_str[40];
    int port;
    if (sscanf(addr_port_str, "%99[^:]:%d", addr_str, &port) != 2) 
    {
        fprintf(stderr, "Failed to parse address and port from string: %s\n", addr_port_str);
        exit(1);
    }

    // Create TCP socket
    int listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (listen_fd == -1) {
        perror("socket");
        exit(1);
    }

    // Setup address
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    if (inet_pton(AF_INET, addr_str, &addr.sin_addr) != 1) {
        perror("inet_pton");
        close(listen_fd);
        exit(1);
    }

    // Bind
    if (bind(listen_fd, (struct sockaddr*)&addr, sizeof(addr)) == -1) {
        perror("bind");
        close(listen_fd);
        exit(1);
    }

    // Listen
    if (listen(listen_fd, queue_size) == -1) {
        perror("listen");
        close(listen_fd);
        exit(1);
    }

    return listen_fd;
}


/**
 * Convert a string to an integer.
 * 
 * The function attempts to convert the given string to an integer value.
 * The conversion is based on the strtol function, ensuring that the result
 * lies within the range of the int data type.
 *
 * If the conversion is unsuccessful due to invalid characters or if the
 * result is out of the int range, the function prints an error message
 * to stderr and terminates the program.
 *
 * @param:
 *  str The string to be converted.
 * 
 * @return:
 *  The integer representation of the string.
 *
 * Usage:
 * int value = strToInt("12345");
 * int anotherValue = strToInt("-987");
 * 
 * Error Handling:
 * For invalid inputs like "12a3" or numbers out of int range like 
 * "99999999999999999999", the function will print an error message
 * and terminate the program.
 */
int strToInt(const char *str) 
{
    char *endptr;
    long int result = strtol(str, &endptr, 10);

    // Check if the string is empty or if there are invalid characters in the string
    if (str == endptr || *endptr != '\0') 
    {
        fprintf(stderr, "Invalid number provided: %s\n", str);
        exit(EXIT_FAILURE);
    }

    // Check if the number is out of the range of int
    if (result > INT_MAX || result < INT_MIN) 
    {
        fprintf(stderr, "Number out of range for int: %s\n", str);
        exit(EXIT_FAILURE);
    }

    return (int)result;
}


/**
 * Send a TCP message.
 * 
 * This function takes a socket file descriptor and a message string, and
 * sends the message through the socket.
 * 
 * Parameters:
 *  - sock_fd: The socket file descriptor.
 * - msg: The message string to be sent.
 * 
 * Returns:
 * - 0 on success.
 * 
*/
int send_tcp_message(int sock_fd, const char *msg)
{
    if (send(sock_fd, msg, strlen(msg), 0) == -1)
    {
        perror("send");
        exit(1);
    }

    return 0;
}

/**
 * Bind a UDP socket to a specified IP address and port.
 * 
 * This function takes a string in the format "IP:PORT", attempts to bind
 * a UDP socket to the given IP and port, and returns the file descriptor
 * of the bound socket.
 * 
 * @param
 *   - addr_port_str: A string in the format "IP:PORT", e.g., "127.0.0.1:8080".
 * 
 * @return
 *   - An integer representing the file descriptor of the bound socket.
 * 
 * Errors:
 *   - If there's an error in parsing the IP address and port, socket creation, 
 *     address conversion, or binding, the function prints an error message 
 *     and exits the program.
 */
int bind_udp_socket(const char* addr_port_str) 
{
    // Extract address and port
    char addr_str[100];
    int port;
    if (sscanf(addr_port_str, "%99[^:]:%d", addr_str, &port) != 2) 
    {
        fprintf(stderr, "Failed to parse address and port from string: %s\n", addr_port_str);
        exit(1);
    }

    // Create UDP socket
    int fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd == -1) 
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    if (inet_pton(AF_INET, addr_str, &addr.sin_addr) != 1) 
    {
        perror("inet_pton");
        close(fd);
        exit(1);
    }

    // Bind
    if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) == -1) 
    {
        perror("bind");
        close(fd);
        exit(1);
    }

    return fd;
}


/**
 * Send a message over UDP to a specified IP address and port.
 * 
 * This function takes a string in the format "IP:PORT", creates a socket address
 * based on it, and sends a message using the `sendto()` function.
 * 
 * @param
 *   - udp_fd: The UDP socket file descriptor.
 *   - message: Pointer to the message to be sent.
 *   - len: Length of the message.
 *   - addr_port_str: A string in the format "IP:PORT", e.g., "127.0.0.1:8080".
 * 
 * Errors:
 *   - If there's an error in parsing the IP address and port, address conversion, 
 *     or sending the message, the function prints an error message and exits the program.
 */
void udp_send_to(int udp_fd, const void *message, size_t len, const char *addr_port_str)
{
    // Extract address and port from the string
    char addr_str[100];
    int port;
    if (sscanf(addr_port_str, "%99[^:]:%d", addr_str, &port) != 2) 
    {
        fprintf(stderr, "Failed to parse address and port from string: %s\n", addr_port_str);
        exit(1);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    if (inet_pton(AF_INET, addr_str, &addr.sin_addr) != 1) 
    {
        perror("inet_pton");
        exit(1);
    }

    // Send the message using sendto()
    if (sendto(udp_fd, message, len, 0, (struct sockaddr *)&addr, sizeof(addr)) == -1)
    {
        perror("sendto");
        exit(1);
    }
}
