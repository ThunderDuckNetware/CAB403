#ifndef DATAGRAMS_H
#define DATAGRAMS_H
#include <sys/time.h>

// Datagram for the fire alarm
typedef struct {
    char header[4]; // {'F', 'I', 'R', 'E'}
} fire_emergency_dgram;

// Datagram for the firealarm to register a door
typedef struct {
    char header[4]; // {'D', 'O', 'O', 'R'}
    struct in_addr door_addr;
    in_port_t door_port;
} door_reg_dgram;

// Datagram for the overseer to confirm a door registration
typedef struct {
    char header[4]; // {'D', 'R', 'E', 'G'}
    struct in_addr door_addr;
    in_port_t door_port;
} door_confirm_dgram;

// Sensor struct
struct addr_entry {
  struct in_addr sensor_addr;
  in_port_t sensor_port;
};

// Datagram sent by the temperature sensor
typedef struct {
  char header[4]; // {'T', 'E', 'M', 'P'}
  struct timeval timestamp;
  float temperature;
  uint16_t id;
  uint8_t address_count;
  struct addr_entry address_list[50];
} temp_update_datagram;

#endif