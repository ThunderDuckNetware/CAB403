CC = gcc
CFLAGS = -Wall
LDFLAGS = -lrt -pthread

# All components you want to compile with just `make`
ALL_COMPONENTS = cardreader door callpoint firealarm overseer simulator

all: $(ALL_COMPONENTS)

# Cardreader rules
cardreader: cardreader.o
	$(CC) -o $@ $^ $(LDFLAGS)

cardreader.o: cardreader.c
	$(CC) -c $< $(CFLAGS)

# Door rules (assuming door.c exists)
door: door.o
	$(CC) -o $@ $^ $(LDFLAGS)

door.o: door.c
	$(CC) -c $< $(CFLAGS)

# Callpoint rules (assuming callpoint.c exists)
callpoint: callpoint.o
	$(CC) -o $@ $^ $(LDFLAGS)

callpoint.o: callpoint.c
	$(CC) -c $< $(CFLAGS)

# Firealarm rules (assuming firealarm.c exists)
firealarm: firealarm.o
	$(CC) -o $@ $^ $(LDFLAGS)

firealarm.o: firealarm.c
	$(CC) -c $< $(CFLAGS)

# Overseer rules (assuming overseer.c exists)
overseer: overseer.o
	$(CC) -o $@ $^ $(LDFLAGS)

overseer.o: overseer.c
	$(CC) -c $< $(CFLAGS)

# Overseer rules (assuming overseer.c exists)
simulator: simulator.o
	$(CC) -o $@ $^ $(LDFLAGS)

simulator.o: simulator.c
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f $(ALL_COMPONENTS) *.o
