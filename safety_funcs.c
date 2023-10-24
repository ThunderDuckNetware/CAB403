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
#include "datagrams.h"  


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