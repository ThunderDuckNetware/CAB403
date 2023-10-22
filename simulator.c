#include <stdio.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#include "helper_func.h"
#include "shm_units.h"
#include "device_structs.h"
#include "init_devices.h"

//shared memory names
char* shmloc_temp_sense = "/shm_temp_sense";
char* shmloc_card_reader = "/shm_card_reader";
char* shmloc_door = "/shm_door";
char* shmloc_callpoint = "/shm_callpoint";
char* shmloc_overseer = "/shm_overseer";
char* shmloc_fire_alarm = "/shm_fire_alarm";

//devices collections
struct overseers overseerCollection;
struct fireAlarms fireAlarmCollection;
struct cardReaders cardReaderCollection;
struct doors doorCollection;
struct callpoints callpointCollection;
struct tempSensors tempSensorCollection;

// track the number of devices
int num_overseers = 0;
int num_fireAlarms = 0;
int num_cardReaders = 0;
int num_doors = 0;
int num_callpoints = 0;
int num_tempSensors = 0;

//port number
int num_ports = 0;

void create_shm(size_t size, int num, char* name){
    int fd;
    size_t total_size = size * num;  // total memory required

    //Open the named shared memory segment for creation
    fd = shm_open(name, O_CREAT | O_TRUNC | O_RDWR, 0666);
    if (fd == -1) {
        perror("shm_open");
        exit(1);
    }

    //Set the size of the shared memory segment
    if (ftruncate(fd, total_size) == -1) {
        perror("ftruncate");
        exit(1);
    }

    //Map the shared memory segment into the process's address space
    void *baseAddress = mmap(NULL, total_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (baseAddress == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }

    // initialize the memory here
    memset(baseAddress, 0, total_size);

    //Cleanup
    //munmap(baseAddress, total_size);
    close(fd);
}


void check_input(int argc){
    if (argc < 2) {
        printf("Please provide an input file.\n");
        exit(1);
    }
    if (argc > 2) {
        printf("Too many arguments, please provide input file.\n");
        exit(1);
    }
}

void read_input(char *argv[]){
    FILE *file = fopen(argv[1], "r");  // Open the file for reading
    if (file == NULL) {
        perror("Failed to open file");
        exit(1);
    }

    while (!feof(file)) {
    
        char line_buffer[MAX_LINE_LENGTH];

        while (fgets(line_buffer, sizeof(line_buffer), file) != NULL)  {
            char *token;

            // Use strtok to get the first token
            token = strtok(line_buffer, " ");

            //printf("%s", token);
            if (strcmp(token, "INIT") != 1){
            //next token
                token = strtok(NULL, " ");
                if (token != NULL) { // check if token is NULL

                    char* restOfString = token + strlen(token) + 1;
                    
                    if (strcmp(token, "overseer") == 0){
                        printf("%s\n", restOfString);
                        int port = START_PORT + num_ports;
                        int offset = overseerCollection.num_devices * sizeof(shm_overseer);
                        printf("offset: %d\n", offset);
                        overseerCollection.devices[overseerCollection.num_devices] = callDeviceOverseerUsingSplitString(port, restOfString, offset);
                        overseerCollection.num_devices++;
/*
                    }else if(strcmp(token, "firealarm") == 0){
                        printf("%s\n", restOfString);
                        fireAlarmCollection.devices[fireAlarmCollection.num_devices] = callDeviceFireAlarmUsingSplitString(restOfString);
                        fireAlarmCollection.devices[fireAlarmCollection.num_devices].port = START_PORT + num_ports;
                        fireAlarmCollection.num_devices++;

                    }else if(strcmp(token,"cardreader") == 0){
                        printf("%s\n", restOfString);
                        cardReaderCollection.devices[cardReaderCollection.num_devices] = callDeviceCardReaderUsingSplitString(restOfString);
                        cardReaderCollection.devices[cardReaderCollection.num_devices].port = START_PORT + num_ports;
                        cardReaderCollection.num_devices++;

                    }else if(strcmp(token,"door") == 0){                        
                        printf("%s\n", restOfString);
                        doorCollection.devices[doorCollection.num_devices] = callDeviceDoorUsingSplitString(restOfString);
                        doorCollection.devices[doorCollection.num_devices].port = START_PORT + num_ports;
                        doorCollection.num_devices++;

                    }else if(strcmp(token,"tempsensor") == 0){
                        printf("%s\n", restOfString);
                        tempSensorCollection.devices[tempSensorCollection.num_devices] = callTempSensorUsingSplitString(restOfString);
                        tempSensorCollection.devices[tempSensorCollection.num_devices].port = START_PORT + num_ports;
                        tempSensorCollection.num_devices++;

                    }else if(strcmp(token,"callpoint") == 0){
                        printf("%s\n", restOfString);
                        callpointCollection.devices[callpointCollection.num_devices] = callCallpointUsingSplitString(restOfString);
                        callpointCollection.devices[callpointCollection.num_devices].port = START_PORT + num_ports;
                        callpointCollection.num_devices++;
*/
                    }else{
                        printf("CONFIG ERROR!\n");
                        break;
                        //exit(1);
                    }
                }
            }
            num_ports++;
        }
    }
    fclose(file);  // Close the file
}

void create_all_shm(){
    //Create our shared memory for each device type
    //Overseer
    create_shm(sizeof(shm_overseer), MAX_OVERSEER, shmloc_overseer );
    overseerCollection.num_devices = num_overseers;
    overseerCollection.shm_name = shmloc_overseer;
    //fireAlarm
    create_shm(sizeof(shm_firealarm), MAX_FIRE_ALARM, shmloc_fire_alarm  );
    fireAlarmCollection.num_devices = num_fireAlarms;
    fireAlarmCollection.shm_name = shmloc_fire_alarm;

    //cardReader
    create_shm(sizeof(shm_cardreader), MAX_CARD_READERS, shmloc_card_reader );
    cardReaderCollection.num_devices = num_cardReaders;
    cardReaderCollection.shm_name = shmloc_card_reader;

    //door
    create_shm(sizeof(shm_door), MAX_DOORS, shmloc_door );
    doorCollection.num_devices = num_doors;
    doorCollection.shm_name = shmloc_door;

    //callpoint
    create_shm(sizeof(shm_callpoint), MAX_CALLPOINTS, shmloc_callpoint);
    callpointCollection.num_devices = num_callpoints;
    callpointCollection.shm_name = shmloc_callpoint;

    //tempsensor
    create_shm(sizeof(shm_temp_sense_cntrl), MAX_TEMP_SENSORS, shmloc_temp_sense);
    tempSensorCollection.num_devices = num_tempSensors;
    tempSensorCollection.shm_name = shmloc_temp_sense;
}

int main(int argc, char *argv[]){

    //check our input, exit early if error
    check_input(argc);
    
    //Create our shared memory for each device type
    create_all_shm();

    //FUNCTION READ CONFIG
    read_input(argv);

    //IF MEMORY CONCIOUS TRIM THE SHM AND ARRAYS ONCE WE KNOW THE SIZE
    //CHILD ONLEY GETS A COPY OF GLOBAL SCOPE

    //FUNCTION CREATE PROCESSES
    printf("Spawning Overseer\n");
    //use fork() the parent process should call execl() to launch the overseer process
    pid_t pid;

    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        //Child Process
        sleep(0.25);
        printf("SIMULATOR: Launching other processes.\n");

    } else {
        // Parent process
        printf("SIMULATOR: Spawning Overseer\n");
        execl("./overseer", "overseer",
            overseerCollection.devices->address_port,
            overseerCollection.devices->door_open_duration,
            overseerCollection.devices->datagram_resend_delay,
            overseerCollection.devices->auth_file,
            overseerCollection.devices->conn_file,
            overseerCollection.devices->layout_file,
            overseerCollection.shm_name,
            overseerCollection.devices->shm_offset,
        NULL);
        perror("execl");
        exit(EXIT_FAILURE);
    }

    //wait 1 sec after starting processes

    //wait 1 sec after last event

    //terminate all processes and exit 

        
    return 0;
}