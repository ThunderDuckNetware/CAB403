#ifndef DEVICE_STRUCTS_H
#define DEVICE_STRUCTS_H

// Max limits definitions
#define MAX_OVERSEER 1
#define MAX_FIRE_ALARM 1
#define MAX_CARD_READERS 40
#define MAX_DOORS 20
#define MAX_TEMP_SENSORS 20
#define MAX_CALLPOINTS 20
#define MAX_ADDRESS_PORT_LEN 20

// Definition of different device types
typedef struct {
    char address_port[MAX_ADDRESS_PORT_LEN];
    char* door_open_duration;
    char* datagram_resend_delay;
    char* auth_file;
    char* conn_file;
    char* layout_file;
    shm_overseer_t *shm_ptr;
    char* shm_offset;
}deviceOverseer_t;

typedef struct {
    int port;
    float temperature_threshold;
    int minimum_detections; 
    int detection_period; //us
    shm_firealarm_t *shm_ptr;  
}deviceFireAlarm_t;

typedef struct {
    int port;
    int id;
    int wait_time; //us
}deviceCardReader_t;

typedef struct {
    int port;
    int id;
    char* fail_type;
    int open_close_time;
}deviceDoor_t;

typedef struct {
    int port;
    int resend_delay; // us
}deviceCallpoint_t;

typedef struct {
    int port;
    int id;
    int max_cond_var_wait; //us
    int max_update_wait; //us
    int reciever_addr;
    int reciever_port; 
}deviceTempSensor_t;

// Arrays for each device type
deviceOverseer_t overseers[MAX_OVERSEER];
deviceFireAlarm_t fireAlarms[MAX_FIRE_ALARM];
deviceCardReader_t cardReaders[MAX_CARD_READERS];
deviceDoor_t doors[MAX_DOORS];
deviceCallpoint_t callpoints[MAX_CALLPOINTS];
deviceTempSensor_t tempSensors[MAX_TEMP_SENSORS];

///////////////////////DEVICE COLLECTIONS//////////////////////
typedef struct{
    char* shm_name;
    int num_devices;
    deviceTempSensor_t devices[MAX_TEMP_SENSORS];
}tempSensors_t;

typedef struct{
    char* shm_name;
    int num_devices;
    deviceOverseer_t devices[MAX_OVERSEER];
}overseers_t;

typedef struct{
    char* shm_name;
    int num_devices;
    deviceFireAlarm_t devices[MAX_FIRE_ALARM];
}fireAlarms_t;

typedef struct{
    char* shm_name;
    int num_devices;
    deviceCardReader_t devices[MAX_CARD_READERS];
}cardReaders_t;

typedef struct{
    char* shm_name;
    int num_devices;
    deviceDoor_t devices[MAX_DOORS];
}doors_t;

typedef struct{
    char* shm_name;
    int num_devices;
    deviceCallpoint_t devices[MAX_CALLPOINTS];
}callPoints_t;

// Enum to track the type of deviceInfo currently pointed to
typedef enum {
    TYPE_DEVICE_OVERSEER,
    TYPE_DEVICE_FIREALARM,
    TYPE_DEVICE_CARDREADER,
    TYPE_DEVICE_DOOR,
    TYPE_DEVICE_CALLPOINT,
    TYPE_DEVICE_TEMPSENSOR,
} DeviceType;

// Union that can store a pointer to any deviceInfo type
union DeviceInfoUnion {
    struct deviceOverseer* overseer;
    struct deviceFireAlarm* fireAlarm;
    struct deviceCardReader* cardReader;
    struct deviceDoor* door;
    struct deviceCallPoint* callPoint;
    struct deviceTempSensor* tempSensor;
};

// Definition of the main struct
struct device {
    int addr;
    int port_number;
    char type; 
    int mem_offset;
    DeviceType infoType;          // Enum field to indicate the type
    union DeviceInfoUnion infoUnion;  // Union field to store the actual pointer
};



#endif