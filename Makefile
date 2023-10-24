CC = gcc
CFLAGS = -Wall
LDFLAGS = -lrt -pthread

# All components you want to compile with just `make`
ALL_COMPONENTS = cardreader door callpoint firealarm simulator overseer

all: $(ALL_COMPONENTS)
# helper_func rules (assuming helper_func.c exists)

helper_func.o: helper_func.c helper_func.h
	$(CC) $(CFLAGS) -c helper_func.c

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
cardreader: cardreader.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

cardreader.o: cardreader.c helper_func.h
	$(CC) -c $< $(CFLAGS)

# Door rules (assuming door.c exists)
door: door.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

door.o: door.c helper_func.h
	$(CC) -c $< $(CFLAGS)

# Callpoint rules (assuming callpoint.c exists)
callpoint: callpoint.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

callpoint.o: callpoint.c helper_func.h
	$(CC) -c $< $(CFLAGS)

# Firealarm rules (assuming firealarm.c exists)
firealarm: firealarm.o helper_func.o
	$(CC) -o $@ $^ $(LDFLAGS)

firealarm.o: firealarm.c helper_func.h
	$(CC) -c $< $(CFLAGS)

# Tempsensor rules (assuming tempsensor.c exists)
tempsensor: tempsensor.o
	$(CC) -o $@ $^ $(LDFLAGS)

tempsensor.o: tempsensor.c
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f $(ALL_COMPONENTS) *.o
