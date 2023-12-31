#ifndef HELPER_FUNC_H
#define HELPER_FUNC_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "shm_units.h"
#include "overseer_structs.h"
#include "device_structs.h"

#define MAX_CONFIG_WORDS 100   // maximum number of words in a string
#define MAX_CONFIG_WORD_LEN 50 // maximum length of each word
#define MAX_LINE_LENGTH 100
#define MAX_ARG_LENGTH 100
#define START_PORT 3000
#define MAX_CLIENTS 100


// Function prototypes
void splitStringBySpaces(const char* str, char output[][MAX_CONFIG_WORD_LEN], int* count);

void splitByColon(const char *str, char result[][MAX_CONFIG_WORD_LEN], int *count);

door_access_t* appendValueDoor(door_access_t* door_arr, int size);

deviceDoor_t* appendDeviceDoor(deviceDoor_t* arr, int size) ;

deviceCardReader_t* appendDeviceCardReader(deviceCardReader_t* arr, int size);

deviceFireAlarm_t* appendDeviceFireAlarm(deviceFireAlarm_t* arr, int size);

int* appendValueInt(int* arr, int size);

int countLines(const char *filename);

// TCP functions
void *TCP_server_thread(overseer_thread_data_t *thread_data);

void *handle_client(void *arg);

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
void *open_shared_memory(const char *shm_path);

/**
 * Create a TCP connection to a specified IP address and port.
 * 
 * This function takes a string in the format "IP:PORT", attempts to establish
 * a TCP connection to the given IP and port, and returns the file descriptor
 * of the connected socket.
 * 
 * Parameters:
 *   - addr_port_str: A string in the format "IP:PORT", e.g., "127.0.0.1:8080".
 * 
 * Returns:
 *   - An integer representing the file descriptor of the connected socket.
 * 
 * Errors:
 *   - If there's an error in parsing the IP address and port, socket creation, 
 *     address conversion, or connection, the function prints an error message 
 *     and exits the program.
 */
int create_tcp_connection(const char* addr_port_str, int timeout);

/**
 * Creates a listening TCP socket on the given address and port.
 *
 * This function takes a string in the format "IP_ADDRESS:PORT", creates a 
 * TCP socket, binds it to the given IP address and port, and then starts
 * listening for incoming connections on that socket.
 *
 * Parameters:
 * - addr_port_str: A string containing the IP address and port in the format "IP_ADDRESS:PORT"
 *                  For example: "192.168.1.10:8080".
 * - queue_size: The maximum number of pending connections the socket can queue.
 *               This is passed directly to the listen() system call.
 *
 * Returns:
 * - The file descriptor for the created listening socket.
 *
 * Errors:
 * - If there's any error during the socket creation, binding, or listening processes, 
 *   this function will print an error message to stderr and then exit the program.
 * - If the addr_port_str is not in the expected format, the program will also exit with an error message.
 */
int create_listening_tcp_socket(const char* addr_port_str, int queue_size);

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
int strToInt(const char *str);


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
int send_tcp_message(int sock_fd, const char *msg);

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
int bind_udp_socket(const char* addr_port_str);

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
void udp_send_to(int udp_fd, const void *message, size_t len, const char *addr_port_str);

#endif // HELPER_FUNC_H