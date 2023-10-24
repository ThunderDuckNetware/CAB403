#ifndef HELPER_FUNC_H
#define HELPER_FUNC_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

#endif // HELPER_FUNC_H