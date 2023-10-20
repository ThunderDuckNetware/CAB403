# Cardreader
- Not sure how to handle the connection failing. Currently that just exits out of the prog

# Door
- Not sure whether to listen on multiple addresses or just the one
- Remove close secure code
- what is the unspecified address/port

# Callpoint
- add error checking for all functions
- can you infinite loop for security critical?
- need to justify safety criticalness

# Fire alarm unit
- not sending data to overseer properly?
- issue with sending packet stuck on loop for overseer
- need safety critical

# General
- need to do cleanup on all nodes (closing sockets and shms)
- remove all extra headers that aren't necessary