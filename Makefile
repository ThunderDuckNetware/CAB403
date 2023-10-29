CC = gcc
CFLAGS = -Wall
CFLAGS_SECURE = -Wall -Wextra -Wfloat-equal -Wundef -Wcast-align -Wwrite-strings -Wpedantic -Werror
LDFLAGS = -lrt -pthread

# All components you want to compile with just `make`
ALL_COMPONENTS = cardreader door callpoint firealarm simulator overseer

all: $(ALL_COMPONENTS)

# helper_func rules (assuming helper_func.c exists)
helper_func.o: helper_func.c helper_func.h
	$(CC) $(CFLAGS) -c helper_func.c

# safety_funcs rules (assuming helper_func.c exists)
safety_funcs.o: safety_funcs.c safety_funcs.h
	$(CC) $(CFLAGS) -c safety_funcs.c

# Overseer rules (assuming overseer.c exists)
overseer: overseer.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

overseer.o: overseer.c
	$(CC) -c $< $(CFLAGS)	

# simulator rules (assuming overseer.c exists)
simulator: simulator.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

simulator.o: simulator.c 
	$(CC) -c $< $(CFLAGS)

# Cardreader rules
cardreader: cardreader.o safety_funcs.o
	$(CC) -o $@ $^ $(LDFLAGS)

cardreader.o: cardreader.c safety_funcs.h
	$(CC) -c $< $(CFLAGS)

# Tempsensor rules (assuming tempsensor.c exists)
tempsensor: tempsensor.o safety_funcs.o
	$(CC) -o $@ $^ $(LDFLAGS)

tempsensor.o: tempsensor.c safety_funcs.h
	$(CC) -c $< $(CFLAGS)

# SAFETY CRITICAL COMPONENTS
# Door rules (assuming door.c exists)
door: door.o safety_funcs.o
	$(CC) -o $@ $^ $(LDFLAGS)

door.o: door.c safety_funcs.h
	$(CC) -c $< $(CFLAGS_SECURE)

# Callpoint rules (assuming callpoint.c exists)
callpoint: callpoint.o safety_funcs.o
	$(CC) -o $@ $^ $(LDFLAGS)

callpoint.o: callpoint.c safety_funcs.h
	$(CC) -c $< $(CFLAGS_SECURE)

# Firealarm rules (assuming firealarm.c exists)
firealarm: firealarm.o safety_funcs.o
	$(CC) -o $@ $^ $(LDFLAGS)

firealarm.o: firealarm.c safety_funcs.h
	$(CC) -c $< $(CFLAGS_SECURE)

clean:
	rm -f $(ALL_COMPONENTS) *.o
