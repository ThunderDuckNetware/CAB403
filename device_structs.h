#ifndef DEVICE_STRUCTS_H
#define DEVICE_STRUCTS_H

// Max limits definitions
#define MAX_OVERSEER 1
#define MAX_FIRE_ALARM 1
#define MAX_CARD_READERS 40
#define MAX_DOORS 20
#define MAX_TEMP_SENSORS 20
#define MAX_CALLPOINTS 20


// Definition of different device types
struct deviceOverseer {
    char* address_port;
    char* door_open_duration;
    char* datagram_resend_delay;
    char* auth_file;
    char* conn_file;
    char* layout_file;
    shm_overseer shm;
    char* shm_offset;
};

struct deviceFireAlarm {
    int port;
    float temperature_threshold;
    int minimum_detections; 
    int detection_period; //us  
};

struct deviceCardReader {
    int port;
    int id;
    int wait_time; //us
};

struct deviceDoor{
    int port;
    int id;
    char* fail_type;
    int open_close_time;
};

struct deviceCallpoint {
    int port;
    int resend_delay; // us
};

struct deviceTempSensor {
    int port;
    int id;
    int max_cond_var_wait; //us
    int max_update_wait; //us
    int reciever_addr;
    int reciever_port; 
};

// Arrays for each device type
struct deviceOverseer overseers[MAX_OVERSEER];
struct deviceFireAlarm fireAlarms[MAX_FIRE_ALARM];
struct deviceCardReader cardReaders[MAX_CARD_READERS];
struct deviceDoor doors[MAX_DOORS];
struct deviceCallpoint callpoints[MAX_CALLPOINTS];
struct deviceTempSensor tempSensors[MAX_TEMP_SENSORS];

///////////////////////DEVICE COLLECTIONS//////////////////////
struct tempSensors{
    char* shm_name;
    int num_devices;
    struct deviceTempSensor devices[MAX_TEMP_SENSORS];
};

struct overseers{
    char* shm_name;
    int num_devices;
    struct deviceOverseer devices[MAX_OVERSEER];
};

struct fireAlarms{
    char* shm_name;
    int num_devices;
    struct deviceFireAlarm devices[MAX_FIRE_ALARM];
};

struct cardReaders{
    char* shm_name;
    int num_devices;
    struct deviceCardReader devices[MAX_CARD_READERS];
};

struct doors{
    char* shm_name;
    int num_devices;
    struct deviceDoor devices[MAX_DOORS];
};

struct callpoints{
    char* shm_name;
    int num_devices;
    struct deviceCallpoint devices[MAX_CALLPOINTS];
};

// Enum to track the type of deviceInfo currently pointed to
typedef enum {
    TYPE_DEVICE_OVERSEER,
    TYPE_DEVICE_FIREALARM,
    TYPE_DEVICE_CARDREADER,
    TYPE_DEVICE_DOOR,
    TYPE_DEVICE_CALLPOINT,
    TYPE_DEVICE_TEMPSENSOR,
    // ... add other types as needed
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