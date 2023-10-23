#ifndef INIT_DEVICES_H
#define INIT_DEVICES_H

#include <pthread.h>
#include <stdlib.h>
#include <string.h>

#define LOCALHOST "127.0.0.1"



/////////////////////////INIT DEVICES//////////////////////////////////
struct deviceOverseer initDeviceOverseer(char* port, char* duration, char* delay, char* auth, char* conn, char* layout, char* shm_offset, shm_overseer_t *shm_ptr) {
    struct deviceOverseer overseer;
    strcpy(overseer.address_port, port);
    overseer.door_open_duration = duration;
    overseer.datagram_resend_delay = delay;
    overseer.auth_file = auth;
    overseer.conn_file = conn;
    overseer.layout_file = layout;
    overseer.shm_offset = shm_offset;
    overseer.shm_ptr = shm_ptr;
    
    //init MUTEX
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
    pthread_mutex_init(&overseer.shm_ptr->mutex, &attr);

    //init COND_VAR
    pthread_condattr_t cond_attr;
    pthread_condattr_init(&cond_attr);
    pthread_condattr_setpshared(&cond_attr, PTHREAD_PROCESS_SHARED);
    pthread_cond_init(&overseer.shm_ptr->cond, &cond_attr);

    //init DEFAULT
    overseer.shm_ptr->security_alarm = '-';

    return overseer;
}

struct deviceFireAlarm initDeviceFireAlarm(float threshold, int min_detections, int period ) {
    struct deviceFireAlarm fireAlarm;
    fireAlarm.port = -1; //placeholder allow main to handle ports.
    fireAlarm.temperature_threshold = threshold;
    fireAlarm.minimum_detections = min_detections;
    fireAlarm.detection_period = period;
    
    return fireAlarm;
}

struct deviceCardReader initDeviceCardReader(int reader_id, int time) {
    struct deviceCardReader reader;
    reader.port = -1; //placeholder allow main to handle ports.
    reader.id = reader_id;
    reader.wait_time = time;
    return reader;
}

struct deviceDoor initDeviceDoor(int door_id, char* type, int time) {
    struct deviceDoor door;
    door.port = -1; //placeholder allow main to handle ports.
    door.id = door_id;
    door.fail_type = type;
    door.open_close_time = time;
    return door;
}

struct deviceCallpoint initCallpoint(int delay) {
    struct deviceCallpoint point;
    point.port = -1; //placeholder allow main to handle ports.
    point.resend_delay = delay;
    return point;
}

struct deviceTempSensor initTempSensor(int sensor_id, int max_var_wait, int max_update, int addr, int port) {
    struct deviceTempSensor sensor;
    sensor.port = -1; //placeholder allow main to handle ports.
    sensor.id = sensor_id;
    sensor.max_cond_var_wait = max_var_wait;
    sensor.max_update_wait = max_update;
    sensor.reciever_addr = addr;
    sensor.reciever_port = port;
    return sensor;
}


/////////////////////////CAST FROM CONFIG AND CALL INIT DEVICES//////////////////////////////////
struct deviceOverseer callDeviceOverseerUsingSplitString(int port, const char* inputStr, int offset, shm_overseer_t *shm_ptr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 5) {
        printf("Not enough arguments for deviceOverseer\n");
        exit(EXIT_FAILURE);
    }

    char address_port[MAX_ADDRESS_PORT_LEN];
    sprintf(address_port, "%s:%d", LOCALHOST, port); 

    printf("test: address port %s\n", address_port);

    char str_offset[20];
    sprintf(str_offset, "%d", offset);

    return initDeviceOverseer(address_port, words[0], words[1], words[2], words[3], words[4], str_offset, shm_ptr);
}

struct deviceFireAlarm callDeviceFireAlarmUsingSplitString(const char* inputStr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 3) {
        printf("Not enough arguments for deviceFireAlarm\n");
        exit(EXIT_FAILURE);
    }

    return initDeviceFireAlarm(atof(words[0]), atoi(words[1]), atoi(words[2]));
}

struct deviceCardReader callDeviceCardReaderUsingSplitString(const char* inputStr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 3) {
        printf("Not enough arguments for deviceCardReader\n");
        exit(EXIT_FAILURE);
    }

    return initDeviceCardReader(atoi(words[0]), atoi(words[1])); 
}

struct deviceDoor callDeviceDoorUsingSplitString(const char* inputStr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 4) {
        printf("Not enough arguments for deviceDoor\n");
        exit(EXIT_FAILURE);
    }

    return initDeviceDoor(atoi(words[0]), words[1], atoi(words[2])); 
}

struct deviceCallpoint callCallpointUsingSplitString(const char* inputStr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 1) {
        printf("Not enough arguments for callpoint\n");
        exit(EXIT_FAILURE);
    }

    return initCallpoint(atoi(words[0]));
}

struct deviceTempSensor callTempSensorUsingSplitString(const char* inputStr) {
    char words[MAX_CONFIG_WORDS][MAX_CONFIG_WORD_LEN];
    int wordCount = 0;

    splitStringBySpaces(inputStr, words, &wordCount);
    
    if (wordCount < 6) {
        printf("Not enough arguments for tempsensor\n");
        exit(EXIT_FAILURE);
    }

    return initTempSensor(atoi(words[0]), atoi(words[1]), atoi(words[2]), atoi(words[3]), atoi(words[4])); 
}

#endif