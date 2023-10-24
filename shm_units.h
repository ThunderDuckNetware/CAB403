#ifndef SHM_UNITS_H
#define SHM_UNITS_H
#include <pthread.h>

//temperature sensor controller
typedef struct {
    float temperature;
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} shm_temp_sense_cntrl_t;

// Shared memory struct for card reader
typedef struct {
    char scanned[16];
    pthread_mutex_t mutex;
    pthread_cond_t scanned_cond;
    
    char response; // 'Y' or 'N' (or '\0' at first)
    pthread_cond_t response_cond;
} shm_cardreader_t;

// Shared memory struct for fire alarm callpoint controller
typedef struct {
    char status; // '-' for inactive, '*' for active
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} shm_callpoint_t;

// Shared memory struct for door controller
typedef struct {
    char status; // 'O' for open, 'C' for closed, 'o' for opening, 'c' for closing
    pthread_mutex_t mutex;
    pthread_cond_t cond_start;
    pthread_cond_t cond_end;
} shm_door_t;

// Shared memory struct for fire alarm unit
typedef struct {
    char alarm; // '-' if inactive, 'A' if active
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} shm_firealarm_t;

// Shared memory struct for overseer
typedef struct {
    char security_alarm; // '-' if inactive, 'A' if active
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} shm_overseer_t;

// Shared memory struct for temperature sensor
typedef struct {
    float temperature;
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} shm_tempsensor_t;

#endif