cardreader_1_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Cardreader sim (#0) started
[00.249](1) SIMULATOR: Cardreader sim (#3) started
[00.249](2) SIMULATOR: Cardreader sim (#1) started
[00.249](3) SIMULATOR: Door sim (#0) started
[00.249](4) SIMULATOR: Cardreader sim (#2) started
[00.249](5) SIMULATOR: Door sim (#1) started
[00.251](1) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.251](1) OVERSEER: Got reg event from cardreader 102
[00.251](1) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.251](1) OVERSEER: Got reg event from cardreader 101
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4000
[00.252](0) DOOR.101: Binding addr 127.0.0.1:4001
[00.252](2) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4001 FAIL_SAFE#
[00.252](2) OVERSEER: Registered door #101 @127.0.0.1:4001 (FAIL_SAFE#)
[00.252](1) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.252](1) OVERSEER: Got reg event from cardreader 103
[00.252](3) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.252](3) OVERSEER: Got reg event from cardreader 104
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4000
[00.253](0) DOOR.102: Binding addr 127.0.0.1:4002
[00.253](3) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4002 FAIL_SECURE#
[00.253](3) OVERSEER: Registered door #102 @127.0.0.1:4002 (FAIL_SECURE#)
[01.299](6) SIMULATOR: Simulated input to overseer: DOOR LIST
101 127.0.0.1:4001 FAIL_SAFE
102 127.0.0.1:4002 FAIL_SECURE
[01.349](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 102
[01.349](0) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.349](0) DOOR.102: Received message: OPEN#
[01.349](0) DOOR.102: Current status: C
[01.349](0) DOOR.102: OPENING#
[01.349](5) SIMULATOR: Door sim (#1) woke up. Status = o
[01.349](3) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.349](3) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.349](0) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.349](0) DOOR.101: Received message: OPEN#
[01.349](0) DOOR.101: Current status: C
[01.349](0) DOOR.101: OPENING#
[01.349](3) OVERSEER: Received OPENING# from door
[01.349](3) SIMULATOR: Door sim (#0) woke up. Status = o
[01.359](5) SIMULATOR: Door sim (#1) changed status to = O
[01.359](0) DOOR.102: OPENED#
[01.360](3) SIMULATOR: Door sim (#0) changed status to = O
[01.360](0) DOOR.101: OPENED#
[01.360](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.449](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 102
[01.449](0) DOOR.102: Received message: CLOSE#
[01.449](0) DOOR.102: Current status: O
[01.449](0) DOOR.102: CLOSING#
[01.449](5) SIMULATOR: Door sim (#1) woke up. Status = c
[01.459](5) SIMULATOR: Door sim (#1) changed status to = C
[01.459](0) DOOR.102: CLOSED#
[01.460](0) DOOR.101: Received message: CLOSE#
[01.460](0) DOOR.101: Current status: O
[01.460](0) DOOR.101: CLOSING#
[01.460](3) OVERSEER: Received CLOSING# from door
[01.460](3) SIMULATOR: Door sim (#0) woke up. Status = c
[01.470](3) SIMULATOR: Door sim (#0) changed status to = C
[01.470](0) DOOR.101: CLOSED#
[01.470](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.549](0) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](3) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[01.549](3) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[01.549](0) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](0) DOOR.101: Received message: OPEN#
[01.549](0) DOOR.101: Current status: C
[01.549](0) DOOR.101: OPENING#
[01.549](3) OVERSEER: Received OPENING# from door
[01.549](3) SIMULATOR: Door sim (#0) woke up. Status = o
[01.559](3) SIMULATOR: Door sim (#0) changed status to = O
[01.559](0) DOOR.101: OPENED#
[01.559](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.569](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.569](0) DOOR.101: Received message: CLOSE#
[01.569](0) DOOR.101: Current status: O
[01.569](0) DOOR.101: CLOSING#
[01.569](3) SIMULATOR: Door sim (#0) woke up. Status = c
[01.579](3) SIMULATOR: Door sim (#0) changed status to = C
[01.579](0) DOOR.101: CLOSED#
[01.660](0) DOOR.101: Received message: CLOSE#
[01.660](0) DOOR.101: Current status: C
[01.660](0) DOOR.101: ALREADY#
[01.660](3) OVERSEER: Received ALREADY# from door
[01.749](4) SIMULATOR: Cardreader sim (#2): scanned code db4ed0a0bfbb00ac
[01.749](3) OVERSEER: Received message from client: CARDREADER 103 SCANNED db4ed0a0bfbb00ac#
[01.749](3) OVERSEER: Got scan from cardreader 103: db4ed0a0bfbb00ac
[01.749](4) SIMULATOR: Cardreader sim (#2): response to scan: N
[01.949](4) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[01.949](3) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.949](3) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.949](4) SIMULATOR: Cardreader sim (#2): response to scan: Y
[01.949](0) DOOR.102: Received message: OPEN#
[01.949](0) DOOR.102: Current status: C
[01.949](0) DOOR.102: OPENING#
[01.949](3) OVERSEER: Received OPENING# from door
[01.949](5) SIMULATOR: Door sim (#1) woke up. Status = o
[01.959](5) SIMULATOR: Door sim (#1) changed status to = O
[01.959](0) DOOR.102: OPENED#
[01.959](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.049](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 101
[02.049](0) DOOR.101: Received message: OPEN#
[02.049](0) DOOR.101: Current status: C
[02.049](0) DOOR.101: OPENING#
[02.049](3) SIMULATOR: Door sim (#0) woke up. Status = o
[02.059](3) SIMULATOR: Door sim (#0) changed status to = O
[02.059](0) DOOR.101: OPENED#
[02.060](0) DOOR.102: Received message: CLOSE#
[02.060](0) DOOR.102: Current status: O
[02.060](0) DOOR.102: CLOSING#
[02.060](3) OVERSEER: Received CLOSING# from door
[02.060](5) SIMULATOR: Door sim (#1) woke up. Status = c
[02.070](5) SIMULATOR: Door sim (#1) changed status to = C
[02.070](0) DOOR.102: CLOSED#
[02.070](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.149](1) SIMULATOR: Cardreader sim (#3): scanned code 2214a7ba5943d923
[02.149](3) OVERSEER: Received message from client: CARDREADER 104 SCANNED 2214a7ba5943d923#
[02.149](3) OVERSEER: Got scan from cardreader 104: 2214a7ba5943d923
[02.149](1) SIMULATOR: Cardreader sim (#3): response to scan: Y
[02.149](0) DOOR.102: Received message: OPEN#
[02.149](0) DOOR.102: Current status: C
[02.149](0) DOOR.102: OPENING#
[02.149](3) OVERSEER: Received OPENING# from door
[02.149](5) SIMULATOR: Door sim (#1) woke up. Status = o
[02.159](5) SIMULATOR: Door sim (#1) changed status to = O
[02.159](0) DOOR.102: OPENED#
[02.160](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.260](0) DOOR.102: Received message: CLOSE#
[02.260](0) DOOR.102: Current status: O
[02.260](0) DOOR.102: CLOSING#
[02.260](5) SIMULATOR: Door sim (#1) woke up. Status = c
[02.260](3) OVERSEER: Received CLOSING# from door
[02.270](5) SIMULATOR: Door sim (#1) changed status to = C
[02.270](0) DOOR.102: CLOSED#
[02.270](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.149](6) SIMULATOR: Simulation ended, shutting down
"""

cardreader_2_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.250](0) SIMULATOR: Door sim (#3) started
[00.250](1) SIMULATOR: Door sim (#1) started
[00.250](2) SIMULATOR: Door sim (#4) started
[00.250](3) SIMULATOR: Cardreader sim (#8) started
[00.251](4) SIMULATOR: Door sim (#0) started
[00.250](5) SIMULATOR: Cardreader sim (#9) started
[00.250](6) SIMULATOR: Door sim (#2) started
[00.250](7) SIMULATOR: Cardreader sim (#5) started
[00.250](8) SIMULATOR: Cardreader sim (#7) started
[00.250](9) SIMULATOR: Destselect sim (#0) started
[00.251](10) SIMULATOR: Cardreader sim (#2) started
[00.250](11) SIMULATOR: Elevator sim (#0) started
[00.251](12) SIMULATOR: Cardreader sim (#3) started
[00.251](13) SIMULATOR: Cardreader sim (#4) started
[00.251](1) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.250](14) SIMULATOR: Cardreader sim (#0) started
[00.251](1) OVERSEER: Got reg event from cardreader 101
[00.251](10) SIMULATOR: Destselect sim (#3) started
[00.251](15) SIMULATOR: Destselect sim (#5) started
[00.251](8) SIMULATOR: Destselect sim (#4) started
[00.251](16) SIMULATOR: Destselect sim (#1) started
[00.251](17) SIMULATOR: Cardreader sim (#1) started
[00.250](18) SIMULATOR: Elevator sim (#1) started
[00.250](19) SIMULATOR: Cardreader sim (#6) started
[00.251](20) SIMULATOR: Camera sim (#0) started
[00.251](21) SIMULATOR: Destselect sim (#6) started
[00.251](22) SIMULATOR: Camera sim (#4) started
[00.251](8) SIMULATOR: Camera sim (#3) started
[00.251](15) SIMULATOR: Camera sim (#2) started
[00.251](12) SIMULATOR: Destselect sim (#2) started
[00.251](10) SIMULATOR: Camera sim (#1) started
[00.253](1) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.253](1) OVERSEER: Got reg event from cardreader 102
[00.255](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4100
[00.255](0) DOOR.101: Binding addr 127.0.0.1:4101
[00.256](0) DOOR.301: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7024. Overseer addr: 127.0.0.1:4100
[00.256](0) DOOR.501: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 7168. Overseer addr: 127.0.0.1:4100
[00.256](0) DOOR.301: Binding addr 127.0.0.1:4104
[00.257](0) CAMERA.22: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 15136. Overseer addr: 127.0.0.1:4100
[00.257](0) CAMERA.22: Binding addr 127.0.0.1:4109
[00.257](0) ELEVATOR.2: Starting up. Wait time: 10000us. Door open duration: 200000us. Shm path: /shm. Offset: 53296. Overseer addr: 127.0.0.1:4100
[00.257](0) ELEVATOR.2: Binding addr 127.0.0.1:4107
[00.258](0) DOOR.501: Binding addr 127.0.0.1:4105
[00.258](0) CAMERA.33: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 16960. Overseer addr: 127.0.0.1:4100
[00.258](0) CAMERA.33: Binding addr 127.0.0.1:4110
[00.258](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4100
[00.258](0) DOOR.102: Binding addr 127.0.0.1:4102
[00.258](0) CAMERA.44: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 18784. Overseer addr: 127.0.0.1:4100
[00.258](0) CAMERA.44: Binding addr 127.0.0.1:4111
[00.258](0) ELEVATOR.1: Starting up. Wait time: 10000us. Door open duration: 200000us. Shm path: /shm. Offset: 53152. Overseer addr: 127.0.0.1:4100
[00.258](0) ELEVATOR.1: Binding addr 127.0.0.1:4106
[00.258](2) OVERSEER: Received message from client: ELEVATOR 1 127.0.0.1:4106 HELLO#
[00.259](2) OVERSEER: Registered elevator #1 @127.0.0.1:4106
[00.260](3) OVERSEER: Received message from client: DOOR 301 127.0.0.1:4104 FAIL_SAFE#
[00.260](3) OVERSEER: Registered door #301 @127.0.0.1:4104 (FAIL_SAFE#)
[00.260](0) DOOR.201: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6880. Overseer addr: 127.0.0.1:4100
[00.260](4) OVERSEER: Received message from client: CARDREADER 501 HELLO#
[00.260](4) OVERSEER: Got reg event from cardreader 501
[00.260](0) DOOR.201: Binding addr 127.0.0.1:4103
[00.260](3) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.260](3) OVERSEER: Got reg event from cardreader 104
[00.260](0) DESTSELECT.202: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50128. Overseer addr: 127.0.0.1:4100
[00.260](0) DESTSELECT.302: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50464. Overseer addr: 127.0.0.1:4100
[00.260](0) DESTSELECT.202: Attempting to connect to 127.0.0.1:4100
[00.260](0) DESTSELECT.302: Attempting to connect to 127.0.0.1:4100
[00.260](5) OVERSEER: Received message from client: CAMERA 44 127.0.0.1:4111 HELLO#
[00.260](5) OVERSEER: Registered camera #44 @127.0.0.1:4111
[00.260](0) DESTSELECT.202: Sending HELLO#
[00.260](0) DESTSELECT.302: Sending HELLO#
[00.260](6) OVERSEER: Received message from client: CAMERA 33 127.0.0.1:4110 HELLO#
[00.260](6) OVERSEER: Registered camera #33 @127.0.0.1:4110
[00.260](4) OVERSEER: Received message from client: DESTSELECT 202 HELLO#
[00.260](4) OVERSEER: Got reg event from destselect 202
[00.260](7) OVERSEER: Received message from client: CARDREADER 202 HELLO#
[00.260](7) OVERSEER: Got reg event from cardreader 202
[00.260](5) OVERSEER: Received message from client: DESTSELECT 302 HELLO#
[00.260](5) OVERSEER: Got reg event from destselect 302
[00.260](8) OVERSEER: Received message from client: CARDREADER 301 HELLO#
[00.260](8) OVERSEER: Got reg event from cardreader 301
[00.261](0) DESTSELECT.201: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 49960. Overseer addr: 127.0.0.1:4100
[00.261](0) DESTSELECT.201: Attempting to connect to 127.0.0.1:4100
[00.261](0) DESTSELECT.201: Sending HELLO#
[00.261](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4101 FAIL_SAFE#
[00.261](1) OVERSEER: Registered door #101 @127.0.0.1:4101 (FAIL_SAFE#)
[00.261](3) OVERSEER: Received message from client: DOOR 201 127.0.0.1:4103 FAIL_SAFE#
[00.261](3) OVERSEER: Registered door #201 @127.0.0.1:4103 (FAIL_SAFE#)
[00.261](9) OVERSEER: Received message from client: CARDREADER 502 HELLO#
[00.261](9) OVERSEER: Got reg event from cardreader 502
[00.261](10) OVERSEER: Received message from client: CAMERA 22 127.0.0.1:4109 HELLO#
[00.261](10) OVERSEER: Registered camera #22 @127.0.0.1:4109
[00.261](5) OVERSEER: Received message from client: CARDREADER 302 HELLO#
[00.261](5) OVERSEER: Got reg event from cardreader 302
[00.261](8) OVERSEER: Received message from client: DESTSELECT 201 HELLO#
[00.261](8) OVERSEER: Got reg event from destselect 201
[00.261](11) OVERSEER: Received message from client: ELEVATOR 2 127.0.0.1:4107 HELLO#
[00.261](11) OVERSEER: Registered elevator #2 @127.0.0.1:4107
[00.261](9) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.261](9) OVERSEER: Got reg event from cardreader 103
[00.261](0) DESTSELECT.502: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50800. Overseer addr: 127.0.0.1:4100
[00.261](0) DESTSELECT.502: Attempting to connect to 127.0.0.1:4100
[00.261](12) OVERSEER: Received message from client: DOOR 501 127.0.0.1:4105 FAIL_SECURE#
[00.261](12) OVERSEER: Registered door #501 @127.0.0.1:4105 (FAIL_SECURE#)
[00.261](0) DESTSELECT.502: Sending HELLO#
[00.261](13) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4102 FAIL_SECURE#
[00.261](13) OVERSEER: Registered door #102 @127.0.0.1:4102 (FAIL_SECURE#)
[00.262](12) OVERSEER: Received message from client: DESTSELECT 502 HELLO#
[00.262](12) OVERSEER: Got reg event from destselect 502
[00.262](0) DESTSELECT.402: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50632. Overseer addr: 127.0.0.1:4100
[00.263](0) DESTSELECT.402: Attempting to connect to 127.0.0.1:4100
[00.263](0) DESTSELECT.402: Sending HELLO#
[00.263](12) OVERSEER: Received message from client: DESTSELECT 402 HELLO#
[00.263](12) OVERSEER: Got reg event from destselect 402
[00.263](0) CAMERA.11: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 13312. Overseer addr: 127.0.0.1:4100
[00.264](0) CAMERA.11: Binding addr 127.0.0.1:4108
[00.264](0) DESTSELECT.301: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50296. Overseer addr: 127.0.0.1:4100
[00.264](0) DESTSELECT.301: Attempting to connect to 127.0.0.1:4100
[00.264](0) DESTSELECT.301: Sending HELLO#
[00.264](12) OVERSEER: Received message from client: CAMERA 11 127.0.0.1:4108 HELLO#
[00.264](12) OVERSEER: Registered camera #11 @127.0.0.1:4108
[00.264](13) OVERSEER: Received message from client: DESTSELECT 301 HELLO#
[00.264](13) OVERSEER: Got reg event from destselect 301
[00.265](0) DESTSELECT.101: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 49792. Overseer addr: 127.0.0.1:4100
[00.265](0) DESTSELECT.101: Attempting to connect to 127.0.0.1:4100
[00.265](0) DESTSELECT.101: Sending HELLO#
[00.265](13) OVERSEER: Received message from client: DESTSELECT 101 HELLO#
[00.265](13) OVERSEER: Got reg event from destselect 101
[00.266](13) OVERSEER: Received message from client: CARDREADER 201 HELLO#
[00.266](13) OVERSEER: Got reg event from cardreader 201
[00.267](0) CAMERA.55: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 20608. Overseer addr: 127.0.0.1:4100
[00.267](0) CAMERA.55: Binding addr 127.0.0.1:4112
[00.267](13) OVERSEER: Received message from client: CAMERA 55 127.0.0.1:4112 HELLO#
[00.267](13) OVERSEER: Registered camera #55 @127.0.0.1:4112
[01.350](14) SIMULATOR: Cardreader sim (#0): scanned code 4b6f9c1d4d55506c
[01.350](13) OVERSEER: Received message from client: CARDREADER 101 SCANNED 4b6f9c1d4d55506c#
[01.350](13) OVERSEER: Got scan from cardreader 101: 4b6f9c1d4d55506c
[01.350](14) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.350](0) DOOR.101: Received message: OPEN#
[01.350](0) DOOR.101: Current status: C
[01.350](0) DOOR.101: OPENING#
[01.350](4) SIMULATOR: Door sim (#0) woke up. Status = o
[01.350](13) OVERSEER: Received OPENING# from door
[01.360](4) SIMULATOR: Door sim (#0) changed status to = O
[01.360](0) DOOR.101: OPENED#
[01.360](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.440](9) SIMULATOR: Destselect sim (#0): scanned code 4b6f9c1d4d55506c and floor 2
[01.440](0) DESTSELECT.101: Scanned code: 4b6f9c1d4d55506c and floor: 2 - connecting to overseer
[01.440](12) OVERSEER: Received message from client: DESTSELECT 101 SCANNED 4b6f9c1d4d55506c 2#
[01.440](12) OVERSEER: Got scan from destselect 101: 4b6f9c1d4d55506c, floor 2
[01.446](0) ELEVATOR.1: Received message: FROM 1 TO 2#
[01.450](0) DESTSELECT.101: Received response: ALLOWED#
[01.450](9) SIMULATOR: Destselect sim (#0): response to scan: Y
[01.460](0) DOOR.101: Received message: CLOSE#
[01.460](0) DOOR.101: Current status: O
[01.460](0) DOOR.101: CLOSING#
[01.460](13) OVERSEER: Received CLOSING# from door
[01.460](4) SIMULATOR: Door sim (#0) woke up. Status = c
[01.466](11) SIMULATOR: Elevator sim (#0): Status is now O
[01.470](4) SIMULATOR: Door sim (#0) changed status to = C
[01.470](0) DOOR.101: CLOSED#
[01.471](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.786](11) SIMULATOR: Elevator sim (#0) moved from floor 1 to 2. Status is now C
[01.806](11) SIMULATOR: Elevator sim (#0): Status is now O
[01.870](10) SIMULATOR: Camera sim (#1) simulated motion (angle: 330, status: O)
[01.870](13) OVERSEER: Received message from client: CAMERA 22 MOTION#
[01.870](13) OVERSEER: Received motion event from camera #22
[01.890](13) SIMULATOR: Cardreader sim (#4): scanned code 4b6f9c1d4d55506c
[01.890](13) OVERSEER: Received message from client: CARDREADER 201 SCANNED 4b6f9c1d4d55506c#
[01.890](13) OVERSEER: Got scan from cardreader 201: 4b6f9c1d4d55506c
[01.890](13) SIMULATOR: Cardreader sim (#4): response to scan: Y
[01.890](0) DOOR.201: Received message: OPEN#
[01.890](0) DOOR.201: Current status: C
[01.890](0) DOOR.201: OPENING#
[01.890](13) OVERSEER: Received OPENING# from door
[01.890](6) SIMULATOR: Door sim (#2) woke up. Status = o
[01.900](6) SIMULATOR: Door sim (#2) changed status to = O
[01.900](0) DOOR.201: OPENED#
[01.900](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.910](15) SIMULATOR: Camera sim (#2) simulated motion (angle: 135, status: O)
[01.911](12) OVERSEER: Received message from client: CAMERA 33 MOTION#
[01.911](12) OVERSEER: Received motion event from camera #33
[01.940](12) SIMULATOR: Destselect sim (#2): scanned code 4b6f9c1d4d55506c and floor 5
[01.940](0) DESTSELECT.202: Scanned code: 4b6f9c1d4d55506c and floor: 5 - connecting to overseer
[01.940](12) OVERSEER: Received message from client: DESTSELECT 202 SCANNED 4b6f9c1d4d55506c 5#
[01.940](12) OVERSEER: Got scan from destselect 202: 4b6f9c1d4d55506c, floor 5
[01.948](0) ELEVATOR.2: Received message: FROM 2 TO 5#
[01.950](0) DESTSELECT.202: Received response: ALLOWED#
[01.950](12) SIMULATOR: Destselect sim (#2): response to scan: Y
[01.968](18) SIMULATOR: Elevator sim (#1): Status is now O
[02.000](0) DOOR.201: Received message: CLOSE#
[02.000](0) DOOR.201: Current status: O
[02.000](0) DOOR.201: CLOSING#
[02.000](13) OVERSEER: Received CLOSING# from door
[02.000](6) SIMULATOR: Door sim (#2) woke up. Status = c
[02.010](6) SIMULATOR: Door sim (#2) changed status to = C
[02.010](0) DOOR.201: CLOSED#
[02.010](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.288](18) SIMULATOR: Elevator sim (#1) moved from floor 2 to 3. Status is now C
[02.388](18) SIMULATOR: Elevator sim (#1) moved from floor 3 to 4
[02.488](18) SIMULATOR: Elevator sim (#1) moved from floor 4 to 5
[02.508](18) SIMULATOR: Elevator sim (#1): Status is now O
[02.740](3) SIMULATOR: Cardreader sim (#8): scanned code 4b6f9c1d4d55506c
[02.740](13) OVERSEER: Received message from client: CARDREADER 501 SCANNED 4b6f9c1d4d55506c#
[02.740](13) OVERSEER: Got scan from cardreader 501: 4b6f9c1d4d55506c
[02.740](3) SIMULATOR: Cardreader sim (#8): response to scan: Y
[02.740](0) DOOR.501: Received message: OPEN#
[02.740](0) DOOR.501: Current status: C
[02.740](0) DOOR.501: OPENING#
[02.740](13) OVERSEER: Received OPENING# from door
[02.740](2) SIMULATOR: Door sim (#4) woke up. Status = o
[02.750](2) SIMULATOR: Door sim (#4) changed status to = O
[02.750](0) DOOR.501: OPENED#
[02.750](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.770](22) SIMULATOR: Camera sim (#4) simulated motion (angle: 105, status: O)
[02.770](12) OVERSEER: Received message from client: CAMERA 55 MOTION#
[02.770](12) OVERSEER: Received motion event from camera #55
[02.850](0) DOOR.501: Received message: CLOSE#
[02.850](0) DOOR.501: Current status: O
[02.850](0) DOOR.501: CLOSING#
[02.850](13) OVERSEER: Received CLOSING# from door
[02.850](2) SIMULATOR: Door sim (#4) woke up. Status = c
[02.861](2) SIMULATOR: Door sim (#4) changed status to = C
[02.861](0) DOOR.501: CLOSED#
[02.861](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.950](5) SIMULATOR: Cardreader sim (#9): scanned code 4b6f9c1d4d55506c
[02.950](13) OVERSEER: Received message from client: CARDREADER 502 SCANNED 4b6f9c1d4d55506c#
[02.950](13) OVERSEER: Got scan from cardreader 502: 4b6f9c1d4d55506c
[02.950](5) SIMULATOR: Cardreader sim (#9): response to scan: Y
[02.950](0) DOOR.501: Received message: OPEN#
[02.950](0) DOOR.501: Current status: C
[02.950](0) DOOR.501: OPENING#
[02.950](13) OVERSEER: Received OPENING# from door
[02.950](2) SIMULATOR: Door sim (#4) woke up. Status = o
[02.960](2) SIMULATOR: Door sim (#4) changed status to = O
[02.960](0) DOOR.501: OPENED#
[02.960](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[03.050](21) SIMULATOR: Destselect sim (#6): scanned code 4b6f9c1d4d55506c and floor 2
[03.050](0) DESTSELECT.502: Scanned code: 4b6f9c1d4d55506c and floor: 2 - connecting to overseer
[03.050](12) OVERSEER: Received message from client: DESTSELECT 502 SCANNED 4b6f9c1d4d55506c 2#
[03.050](12) OVERSEER: Got scan from destselect 502: 4b6f9c1d4d55506c, floor 2
[03.052](0) ELEVATOR.2: Received message: FROM 5 TO 2#
[03.060](0) DESTSELECT.502: Received response: ALLOWED#
[03.060](21) SIMULATOR: Destselect sim (#6): response to scan: Y
[03.060](0) DOOR.501: Received message: CLOSE#
[03.060](0) DOOR.501: Current status: O
[03.060](0) DOOR.501: CLOSING#
[03.060](13) OVERSEER: Received CLOSING# from door
[03.060](2) SIMULATOR: Door sim (#4) woke up. Status = c
[03.070](2) SIMULATOR: Door sim (#4) changed status to = C
[03.070](0) DOOR.501: CLOSED#
[03.071](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.272](18) SIMULATOR: Elevator sim (#1): Status is now C
[03.292](18) SIMULATOR: Elevator sim (#1): Status is now O
[03.612](18) SIMULATOR: Elevator sim (#1) moved from floor 5 to 4. Status is now C
[03.712](18) SIMULATOR: Elevator sim (#1) moved from floor 4 to 3
[03.750](15) SIMULATOR: Camera sim (#2) simulated motion (angle: 135, status: O)
[03.751](13) OVERSEER: Received message from client: CAMERA 33 MOTION#
[03.751](13) OVERSEER: Received motion event from camera #33
[03.813](18) SIMULATOR: Elevator sim (#1) moved from floor 3 to 2
[03.833](18) SIMULATOR: Elevator sim (#1): Status is now O
[03.850](7) SIMULATOR: Cardreader sim (#5): scanned code 4b6f9c1d4d55506c
[03.850](13) OVERSEER: Received message from client: CARDREADER 202 SCANNED 4b6f9c1d4d55506c#
[03.850](13) OVERSEER: Got scan from cardreader 202: 4b6f9c1d4d55506c
[03.850](7) SIMULATOR: Cardreader sim (#5): response to scan: Y
[03.850](0) DOOR.201: Received message: OPEN#
[03.850](0) DOOR.201: Current status: C
[03.850](0) DOOR.201: OPENING#
[03.850](13) OVERSEER: Received OPENING# from door
[03.850](6) SIMULATOR: Door sim (#2) woke up. Status = o
[03.860](6) SIMULATOR: Door sim (#2) changed status to = O
[03.860](0) DOOR.201: OPENED#
[03.860](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[03.950](10) SIMULATOR: Camera sim (#1) simulated motion (angle: 330, status: O)
[03.950](12) OVERSEER: Received message from client: CAMERA 22 MOTION#
[03.950](12) OVERSEER: Received motion event from camera #22
[03.960](0) DOOR.201: Received message: CLOSE#
[03.960](0) DOOR.201: Current status: O
[03.960](0) DOOR.201: CLOSING#
[03.960](13) OVERSEER: Received CLOSING# from door
[03.960](6) SIMULATOR: Door sim (#2) woke up. Status = c
[03.970](6) SIMULATOR: Door sim (#2) changed status to = C
[03.970](0) DOOR.201: CLOSED#
[03.970](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[04.050](16) SIMULATOR: Destselect sim (#1): scanned code 4b6f9c1d4d55506c and floor 1
[04.050](0) DESTSELECT.201: Scanned code: 4b6f9c1d4d55506c and floor: 1 - connecting to overseer
[04.050](13) OVERSEER: Received message from client: DESTSELECT 201 SCANNED 4b6f9c1d4d55506c 1#
[04.050](13) OVERSEER: Got scan from destselect 201: 4b6f9c1d4d55506c, floor 1
[04.051](0) ELEVATOR.1: Received message: FROM 2 TO 1#
[04.060](0) DESTSELECT.201: Received response: ALLOWED#
[04.060](16) SIMULATOR: Destselect sim (#1): response to scan: Y
[04.271](11) SIMULATOR: Elevator sim (#0): Status is now C
[04.291](11) SIMULATOR: Elevator sim (#0): Status is now O
[04.611](11) SIMULATOR: Elevator sim (#0) moved from floor 2 to 1. Status is now C
[04.631](11) SIMULATOR: Elevator sim (#0): Status is now O
[04.750](17) SIMULATOR: Cardreader sim (#1): scanned code 4b6f9c1d4d55506c
[04.750](13) OVERSEER: Received message from client: CARDREADER 102 SCANNED 4b6f9c1d4d55506c#
[04.750](13) OVERSEER: Got scan from cardreader 102: 4b6f9c1d4d55506c
[04.750](17) SIMULATOR: Cardreader sim (#1): response to scan: Y
[04.750](0) DOOR.101: Received message: OPEN#
[04.750](0) DOOR.101: Current status: C
[04.750](0) DOOR.101: OPENING#
[04.750](13) OVERSEER: Received OPENING# from door
[04.750](4) SIMULATOR: Door sim (#0) woke up. Status = o
[04.760](4) SIMULATOR: Door sim (#0) changed status to = O
[04.760](0) DOOR.101: OPENED#
[04.760](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[04.850](22) SIMULATOR: Camera sim (#4) simulated motion (angle: 105, status: O)
[04.850](12) OVERSEER: Received message from client: CAMERA 55 MOTION#
[04.850](12) OVERSEER: Received motion event from camera #55
[04.850](12) OVERSEER: Alert in sector 9
Security alarm triggered!
[04.850](23) SIMULATOR: Security alarm has been triggered.
[04.850](0) DOOR.501: Received message: CLOSE_SECURE#
[04.850](0) DOOR.501: Current status: C
[04.850](0) DOOR.501: CLOSING# (security)
[04.850](0) DOOR.102: Received message: CLOSE_SECURE#
[04.850](2) SIMULATOR: Door sim (#4) woke up. Status = c
[04.850](0) DOOR.102: Current status: C
[04.850](0) DOOR.102: CLOSING# (security)
[04.850](1) SIMULATOR: Door sim (#1) woke up. Status = c
[04.860](0) DOOR.101: Received message: CLOSE#
[04.860](0) DOOR.101: Current status: O
[04.860](0) DOOR.101: CLOSING#
[04.860](13) OVERSEER: Received CLOSING# from door
[04.860](4) SIMULATOR: Door sim (#0) woke up. Status = c
[04.860](2) SIMULATOR: Door sim (#4) changed status to = C
[04.860](0) DOOR.501: CLOSED# (security)
[04.860](1) SIMULATOR: Door sim (#1) changed status to = C
[04.860](0) DOOR.102: CLOSED# (security)
[04.870](4) SIMULATOR: Door sim (#0) changed status to = C
[04.870](0) DOOR.101: CLOSED#
[04.870](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[05.850](24) SIMULATOR: Simulation ended, shutting down
"""

cardreader_3_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 10000us Datagram resend delay: 2500us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.249](0) SIMULATOR: Launching tempsensor
[00.249](0) SIMULATOR: Launching tempsensor
[00.249](0) SIMULATOR: Launching tempsensor
[00.249](0) SIMULATOR: Launching tempsensor
[00.249](0) SIMULATOR: Launching tempsensor
[00.250](1) SIMULATOR: Cardreader sim (#5) started
[00.250](2) SIMULATOR: Cardreader sim (#6) started
[00.251](3) SIMULATOR: Cardreader sim (#7) started
[00.251](4) SIMULATOR: Camera sim (#4) started
[00.251](5) SIMULATOR: Tempsensor sim (#4) started
[00.251](6) SIMULATOR: Tempsensor sim (#3) started
[00.251](7) SIMULATOR: Tempsensor sim (#2) started
[00.251](8) SIMULATOR: Tempsensor sim (#0) started
[00.251](9) SIMULATOR: Door sim (#0) started
[00.251](10) SIMULATOR: Cardreader sim (#0) started
[00.251](11) SIMULATOR: Cardreader sim (#2) started
[00.251](12) SIMULATOR: Cardreader sim (#1) started
[00.251](13) SIMULATOR: Destselect sim (#6) started
[00.252](14) SIMULATOR: Camera sim (#3) started
[00.252](15) SIMULATOR: Camera sim (#1) started
[00.252](16) SIMULATOR: Camera sim (#2) started
[00.251](17) SIMULATOR: Camera sim (#0) started
[00.252](18) SIMULATOR: Tempsensor sim (#1) started
[00.252](19) SIMULATOR: Door sim (#1) started
[00.252](20) SIMULATOR: Door sim (#3) started
[00.252](21) SIMULATOR: Door sim (#4) started
[00.252](22) SIMULATOR: Elevator sim (#0) started
[00.252](23) SIMULATOR: Elevator sim (#1) started
[00.252](24) SIMULATOR: Destselect sim (#0) started
[00.252](25) SIMULATOR: Destselect sim (#1) started
[00.252](26) SIMULATOR: Destselect sim (#2) started
[00.252](27) SIMULATOR: Cardreader sim (#3) started
[00.252](28) SIMULATOR: Cardreader sim (#8) started
[00.252](29) SIMULATOR: Door sim (#2) started
[00.252](30) SIMULATOR: Cardreader sim (#4) started
[00.252](31) SIMULATOR: Destselect sim (#4) started
[00.252](32) SIMULATOR: Destselect sim (#5) started
[00.252](33) SIMULATOR: Destselect sim (#3) started
[00.252](1) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.252](34) SIMULATOR: Cardreader sim (#9) started
[00.252](1) OVERSEER: Got reg event from cardreader 102
[00.252](2) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.252](2) OVERSEER: Got reg event from cardreader 103
[00.252](3) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.252](3) OVERSEER: Got reg event from cardreader 101
[00.253](0) DOOR.102: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4200
[00.253](0) DOOR.102: Binding addr 127.0.0.1:4203
[00.253](3) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4203 FAIL_SAFE#
[00.253](3) OVERSEER: Registered door #102 @127.0.0.1:4203 (FAIL_SAFE#)
[00.259](0) ELEVATOR.1: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53152. Overseer addr: 127.0.0.1:4200
[00.259](0) TEMPSENSOR.101: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9472.
[00.259](0) TEMPSENSOR.101: Receiver #1: 127.0.0.1:4200
[00.259](0) TEMPSENSOR.101: Receiver #2: 127.0.0.1:4209
[00.259](0) TEMPSENSOR.101: Binding addr 127.0.0.1:4207
[00.259](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.259](0) ELEVATOR.1: Binding addr 127.0.0.1:4212
[00.259](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.259](0) ELEVATOR.2: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53296. Overseer addr: 127.0.0.1:4200
[00.259](0) ELEVATOR.2: Binding addr 127.0.0.1:4213
[00.260](0) DESTSELECT.402: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50632. Overseer addr: 127.0.0.1:4200
[00.260](0) DESTSELECT.402: Attempting to connect to 127.0.0.1:4200
[00.260](0) DESTSELECT.402: Sending HELLO#
[00.260](0) DESTSELECT.302: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50464. Overseer addr: 127.0.0.1:4200
[00.260](0) DESTSELECT.302: Attempting to connect to 127.0.0.1:4200
[00.260](0) DESTSELECT.302: Sending HELLO#
[00.261](0) DESTSELECT.502: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50800. Overseer addr: 127.0.0.1:4200
[00.261](0) DESTSELECT.502: Attempting to connect to 127.0.0.1:4200
[00.261](0) DESTSELECT.502: Sending HELLO#
[00.261](0) DESTSELECT.201: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49960. Overseer addr: 127.0.0.1:4200
[00.261](0) DESTSELECT.201: Attempting to connect to 127.0.0.1:4200
[00.261](0) DESTSELECT.201: Sending HELLO#
[00.262](0) DESTSELECT.202: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50296. Overseer addr: 127.0.0.1:4200
[00.262](0) DESTSELECT.202: Attempting to connect to 127.0.0.1:4200
[00.262](0) DESTSELECT.202: Sending HELLO#
[00.263](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4200
[00.263](0) DOOR.101: Binding addr 127.0.0.1:4202
[00.264](0) CAMERA.55: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 20608. Overseer addr: 127.0.0.1:4200
[00.264](0) DOOR.501: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7168. Overseer addr: 127.0.0.1:4200
[00.264](0) CAMERA.55: Binding addr 127.0.0.1:4218
[00.264](0) DOOR.501: Binding addr 127.0.0.1:4206
[00.264](0) CAMERA.11: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 13312. Overseer addr: 127.0.0.1:4200
[00.264](0) CAMERA.11: Binding addr 127.0.0.1:4214
[00.265](3) OVERSEER: Received message from client: CARDREADER 302 HELLO#
[00.265](3) OVERSEER: Got reg event from cardreader 302
[00.265](1) OVERSEER: Received message from client: ELEVATOR 1 127.0.0.1:4212 HELLO#
[00.265](1) OVERSEER: Registered elevator #1 @127.0.0.1:4212
[00.265](5) OVERSEER: Received message from client: DESTSELECT 402 HELLO#
[00.265](5) OVERSEER: Got reg event from destselect 402
[00.265](6) OVERSEER: Received message from client: DESTSELECT 502 HELLO#
[00.265](6) OVERSEER: Got reg event from destselect 502
[00.265](0) DOOR.201: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6880. Overseer addr: 127.0.0.1:4200
[00.265](7) OVERSEER: Received message from client: DESTSELECT 201 HELLO#
[00.265](7) OVERSEER: Got reg event from destselect 201
[00.265](0) DOOR.201: Binding addr 127.0.0.1:4204
[00.265](8) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4202 FAIL_SAFE#
[00.265](8) OVERSEER: Registered door #101 @127.0.0.1:4202 (FAIL_SAFE#)
[00.265](9) OVERSEER: Received message from client: CARDREADER 201 HELLO#
[00.265](9) OVERSEER: Got reg event from cardreader 201
[00.265](10) OVERSEER: Received message from client: DOOR 501 127.0.0.1:4206 FAIL_SAFE#
[00.265](10) OVERSEER: Registered door #501 @127.0.0.1:4206 (FAIL_SAFE#)
[00.265](11) OVERSEER: Received message from client: CAMERA 55 127.0.0.1:4218 HELLO#
[00.265](11) OVERSEER: Registered camera #55 @127.0.0.1:4218
[00.265](12) OVERSEER: Received message from client: DESTSELECT 302 HELLO#
[00.265](12) OVERSEER: Got reg event from destselect 302
[00.265](0) CAMERA.33: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 16960. Overseer addr: 127.0.0.1:4200
[00.265](13) OVERSEER: Received message from client: ELEVATOR 2 127.0.0.1:4213 HELLO#
[00.265](13) OVERSEER: Registered elevator #2 @127.0.0.1:4213
[00.265](0) CAMERA.33: Binding addr 127.0.0.1:4216
[00.265](14) OVERSEER: Received message from client: CARDREADER 501 HELLO#
[00.265](14) OVERSEER: Got reg event from cardreader 501
[00.266](15) OVERSEER: Received message from client: DESTSELECT 202 HELLO#
[00.266](15) OVERSEER: Got reg event from destselect 202
[00.266](0) TEMPSENSOR.103: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9664.
[00.266](0) TEMPSENSOR.103: Receiver #1: 127.0.0.1:4208
[00.266](0) TEMPSENSOR.103: Binding addr 127.0.0.1:4209
[00.266](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.267](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 10. Detection period: 100000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4200
[00.267](0) FIREALARM: Binding addr 127.0.0.1:4201
[00.267](0) DESTSELECT.101: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49792. Overseer addr: 127.0.0.1:4200
[00.267](0) DESTSELECT.101: Attempting to connect to 127.0.0.1:4200
[00.267](0) DESTSELECT.101: Sending HELLO#
[00.267](0) DESTSELECT.301: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50128. Overseer addr: 127.0.0.1:4200
[00.267](0) DESTSELECT.301: Attempting to connect to 127.0.0.1:4200
[00.267](0) DESTSELECT.301: Sending HELLO#
[00.267](0) TEMPSENSOR.105: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9856.
[00.267](0) TEMPSENSOR.105: Receiver #1: 127.0.0.1:4209
[00.267](0) TEMPSENSOR.105: Receiver #2: 127.0.0.1:4201
[00.267](0) TEMPSENSOR.105: Binding addr 127.0.0.1:4211
[00.267](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.267](0) FIREALARM: Received temperature (22.00)
[00.269](0) TEMPSENSOR.102: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9568.
[00.269](0) TEMPSENSOR.102: Receiver #1: 127.0.0.1:4210
[00.269](0) TEMPSENSOR.102: Binding addr 127.0.0.1:4208
[00.269](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.269](0) TEMPSENSOR.104: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9760.
[00.269](0) TEMPSENSOR.104: Receiver #1: 127.0.0.1:4207
[00.269](0) TEMPSENSOR.104: Binding addr 127.0.0.1:4210
[00.269](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.269](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.269](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.269](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.269](0) DOOR.301: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7024. Overseer addr: 127.0.0.1:4200
[00.269](0) DOOR.301: Binding addr 127.0.0.1:4205
[00.269](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.270](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.270](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.270](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.270](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.270](0) CAMERA.44: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 18784. Overseer addr: 127.0.0.1:4200
[00.270](0) CAMERA.44: Binding addr 127.0.0.1:4217
[00.270](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.270](11) OVERSEER: Received message from client: CARDREADER 202 HELLO#
[00.270](11) OVERSEER: Got reg event from cardreader 202
[00.270](0) CAMERA.22: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 15136. Overseer addr: 127.0.0.1:4200
[00.270](0) CAMERA.22: Binding addr 127.0.0.1:4215
[00.270](1) OVERSEER: Received message from client: CARDREADER 502 HELLO#
[00.270](1) OVERSEER: Got reg event from cardreader 502
[00.270](16) OVERSEER: Received message from client: CAMERA 44 127.0.0.1:4217 HELLO#
[00.270](16) OVERSEER: Registered camera #44 @127.0.0.1:4217
[00.270](8) OVERSEER: Received message from client: DESTSELECT 301 HELLO#
[00.271](8) OVERSEER: Got reg event from destselect 301
[00.270](5) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4201 HELLO#
[00.271](5) OVERSEER: Registered fire alarm @127.0.0.1:4201
[00.271](9) OVERSEER: Sending packet to 127.0.0.1:4206
[00.271](2) OVERSEER: Sending packet to 127.0.0.1:4203
[00.271](0) FIREALARM: Got door registration packet
[00.271](14) OVERSEER: Received message from client: CAMERA 11 127.0.0.1:4214 HELLO#
[00.270](6) OVERSEER: Received message from client: DESTSELECT 101 HELLO#
[00.271](0) FIREALARM: Got door registration packet
[00.271](13) OVERSEER: Received message from client: DOOR 201 127.0.0.1:4204 FAIL_SAFE#
[00.271](3) OVERSEER: Received message from client: CAMERA 33 127.0.0.1:4216 HELLO#
[00.271](3) OVERSEER: Registered camera #33 @127.0.0.1:4216
[00.271](13) OVERSEER: Registered door #201 @127.0.0.1:4204 (FAIL_SAFE#)
[00.271](6) OVERSEER: Got reg event from destselect 101
[00.270](12) OVERSEER: Received message from client: CARDREADER 301 HELLO#
[00.271](7) OVERSEER: Sending packet to 127.0.0.1:4202
[00.271](8) OVERSEER: Sending packet to 127.0.0.1:4204
[00.271](15) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.271](0) FIREALARM: Got door registration packet
[00.271](14) OVERSEER: Registered camera #11 @127.0.0.1:4214
[00.271](0) FIREALARM: Got door registration packet
[00.271](10) OVERSEER: Received message from client: DOOR 301 127.0.0.1:4205 FAIL_SAFE#
[00.271](10) OVERSEER: Registered door #301 @127.0.0.1:4205 (FAIL_SAFE#)
[00.271](17) OVERSEER: Received message from client: CAMERA 22 127.0.0.1:4215 HELLO#
[00.271](17) OVERSEER: Registered camera #22 @127.0.0.1:4215
[00.271](15) OVERSEER: Got reg event from cardreader 104
[00.271](13) OVERSEER: Sending packet to 127.0.0.1:4205
[00.271](0) FIREALARM: Got door registration packet
[00.271](12) OVERSEER: Got reg event from cardreader 301
[00.309](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.309](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.309](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.310](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.317](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.317](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.317](0) FIREALARM: Received temperature (22.00)
[00.318](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.318](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.319](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.319](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.319](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.319](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.319](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.319](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.319](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.319](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.320](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.320](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.320](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.321](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.321](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.321](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.321](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.322](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.322](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.360](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.360](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.361](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.361](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.367](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.368](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.368](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.368](0) FIREALARM: Received temperature (22.00)
[00.369](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.369](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.369](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.369](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.370](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.370](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.370](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.370](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.370](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.370](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.370](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.371](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.371](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.371](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.371](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.372](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.372](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.372](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.411](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.411](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.412](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.412](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.418](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.419](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.419](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.419](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.419](0) FIREALARM: Received temperature (22.00)
[00.420](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.420](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.420](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.420](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.421](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.421](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.421](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.421](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.421](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.421](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.421](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.422](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.422](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.422](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.422](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.423](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.423](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.461](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.461](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.462](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.462](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.469](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.470](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.470](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.470](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.470](0) FIREALARM: Received temperature (22.00)
[00.471](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.471](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.471](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.471](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.472](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.472](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.472](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.472](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.472](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.472](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.472](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.473](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.473](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.473](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.473](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.474](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.474](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.511](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.511](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.512](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.512](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.519](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.520](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.520](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.521](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.521](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.521](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.521](0) FIREALARM: Received temperature (22.00)
[00.522](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.522](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.522](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.522](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.522](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.522](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.522](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.523](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.523](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.523](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.523](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.523](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.523](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.524](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.524](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.562](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.562](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.562](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.562](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.570](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.571](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.571](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.571](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.571](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.572](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.572](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.572](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.572](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.572](0) FIREALARM: Received temperature (22.00)
[00.573](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.573](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.573](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.573](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.574](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.574](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.574](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.574](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.574](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.574](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.575](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.575](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.613](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.613](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.613](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.614](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.620](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.621](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.621](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.622](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.622](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.622](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.623](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.623](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.623](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.623](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.623](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.623](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.623](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.623](0) FIREALARM: Received temperature (22.00)
[00.624](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.624](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.624](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.624](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.625](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.626](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.627](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.627](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.663](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.663](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.664](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.665](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.671](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.672](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.672](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.672](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.673](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.673](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.673](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.674](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.674](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.674](0) FIREALARM: Received temperature (22.00)
[00.674](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.674](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.674](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.675](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.675](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.676](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.676](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.676](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.676](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.677](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.678](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.678](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.713](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.713](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.714](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.715](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.721](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.722](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.722](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.723](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.723](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.723](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.724](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.724](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.724](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.724](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.725](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.725](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.725](0) FIREALARM: Received temperature (22.00)
[00.726](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.726](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.726](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.726](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.727](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.727](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.728](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.729](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.729](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.763](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.763](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.764](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.765](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.772](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.773](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.773](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.774](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.774](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.774](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.774](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.774](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.775](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.775](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.775](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.775](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.775](0) FIREALARM: Received temperature (22.00)
[00.775](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.776](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.776](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.776](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.777](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.777](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.778](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.778](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.778](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.814](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.814](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.815](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.816](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.822](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.823](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.823](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.824](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.824](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.824](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.825](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.825](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.825](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.825](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.826](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.826](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.826](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.826](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.826](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.826](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.826](0) FIREALARM: Received temperature (22.00)
[00.828](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.828](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.829](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.829](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.829](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.864](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.864](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.865](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.866](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.873](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.874](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.874](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.875](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.875](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.875](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.876](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.876](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.876](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.876](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.876](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.876](0) FIREALARM: Received temperature (22.00)
[00.877](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.877](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.877](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.877](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.877](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.878](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.878](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.879](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.879](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.879](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.914](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.914](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.915](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.916](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.923](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.924](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.924](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.925](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.925](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.925](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.926](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.926](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.926](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.927](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.927](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.927](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.927](0) FIREALARM: Received temperature (22.00)
[00.928](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.928](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.928](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.928](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.928](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.928](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.929](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.929](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.929](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.964](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.964](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.965](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.966](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.973](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.974](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.974](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.975](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.975](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.975](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.976](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.976](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.976](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.977](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.977](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.978](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.978](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.978](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.978](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.978](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.978](0) FIREALARM: Received temperature (22.00)
[00.980](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.981](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.981](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.981](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.981](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.014](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.014](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.015](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.016](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.024](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.025](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.025](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.026](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.026](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.026](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.027](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.027](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.027](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.028](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.028](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.028](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.029](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.029](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.029](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.029](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.029](0) FIREALARM: Received temperature (22.00)
[01.031](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.032](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.032](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.032](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.032](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.064](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.064](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.065](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.066](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.075](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.076](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.076](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.077](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.077](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.077](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.078](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.078](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.078](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.078](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.078](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.079](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.079](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.079](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.079](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.079](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.079](0) FIREALARM: Received temperature (22.00)
[01.081](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.082](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.082](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.082](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.082](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.115](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.115](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.116](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.117](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.126](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.127](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.127](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.128](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.128](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.128](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.129](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.129](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.129](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.129](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.129](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.129](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.130](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.130](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.130](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.130](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.130](0) FIREALARM: Received temperature (22.00)
[01.132](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.133](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.133](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.134](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.134](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.166](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.166](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.167](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.167](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.176](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.177](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.178](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.178](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.179](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.179](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.179](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.180](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.180](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.180](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.180](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.181](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.181](0) FIREALARM: Received temperature (22.00)
[01.181](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.181](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.181](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.181](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.182](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.182](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.183](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.183](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.183](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.216](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.216](4) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.217](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.218](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.227](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.227](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.228](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.228](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.228](4) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.229](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.230](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.230](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.230](4) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.230](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.231](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.231](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.231](0) FIREALARM: Received temperature (22.00)
[01.232](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.232](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.232](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.232](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.232](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.232](4) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.233](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.233](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.233](4) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.255](10) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.255](13) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.255](13) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.255](10) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.255](0) DOOR.101: Received message: OPEN#
[01.255](0) DOOR.101: Current status: C
[01.255](0) DOOR.101: OPENING#
[01.255](9) SIMULATOR: Door sim (#0) woke up. Status = o
[01.255](13) OVERSEER: Received OPENING# from door
[01.257](9) SIMULATOR: Door sim (#0) changed status to = O
[01.257](0) DOOR.1[...(truncated)...]
[02.192](15) SIMULATOR: Camera sim (#1) simulated motion (angle: 0, status: O)
[02.192](0) TEMPSENSOR.101: Propagating update (103:28.83) to 127.0.0.1:4200
[02.192](4) OVERSEER: Received UDP TEMP packet: id=103 temp=28.83
[02.193](5) OVERSEER: Received message from client: CAMERA 22 MOTION#
[02.193](5) OVERSEER: Received motion event from camera #22
[02.196](22) SIMULATOR: Elevator sim (#0): Status is now C
[02.196](7) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.196](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.197](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.197](22) SIMULATOR: Elevator sim (#0): Status is now O
[02.198](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.199](5) SIMULATOR: Tempsensor sim (#4): temperature changed to 30.00
[02.199](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.199](0) FIREALARM: Received temperature (30.00)
[02.199](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.199](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.200](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.200](0) DOOR.201: Received message: CLOSE#
[02.200](0) DOOR.201: Current status: O
[02.200](0) DOOR.201: CLOSING#
[02.200](29) SIMULATOR: Door sim (#2) woke up. Status = c
[02.200](3) OVERSEER: Received CLOSING# from door
[02.200](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.201](30) SIMULATOR: Cardreader sim (#4): scanned code db4ed0a0bfbb00ac
[02.201](29) SIMULATOR: Door sim (#2) changed status to = C
[02.201](0) DOOR.201: CLOSED#
[02.201](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.201](5) OVERSEER: Received message from client: CARDREADER 201 SCANNED db4ed0a0bfbb00ac#
[02.201](5) OVERSEER: Got scan from cardreader 201: db4ed0a0bfbb00ac
[02.201](30) SIMULATOR: Cardreader sim (#4): response to scan: Y
[02.201](0) DOOR.201: Received message: OPEN#
[02.201](0) DOOR.201: Current status: C
[02.201](0) DOOR.201: OPENING#
[02.201](29) SIMULATOR: Door sim (#2) woke up. Status = o
[02.201](5) OVERSEER: Received OPENING# from door
[02.201](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.202](29) SIMULATOR: Door sim (#2) changed status to = O
[02.202](0) DOOR.201: OPENED#
[02.202](16) SIMULATOR: Camera sim (#2) simulated motion (angle: 0, status: O)
[02.202](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.202](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.202](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.203](0) TEMPSENSOR.102: Temperature is 27.66 - sending update
[02.203](3) OVERSEER: Received message from client: CAMERA 33 MOTION#
[02.203](3) OVERSEER: Received motion event from camera #33
[02.203](0) TEMPSENSOR.104: Propagating update (102:27.66) to 127.0.0.1:4207
[02.205](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4200
[02.205](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4209
[02.205](4) OVERSEER: Received UDP TEMP packet: id=102 temp=27.66
[02.208](33) SIMULATOR: Destselect sim (#3): scanned code db4ed0a0bfbb00ac and floor 3
[02.208](0) DESTSELECT.202: Scanned code: db4ed0a0bfbb00ac and floor: 3 - connecting to overseer
[02.208](3) OVERSEER: Received message from client: DESTSELECT 202 SCANNED db4ed0a0bfbb00ac 3#
[02.208](3) OVERSEER: Got scan from destselect 202: db4ed0a0bfbb00ac, floor 3
[02.209](18) SIMULATOR: Tempsensor sim (#1): temperature changed to 28.13
[02.209](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.209](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.210](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.210](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.210](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.210](0) ELEVATOR.2: Received message: FROM 2 TO 3#
[02.210](0) DESTSELECT.202: Received response: ALLOWED#
[02.210](33) SIMULATOR: Destselect sim (#3): response to scan: Y
[02.211](22) SIMULATOR: Elevator sim (#0) moved from floor 3 to 2. Status is now C
[02.212](34) SIMULATOR: Cardreader sim (#9): scanned code 4b6f9c1d4d55506c
[02.212](3) OVERSEER: Received message from client: CARDREADER 502 SCANNED 4b6f9c1d4d55506c#
[02.212](3) OVERSEER: Got scan from cardreader 502: 4b6f9c1d4d55506c
[02.212](34) SIMULATOR: Cardreader sim (#9): response to scan: Y
[02.212](0) DOOR.501: Received message: OPEN#
[02.212](0) DOOR.501: Current status: C
[02.212](0) DOOR.501: OPENING#
[02.212](21) SIMULATOR: Door sim (#4) woke up. Status = o
[02.212](3) OVERSEER: Received OPENING# from door
[02.213](0) DOOR.201: Received message: CLOSE#
[02.213](0) DOOR.201: Current status: O
[02.213](0) DOOR.201: CLOSING#
[02.213](29) SIMULATOR: Door sim (#2) woke up. Status = c
[02.213](5) OVERSEER: Received CLOSING# from door
[02.213](21) SIMULATOR: Door sim (#4) changed status to = O
[02.213](0) DOOR.501: OPENED#
[02.214](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.214](22) SIMULATOR: Elevator sim (#0) moved from floor 2 to 1
[02.214](29) SIMULATOR: Door sim (#2) changed status to = C
[02.214](0) DOOR.201: CLOSED#
[02.214](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.215](22) SIMULATOR: Elevator sim (#0): Status is now O
[02.220](8) SIMULATOR: Tempsensor sim (#0): temperature changed to 26.77
[02.220](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.220](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.220](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.221](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.221](23) SIMULATOR: Elevator sim (#1): Status is now C
[02.222](7) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.222](23) SIMULATOR: Elevator sim (#1): Status is now O
[02.223](10) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[02.223](5) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[02.223](5) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[02.223](10) SIMULATOR: Cardreader sim (#0): response to scan: Y
[02.223](0) DOOR.101: Received message: OPEN#
[02.223](0) DOOR.101: Current status: C
[02.223](0) DOOR.101: OPENING#
[02.223](9) SIMULATOR: Door sim (#0) woke up. Status = o
[02.223](5) OVERSEER: Received OPENING# from door
[02.224](0) DOOR.501: Received message: CLOSE#
[02.224](0) DOOR.501: Current status: O
[02.224](0) DOOR.501: CLOSING#
[02.224](21) SIMULATOR: Door sim (#4) woke up. Status = c
[02.224](3) OVERSEER: Received CLOSING# from door
[02.224](24) SIMULATOR: Destselect sim (#0): scanned code cae0efe252087308 and floor 3
[02.224](0) DESTSELECT.101: Scanned code: cae0efe252087308 and floor: 3 - connecting to overseer
[02.224](13) OVERSEER: Received message from client: DESTSELECT 101 SCANNED cae0efe252087308 3#
[02.224](13) OVERSEER: Got scan from destselect 101: cae0efe252087308, floor 3
[02.225](28) SIMULATOR: Cardreader sim (#8): scanned code 4b6f9c1d4d55506c
[02.225](9) SIMULATOR: Door sim (#0) changed status to = O
[02.225](0) DOOR.101: OPENED#
[02.225](13) OVERSEER: Received message from client: CARDREADER 501 SCANNED 4b6f9c1d4d55506c#
[02.225](13) OVERSEER: Got scan from cardreader 501: 4b6f9c1d4d55506c
[02.225](28) SIMULATOR: Cardreader sim (#8): response to scan: Y
[02.225](21) SIMULATOR: Door sim (#4) changed status to = C
[02.225](0) DOOR.501: CLOSED#
[02.225](0) DOOR.501: Received message: OPEN#
[02.225](0) DOOR.501: Current status: C
[02.225](0) DOOR.501: OPENING#
[02.225](21) SIMULATOR: Door sim (#4) woke up. Status = o
[02.225](13) OVERSEER: Received OPENING# from door
[02.225](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.225](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.225](0) ELEVATOR.1: Received message: FROM 1 TO 3#
[02.226](21) SIMULATOR: Door sim (#4) changed status to = O
[02.226](0) DOOR.501: OPENED#
[02.226](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.227](0) DESTSELECT.101: Received response: ALLOWED#
[02.227](24) SIMULATOR: Destselect sim (#0): response to scan: Y
[02.229](14) SIMULATOR: Camera sim (#3) simulated motion (angle: 0, status: O)
[02.230](3) OVERSEER: Received message from client: CAMERA 44 MOTION#
[02.230](3) OVERSEER: Received motion event from camera #44
[02.234](11) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[02.234](3) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[02.234](3) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[02.234](11) SIMULATOR: Cardreader sim (#2): response to scan: Y
[02.234](0) DOOR.102: Received message: OPEN#
[02.234](0) DOOR.102: Current status: C
[02.234](0) DOOR.102: OPENING#
[02.234](19) SIMULATOR: Door sim (#1) woke up. Status = o
[02.234](3) OVERSEER: Received OPENING# from door
[02.235](0) DOOR.101: Received message: CLOSE#
[02.235](0) DOOR.101: Current status: O
[02.235](0) DOOR.101: CLOSING#
[02.235](9) SIMULATOR: Door sim (#0) woke up. Status = c
[02.235](5) OVERSEER: Received CLOSING# from door
[02.235](19) SIMULATOR: Door sim (#1) changed status to = O
[02.235](0) DOOR.102: OPENED#
[02.235](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.236](23) SIMULATOR: Elevator sim (#1) moved from floor 2 to 3. Status is now C
[02.236](0) DOOR.501: Received message: CLOSE#
[02.236](0) DOOR.501: Current status: O
[02.236](0) DOOR.501: CLOSING#
[02.236](22) SIMULATOR: Elevator sim (#0): Status is now C
[02.236](21) SIMULATOR: Door sim (#4) woke up. Status = c
[02.236](9) SIMULATOR: Door sim (#0) changed status to = C
[02.236](13) OVERSEER: Received CLOSING# from door
[02.236](0) DOOR.101: CLOSED#
[02.236](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.237](6) SIMULATOR: Tempsensor sim (#3): temperature changed to 27.03
[02.237](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.237](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.237](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.237](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.237](23) SIMULATOR: Elevator sim (#1): Status is now O
[02.237](21) SIMULATOR: Door sim (#4) changed status to = C
[02.237](22) SIMULATOR: Elevator sim (#0): Status is now O
[02.237](0) DOOR.501: CLOSED#
[02.237](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.238](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.244](2) SIMULATOR: Cardreader sim (#6): scanned code cae0efe252087308
[02.244](13) OVERSEER: Received message from client: CARDREADER 301 SCANNED cae0efe252087308#
[02.244](13) OVERSEER: Got scan from cardreader 301: cae0efe252087308
[02.244](2) SIMULATOR: Cardreader sim (#6): response to scan: Y
[02.244](0) DOOR.301: Received message: OPEN#
[02.244](0) DOOR.301: Current status: C
[02.244](0) DOOR.301: OPENING#
[02.244](13) OVERSEER: Received OPENING# from door
[02.244](20) SIMULATOR: Door sim (#3) woke up. Status = o
[02.245](0) DOOR.102: Received message: CLOSE#
[02.245](0) DOOR.102: Current status: O
[02.245](0) DOOR.102: CLOSING#
[02.245](3) OVERSEER: Received CLOSING# from door
[02.245](19) SIMULATOR: Door sim (#1) woke up. Status = c
[02.245](20) SIMULATOR: Door sim (#3) changed status to = O
[02.245](0) DOOR.301: OPENED#
[02.246](13) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.246](19) SIMULATOR: Door sim (#1) changed status to = C
[02.246](0) DOOR.102: CLOSED#
[02.247](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.247](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.248](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.249](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.249](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.249](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.250](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.250](0) FIREALARM: Received temperature (30.00)
[02.251](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.251](22) SIMULATOR: Elevator sim (#0) moved from floor 1 to 2. Status is now C
[02.251](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.252](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.252](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.252](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.254](22) SIMULATOR: Elevator sim (#0) moved from floor 2 to 3
[02.255](22) SIMULATOR: Elevator sim (#0): Status is now O
[02.256](0) DOOR.301: Received message: CLOSE#
[02.256](0) DOOR.301: Current status: O
[02.256](0) DOOR.301: CLOSING#
[02.256](13) OVERSEER: Received CLOSING# from door
[02.256](20) SIMULATOR: Door sim (#3) woke up. Status = c
[02.257](20) SIMULATOR: Door sim (#3) changed status to = C
[02.257](0) DOOR.301: CLOSED#
[02.257](13) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.260](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.260](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.260](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.260](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.260](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.270](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.270](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.271](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.272](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.288](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.288](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.288](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.288](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.289](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.297](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.298](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.299](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.299](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.299](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.301](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.301](0) FIREALARM: Received temperature (30.00)
[02.302](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.303](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.303](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.303](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.303](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.310](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.310](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.310](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.310](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.310](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.320](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.320](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.321](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.322](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.339](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.340](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.340](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.340](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.340](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.348](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.348](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.349](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.349](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.349](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.352](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.352](0) FIREALARM: Received temperature (30.00)
[02.353](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.354](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.354](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.354](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.354](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.360](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.360](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.361](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.361](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.361](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.370](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.370](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.371](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.372](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.390](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.391](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.391](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.391](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.391](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.398](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.399](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.400](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.400](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.400](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.403](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.403](0) FIREALARM: Received temperature (30.00)
[02.404](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.405](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.405](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.406](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.406](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.411](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.411](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.412](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.412](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.412](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.421](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.421](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.421](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.422](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.440](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.441](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.441](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.441](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.441](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.450](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.451](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.451](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.451](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.451](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.454](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.454](0) FIREALARM: Received temperature (30.00)
[02.455](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.456](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.456](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.457](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.457](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.461](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.462](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.463](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.463](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.463](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.471](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.471](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.471](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.472](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.491](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.492](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.492](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.492](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.493](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.500](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.502](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.503](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.504](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.504](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.505](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.505](0) FIREALARM: Received temperature (30.00)
[02.505](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.505](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.506](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.506](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.506](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.511](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.512](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.513](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.513](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.513](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.521](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.521](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.522](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.522](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.541](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.542](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.542](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.542](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.542](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.551](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.552](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.552](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.553](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.553](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.556](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.556](0) FIREALARM: Received temperature (30.00)
[02.556](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.557](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.557](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.558](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.558](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.561](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.561](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.562](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.562](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.562](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.571](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.571](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.571](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.572](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.591](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.592](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.592](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.592](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.592](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.601](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.602](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.602](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.603](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.603](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.607](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.607](0) FIREALARM: Received temperature (30.00)
[02.607](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.608](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.608](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.609](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.609](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.611](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.611](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.612](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.612](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.612](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.621](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.621](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.621](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.622](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.641](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.642](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.642](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.642](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.643](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.652](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.652](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.653](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.653](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.653](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.658](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.658](0) FIREALARM: Received temperature (30.00)
[02.658](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.658](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.659](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.659](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.659](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.662](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.663](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.663](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.663](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.663](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.671](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.671](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.672](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.672](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.692](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.692](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.692](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.692](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.693](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.703](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.703](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.704](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.704](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.704](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.709](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.709](0) FIREALARM: Received temperature (30.00)
[02.709](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.710](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.710](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.711](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.711](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.712](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.712](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.713](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.713](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.713](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.721](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.721](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.722](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.722](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.742](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.744](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.744](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.744](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.744](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.753](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.754](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.754](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.754](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.754](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.759](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.759](0) FIREALARM: Received temperature (30.00)
[02.759](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.760](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.761](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.761](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.761](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.762](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.763](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.763](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.763](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.763](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.771](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.771](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.772](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.773](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.793](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.794](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.794](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.794](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.794](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.804](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.805](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.805](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.805](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.805](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.809](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.810](0) FIREALARM: Received temperature (30.00)
[02.810](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.811](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.812](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.812](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.812](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.813](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.814](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.814](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.814](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.814](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.821](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.821](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.822](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.823](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.844](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.844](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.844](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.844](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.844](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.854](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.855](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.855](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.855](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.855](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.860](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.860](0) FIREALARM: Received temperature (30.00)
[02.860](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.861](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.862](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.862](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.862](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.863](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.864](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.864](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.864](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.864](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.871](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.871](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.872](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.873](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.894](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.894](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.894](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.894](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.894](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.904](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.905](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.905](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.906](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.906](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.910](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.910](0) FIREALARM: Received temperature (30.00)
[02.912](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.912](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.913](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.913](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.913](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.914](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.915](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.915](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.915](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.915](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.922](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.922](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.922](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.923](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.945](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.945](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.945](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.945](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.946](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.955](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.956](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.957](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.957](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.957](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.961](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.961](0) FIREALARM: Received temperature (30.00)
[02.961](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.962](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.963](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.963](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.963](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.965](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.966](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.966](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.966](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.966](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.972](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.972](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.972](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.973](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.995](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.995](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.995](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.995](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.996](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.005](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.006](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.007](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.007](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.007](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.011](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.012](0) FIREALARM: Received temperature (30.00)
[03.013](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.013](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.014](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.014](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.014](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.016](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.017](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.017](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.017](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.017](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.022](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.022](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.022](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.023](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.046](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.046](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.046](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.046](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.047](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.055](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.055](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.057](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.057](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.057](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.062](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.062](0) FIREALARM: Received temperature (30.00)
[03.063](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.063](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.063](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.063](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.063](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.067](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.068](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.069](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.069](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.069](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.072](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.072](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.072](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.073](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.096](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.096](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.096](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.096](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.097](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.106](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.107](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.107](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.107](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.107](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.112](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.112](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.113](0) FIREALARM: Received temperature (30.00)
[03.113](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.114](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.114](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.114](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.118](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.119](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.120](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.120](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.120](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.123](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.123](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.123](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.124](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.147](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.147](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.147](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.147](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.148](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.157](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.158](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.159](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.159](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.159](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.163](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.163](0) FIREALARM: Received temperature (30.00)
[03.164](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.164](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.164](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.164](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.164](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.168](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.168](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.169](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.169](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.169](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.173](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.173](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.173](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.174](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.197](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.197](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.197](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.197](4) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.198](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.207](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.208](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.209](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.209](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.209](4) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.214](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.214](0) FIREALARM: Received temperature (30.00)
[03.215](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.215](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.216](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.217](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.217](4) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.218](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.219](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.220](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.220](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.220](4) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.223](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.223](4) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.223](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.224](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.244](0) SIMULATOR: Simulation ended, shutting down
"""

cardreader_1_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Door sim (#0) started
[00.249](1) SIMULATOR: Cardreader sim (#0) started
[00.249](2) SIMULATOR: Cardreader sim (#1) started
[00.249](3) SIMULATOR: Cardreader sim (#2) started
[00.249](4) SIMULATOR: Cardreader sim (#3) started
[00.249](5) SIMULATOR: Door sim (#1) started
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4000
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4002
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4000
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4001
[00.251](1) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.251](1) OVERSEER: Got reg event from cardreader 103
[00.251](2) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.251](2) OVERSEER: Got reg event from cardreader 102
[00.251](3) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4001 FAIL_SAFE#
[00.251](4) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.251](4) OVERSEER: Got reg event from cardreader 104
[00.251](5) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4002 FAIL_SECURE#
[00.251](3) OVERSEER: Registered door #101 @127.0.0.1:4001 (FAIL_SAFE#)
[00.251](5) OVERSEER: Registered door #102 @127.0.0.1:4002 (FAIL_SECURE#)
[00.252](5) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.252](5) OVERSEER: Got reg event from cardreader 101
[01.299](6) SIMULATOR: Simulated input to overseer: DOOR LIST
101 127.0.0.1:4001 FAIL_SAFE
102 127.0.0.1:4002 FAIL_SECURE
[01.349](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 102
[01.349](1) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.349](0) DOOR.102: Received message: OPEN#
[01.349](0) DOOR.102: Current status: C
[01.349](0) DOOR.102: OPENING#
[01.349](5) SIMULATOR: Door sim (#1) woke up. Status = o
[01.349](5) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.349](5) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.349](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.349](0) DOOR.101: Received message: OPEN#
[01.349](0) DOOR.101: Current status: C
[01.349](0) DOOR.101: OPENING#
[01.349](5) OVERSEER: Received OPENING# from door
[01.349](0) SIMULATOR: Door sim (#0) woke up. Status = o
[01.359](5) SIMULATOR: Door sim (#1) changed status to = O
[01.359](0) DOOR.102: OPENED#
[01.359](0) SIMULATOR: Door sim (#0) changed status to = O
[01.359](0) DOOR.101: OPENED#
[01.359](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.449](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 102
[01.449](0) DOOR.102: Received message: CLOSE#
[01.449](0) DOOR.102: Current status: O
[01.449](0) DOOR.102: CLOSING#
[01.449](5) SIMULATOR: Door sim (#1) woke up. Status = c
[01.459](5) SIMULATOR: Door sim (#1) changed status to = C
[01.459](0) DOOR.102: CLOSED#
[01.459](0) DOOR.101: Received message: CLOSE#
[01.459](0) DOOR.101: Current status: O
[01.459](0) DOOR.101: CLOSING#
[01.459](5) OVERSEER: Received CLOSING# from door
[01.459](0) SIMULATOR: Door sim (#0) woke up. Status = c
[01.469](0) SIMULATOR: Door sim (#0) changed status to = C
[01.469](0) DOOR.101: CLOSED#
[01.469](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.549](1) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](5) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[01.549](5) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[01.549](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](0) DOOR.101: Received message: OPEN#
[01.549](0) DOOR.101: Current status: C
[01.549](0) DOOR.101: OPENING#
[01.549](5) OVERSEER: Received OPENING# from door
[01.549](0) SIMULATOR: Door sim (#0) woke up. Status = o
[01.559](0) SIMULATOR: Door sim (#0) changed status to = O
[01.559](0) DOOR.101: OPENED#
[01.559](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.569](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.569](0) DOOR.101: Received message: CLOSE#
[01.569](0) DOOR.101: Current status: O
[01.569](0) DOOR.101: CLOSING#
[01.569](0) SIMULATOR: Door sim (#0) woke up. Status = c
[01.579](0) SIMULATOR: Door sim (#0) changed status to = C
[01.579](0) DOOR.101: CLOSED#
[01.659](0) DOOR.101: Received message: CLOSE#
[01.659](0) DOOR.101: Current status: C
[01.659](0) DOOR.101: ALREADY#
[01.659](5) OVERSEER: Received ALREADY# from door
[01.749](3) SIMULATOR: Cardreader sim (#2): scanned code db4ed0a0bfbb00ac
[01.749](5) OVERSEER: Received message from client: CARDREADER 103 SCANNED db4ed0a0bfbb00ac#
[01.749](5) OVERSEER: Got scan from cardreader 103: db4ed0a0bfbb00ac
[01.749](3) SIMULATOR: Cardreader sim (#2): response to scan: N
[01.949](3) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[01.949](5) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.949](5) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.949](3) SIMULATOR: Cardreader sim (#2): response to scan: Y
[01.949](0) DOOR.102: Received message: OPEN#
[01.949](0) DOOR.102: Current status: C
[01.949](0) DOOR.102: OPENING#
[01.949](5) OVERSEER: Received OPENING# from door
[01.949](5) SIMULATOR: Door sim (#1) woke up. Status = o
[01.959](5) SIMULATOR: Door sim (#1) changed status to = O
[01.959](0) DOOR.102: OPENED#
[01.959](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.049](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 101
[02.049](0) DOOR.101: Received message: OPEN#
[02.049](0) DOOR.101: Current status: C
[02.049](0) DOOR.101: OPENING#
[02.049](0) SIMULATOR: Door sim (#0) woke up. Status = o
[02.059](0) SIMULATOR: Door sim (#0) changed status to = O
[02.059](0) DOOR.101: OPENED#
[02.059](0) DOOR.102: Received message: CLOSE#
[02.059](0) DOOR.102: Current status: O
[02.059](0) DOOR.102: CLOSING#
[02.059](5) SIMULATOR: Door sim (#1) woke up. Status = c
[02.059](5) OVERSEER: Received CLOSING# from door
[02.069](5) SIMULATOR: Door sim (#1) changed status to = C
[02.069](0) DOOR.102: CLOSED#
[02.069](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.149](4) SIMULATOR: Cardreader sim (#3): scanned code 2214a7ba5943d923
[02.149](5) OVERSEER: Received message from client: CARDREADER 104 SCANNED 2214a7ba5943d923#
[02.149](5) OVERSEER: Got scan from cardreader 104: 2214a7ba5943d923
[02.149](4) SIMULATOR: Cardreader sim (#3): response to scan: Y
[02.149](0) DOOR.102: Received message: OPEN#
[02.149](0) DOOR.102: Current status: C
[02.149](0) DOOR.102: OPENING#
[02.149](5) OVERSEER: Received OPENING# from door
[02.149](5) SIMULATOR: Door sim (#1) woke up. Status = o
[02.159](5) SIMULATOR: Door sim (#1) changed status to = O
[02.159](0) DOOR.102: OPENED#
[02.159](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.259](0) DOOR.102: Received message: CLOSE#
[02.259](0) DOOR.102: Current status: O
[02.259](0) DOOR.102: CLOSING#
[02.259](5) OVERSEER: Received CLOSING# from door
[02.259](5) SIMULATOR: Door sim (#1) woke up. Status = c
[02.269](5) SIMULATOR: Door sim (#1) changed status to = C
[02.269](0) DOOR.102: CLOSED#
[02.269](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.149](6) SIMULATOR: Simulation ended, shutting down
"""

cardreader_2_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.250](0) SIMULATOR: Door sim (#3) started
[00.250](1) SIMULATOR: Door sim (#4) started
[00.250](2) SIMULATOR: Door sim (#2) started
[00.250](3) SIMULATOR: Cardreader sim (#6) started
[00.250](4) SIMULATOR: Door sim (#0) started
[00.250](5) SIMULATOR: Cardreader sim (#5) started
[00.250](6) SIMULATOR: Cardreader sim (#0) started
[00.250](7) SIMULATOR: Cardreader sim (#7) started
[00.250](8) SIMULATOR: Cardreader sim (#1) started
[00.250](9) SIMULATOR: Cardreader sim (#4) started
[00.250](10) SIMULATOR: Door sim (#1) started
[00.250](11) SIMULATOR: Cardreader sim (#2) started
[00.251](3) SIMULATOR: Elevator sim (#1) started
[00.251](12) SIMULATOR: Destselect sim (#5) started
[00.251](13) SIMULATOR: Destselect sim (#3) started
[00.250](14) SIMULATOR: Cardreader sim (#3) started
[00.251](7) SIMULATOR: Elevator sim (#0) started
[00.251](15) SIMULATOR: Cardreader sim (#9) started
[00.251](16) SIMULATOR: Destselect sim (#2) started
[00.251](17) SIMULATOR: Destselect sim (#6) started
[00.251](18) SIMULATOR: Camera sim (#0) started
[00.251](19) SIMULATOR: Cardreader sim (#8) started
[00.251](20) SIMULATOR: Camera sim (#2) started
[00.251](21) SIMULATOR: Camera sim (#3) started
[00.251](22) SIMULATOR: Destselect sim (#0) started
[00.251](11) SIMULATOR: Destselect sim (#1) started
[00.251](13) SIMULATOR: Camera sim (#4) started
[00.251](23) SIMULATOR: Camera sim (#1) started
[00.251](24) SIMULATOR: Destselect sim (#4) started
[00.252](0) DOOR.201: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6880. Overseer addr: 127.0.0.1:4100
[00.252](0) DOOR.201: Binding addr 127.0.0.1:4103
[00.253](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4100
[00.253](0) DOOR.102: Binding addr 127.0.0.1:4102
[00.253](0) DOOR.501: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 7168. Overseer addr: 127.0.0.1:4100
[00.253](0) DOOR.501: Binding addr 127.0.0.1:4105
[00.253](1) OVERSEER: Received message from client: DOOR 201 127.0.0.1:4103 FAIL_SAFE#
[00.253](1) OVERSEER: Registered door #201 @127.0.0.1:4103 (FAIL_SAFE#)
[00.253](2) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4102 FAIL_SECURE#
[00.253](2) OVERSEER: Registered door #102 @127.0.0.1:4102 (FAIL_SECURE#)
[00.253](3) OVERSEER: Received message from client: DOOR 501 127.0.0.1:4105 FAIL_SECURE#
[00.253](3) OVERSEER: Registered door #501 @127.0.0.1:4105 (FAIL_SECURE#)
[00.253](1) OVERSEER: Received message from client: CARDREADER 201 HELLO#
[00.254](1) OVERSEER: Got reg event from cardreader 201
[00.253](0) DOOR.301: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7024. Overseer addr: 127.0.0.1:4100
[00.254](0) DOOR.301: Binding addr 127.0.0.1:4104
[00.254](1) OVERSEER: Received message from client: DOOR 301 127.0.0.1:4104 FAIL_SAFE#
[00.254](1) OVERSEER: Registered door #301 @127.0.0.1:4104 (FAIL_SAFE#)
[00.257](0) ELEVATOR.1: Starting up. Wait time: 10000us. Door open duration: 200000us. Shm path: /shm. Offset: 53152. Overseer addr: 127.0.0.1:4100
[00.257](0) CAMERA.44: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 18784. Overseer addr: 127.0.0.1:4100
[00.257](0) CAMERA.44: Binding addr 127.0.0.1:4111
[00.257](0) ELEVATOR.2: Starting up. Wait time: 10000us. Door open duration: 200000us. Shm path: /shm. Offset: 53296. Overseer addr: 127.0.0.1:4100
[00.258](0) ELEVATOR.2: Binding addr 127.0.0.1:4107
[00.258](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4100
[00.258](0) DOOR.101: Binding addr 127.0.0.1:4101
[00.258](0) CAMERA.11: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 13312. Overseer addr: 127.0.0.1:4100
[00.258](0) CAMERA.22: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 15136. Overseer addr: 127.0.0.1:4100
[00.258](0) CAMERA.11: Binding addr 127.0.0.1:4108
[00.258](0) CAMERA.22: Binding addr 127.0.0.1:4109
[00.259](0) DESTSELECT.302: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50464. Overseer addr: 127.0.0.1:4100
[00.259](0) DESTSELECT.302: Attempting to connect to 127.0.0.1:4100
[00.259](0) DESTSELECT.202: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50128. Overseer addr: 127.0.0.1:4100
[00.259](0) DESTSELECT.202: Attempting to connect to 127.0.0.1:4100
[00.259](0) DESTSELECT.202: Sending HELLO#
[00.259](4) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.259](4) OVERSEER: Got reg event from cardreader 102
[00.259](0) CAMERA.55: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 20608. Overseer addr: 127.0.0.1:4100
[00.259](0) CAMERA.55: Binding addr 127.0.0.1:4112
[00.259](0) DESTSELECT.402: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50632. Overseer addr: 127.0.0.1:4100
[00.259](0) DESTSELECT.402: Attempting to connect to 127.0.0.1:4100
[00.260](0) DESTSELECT.402: Sending HELLO#
[00.260](0) DESTSELECT.201: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 49960. Overseer addr: 127.0.0.1:4100
[00.260](0) DESTSELECT.201: Attempting to connect to 127.0.0.1:4100
[00.260](0) DESTSELECT.201: Sending HELLO#
[00.260](0) CAMERA.33: Starting up. Temperature threshold: 20.Shm path: /shm. Offset: 16960. Overseer addr: 127.0.0.1:4100
[00.260](0) CAMERA.33: Binding addr 127.0.0.1:4110
[00.260](2) OVERSEER: Received message from client: CAMERA 44 127.0.0.1:4111 HELLO#
[00.260](2) OVERSEER: Registered camera #44 @127.0.0.1:4111
[00.260](1) OVERSEER: Received message from client: CARDREADER 302 HELLO#
[00.260](1) OVERSEER: Got reg event from cardreader 302
[00.261](5) OVERSEER: Received message from client: ELEVATOR 2 127.0.0.1:4107 HELLO#
[00.261](5) OVERSEER: Registered elevator #2 @127.0.0.1:4107
[00.261](0) DESTSELECT.101: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 49792. Overseer addr: 127.0.0.1:4100
[00.261](0) DESTSELECT.101: Attempting to connect to 127.0.0.1:4100
[00.261](0) DESTSELECT.502: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50800. Overseer addr: 127.0.0.1:4100
[00.261](0) DESTSELECT.101: Sending HELLO#
[00.261](0) DESTSELECT.302: Sending HELLO#
[00.261](0) ELEVATOR.1: Binding addr 127.0.0.1:4106
[00.262](0) DESTSELECT.502: Attempting to connect to 127.0.0.1:4100
[00.262](0) DESTSELECT.502: Sending HELLO#
[00.262](5) OVERSEER: Received message from client: DESTSELECT 101 HELLO#
[00.262](5) OVERSEER: Got reg event from destselect 101
[00.262](6) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.262](6) OVERSEER: Got reg event from cardreader 101
[00.262](1) OVERSEER: Received message from client: DESTSELECT 302 HELLO#
[00.262](0) DESTSELECT.301: Starting up. Wait time: 10000us. Shm path: /shm. Offset: 50296. Overseer addr: 127.0.0.1:4100
[00.262](1) OVERSEER: Got reg event from destselect 302
[00.262](0) DESTSELECT.301: Attempting to connect to 127.0.0.1:4100
[00.262](0) DESTSELECT.301: Sending HELLO#
[00.262](7) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.262](7) OVERSEER: Got reg event from cardreader 104
[00.262](8) OVERSEER: Received message from client: ELEVATOR 1 127.0.0.1:4106 HELLO#
[00.262](8) OVERSEER: Registered elevator #1 @127.0.0.1:4106
[00.262](9) OVERSEER: Received message from client: DESTSELECT 502 HELLO#
[00.262](9) OVERSEER: Got reg event from destselect 502
[00.262](10) OVERSEER: Received message from client: CARDREADER 301 HELLO#
[00.262](10) OVERSEER: Got reg event from cardreader 301
[00.262](11) OVERSEER: Received message from client: CARDREADER 502 HELLO#
[00.262](11) OVERSEER: Got reg event from cardreader 502
[00.262](1) OVERSEER: Received message from client: DESTSELECT 301 HELLO#
[00.262](1) OVERSEER: Got reg event from destselect 301
[00.263](1) OVERSEER: Received message from client: CARDREADER 501 HELLO#
[00.263](1) OVERSEER: Got reg event from cardreader 501
[00.263](12) OVERSEER: Received message from client: CAMERA 22 127.0.0.1:4109 HELLO#
[00.263](4) OVERSEER: Received message from client: DESTSELECT 202 HELLO#
[00.263](12) OVERSEER: Registered camera #22 @127.0.0.1:4109
[00.263](13) OVERSEER: Received message from client: CAMERA 55 127.0.0.1:4112 HELLO#
[00.263](13) OVERSEER: Registered camera #55 @127.0.0.1:4112
[00.263](14) OVERSEER: Received message from client: CARDREADER 202 HELLO#
[00.263](14) OVERSEER: Got reg event from cardreader 202
[00.263](15) OVERSEER: Received message from client: DESTSELECT 402 HELLO#
[00.263](15) OVERSEER: Got reg event from destselect 402
[00.263](16) OVERSEER: Received message from client: CAMERA 11 127.0.0.1:4108 HELLO#
[00.263](16) OVERSEER: Registered camera #11 @127.0.0.1:4108
[00.263](4) OVERSEER: Got reg event from destselect 202
[00.263](17) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4101 FAIL_SAFE#
[00.263](17) OVERSEER: Registered door #101 @127.0.0.1:4101 (FAIL_SAFE#)
[00.263](2) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.263](2) OVERSEER: Got reg event from cardreader 103
[00.263](18) OVERSEER: Received message from client: CAMERA 33 127.0.0.1:4110 HELLO#
[00.263](18) OVERSEER: Registered camera #33 @127.0.0.1:4110
[00.263](19) OVERSEER: Received message from client: DESTSELECT 201 HELLO#
[00.263](19) OVERSEER: Got reg event from destselect 201
[01.350](6) SIMULATOR: Cardreader sim (#0): scanned code 4b6f9c1d4d55506c
[01.350](19) OVERSEER: Received message from client: CARDREADER 101 SCANNED 4b6f9c1d4d55506c#
[01.350](19) OVERSEER: Got scan from cardreader 101: 4b6f9c1d4d55506c
[01.350](6) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.350](0) DOOR.101: Received message: OPEN#
[01.350](0) DOOR.101: Current status: C
[01.350](0) DOOR.101: OPENING#
[01.350](19) OVERSEER: Received OPENING# from door
[01.350](4) SIMULATOR: Door sim (#0) woke up. Status = o
[01.360](4) SIMULATOR: Door sim (#0) changed status to = O
[01.360](0) DOOR.101: OPENED#
[01.360](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.440](22) SIMULATOR: Destselect sim (#0): scanned code 4b6f9c1d4d55506c and floor 2
[01.440](0) DESTSELECT.101: Scanned code: 4b6f9c1d4d55506c and floor: 2 - connecting to overseer
[01.440](18) OVERSEER: Received message from client: DESTSELECT 101 SCANNED 4b6f9c1d4d55506c 2#
[01.440](18) OVERSEER: Got scan from destselect 101: 4b6f9c1d4d55506c, floor 2
[01.449](0) ELEVATOR.1: Received message: FROM 1 TO 2#
[01.450](0) DESTSELECT.101: Received response: ALLOWED#
[01.450](22) SIMULATOR: Destselect sim (#0): response to scan: Y
[01.460](0) DOOR.101: Received message: CLOSE#
[01.460](0) DOOR.101: Current status: O
[01.460](0) DOOR.101: CLOSING#
[01.460](19) OVERSEER: Received CLOSING# from door
[01.460](4) SIMULATOR: Door sim (#0) woke up. Status = c
[01.469](7) SIMULATOR: Elevator sim (#0): Status is now O
[01.471](4) SIMULATOR: Door sim (#0) changed status to = C
[01.471](0) DOOR.101: CLOSED#
[01.471](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.789](7) SIMULATOR: Elevator sim (#0) moved from floor 1 to 2. Status is now C
[01.810](7) SIMULATOR: Elevator sim (#0): Status is now O
[01.870](23) SIMULATOR: Camera sim (#1) simulated motion (angle: 330, status: O)
[01.870](19) OVERSEER: Received message from client: CAMERA 22 MOTION#
[01.870](19) OVERSEER: Received motion event from camera #22
[01.890](9) SIMULATOR: Cardreader sim (#4): scanned code 4b6f9c1d4d55506c
[01.890](19) OVERSEER: Received message from client: CARDREADER 201 SCANNED 4b6f9c1d4d55506c#
[01.890](19) OVERSEER: Got scan from cardreader 201: 4b6f9c1d4d55506c
[01.890](9) SIMULATOR: Cardreader sim (#4): response to scan: Y
[01.890](0) DOOR.201: Received message: OPEN#
[01.890](0) DOOR.201: Current status: C
[01.890](0) DOOR.201: OPENING#
[01.890](19) OVERSEER: Received OPENING# from door
[01.890](2) SIMULATOR: Door sim (#2) woke up. Status = o
[01.900](2) SIMULATOR: Door sim (#2) changed status to = O
[01.900](0) DOOR.201: OPENED#
[01.900](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.910](20) SIMULATOR: Camera sim (#2) simulated motion (angle: 135, status: O)
[01.910](18) OVERSEER: Received message from client: CAMERA 33 MOTION#
[01.910](18) OVERSEER: Received motion event from camera #33
[01.940](16) SIMULATOR: Destselect sim (#2): scanned code 4b6f9c1d4d55506c and floor 5
[01.940](0) DESTSELECT.202: Scanned code: 4b6f9c1d4d55506c and floor: 5 - connecting to overseer
[01.940](18) OVERSEER: Received message from client: DESTSELECT 202 SCANNED 4b6f9c1d4d55506c 5#
[01.940](18) OVERSEER: Got scan from destselect 202: 4b6f9c1d4d55506c, floor 5
[01.948](0) ELEVATOR.2: Received message: FROM 2 TO 5#
[01.950](0) DESTSELECT.202: Received response: ALLOWED#
[01.950](16) SIMULATOR: Destselect sim (#2): response to scan: Y
[01.968](3) SIMULATOR: Elevator sim (#1): Status is now O
[02.000](0) DOOR.201: Received message: CLOSE#
[02.000](0) DOOR.201: Current status: O
[02.000](0) DOOR.201: CLOSING#
[02.000](2) SIMULATOR: Door sim (#2) woke up. Status = c
[02.000](19) OVERSEER: Received CLOSING# from door
[02.011](2) SIMULATOR: Door sim (#2) changed status to = C
[02.011](0) DOOR.201: CLOSED#
[02.011](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.289](3) SIMULATOR: Elevator sim (#1) moved from floor 2 to 3. Status is now C
[02.389](3) SIMULATOR: Elevator sim (#1) moved from floor 3 to 4
[02.489](3) SIMULATOR: Elevator sim (#1) moved from floor 4 to 5
[02.509](3) SIMULATOR: Elevator sim (#1): Status is now O
[02.740](19) SIMULATOR: Cardreader sim (#8): scanned code 4b6f9c1d4d55506c
[02.740](19) OVERSEER: Received message from client: CARDREADER 501 SCANNED 4b6f9c1d4d55506c#
[02.740](19) OVERSEER: Got scan from cardreader 501: 4b6f9c1d4d55506c
[02.740](19) SIMULATOR: Cardreader sim (#8): response to scan: Y
[02.740](0) DOOR.501: Received message: OPEN#
[02.740](0) DOOR.501: Current status: C
[02.740](0) DOOR.501: OPENING#
[02.740](19) OVERSEER: Received OPENING# from door
[02.740](1) SIMULATOR: Door sim (#4) woke up. Status = o
[02.750](1) SIMULATOR: Door sim (#4) changed status to = O
[02.750](0) DOOR.501: OPENED#
[02.750](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.770](13) SIMULATOR: Camera sim (#4) simulated motion (angle: 105, status: O)
[02.770](18) OVERSEER: Received message from client: CAMERA 55 MOTION#
[02.770](18) OVERSEER: Received motion event from camera #55
[02.850](0) DOOR.501: Received message: CLOSE#
[02.850](0) DOOR.501: Current status: O
[02.850](0) DOOR.501: CLOSING#
[02.850](19) OVERSEER: Received CLOSING# from door
[02.850](1) SIMULATOR: Door sim (#4) woke up. Status = c
[02.860](1) SIMULATOR: Door sim (#4) changed status to = C
[02.860](0) DOOR.501: CLOSED#
[02.860](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.950](15) SIMULATOR: Cardreader sim (#9): scanned code 4b6f9c1d4d55506c
[02.950](19) OVERSEER: Received message from client: CARDREADER 502 SCANNED 4b6f9c1d4d55506c#
[02.950](19) OVERSEER: Got scan from cardreader 502: 4b6f9c1d4d55506c
[02.950](15) SIMULATOR: Cardreader sim (#9): response to scan: Y
[02.950](0) DOOR.501: Received message: OPEN#
[02.950](0) DOOR.501: Current status: C
[02.950](0) DOOR.501: OPENING#
[02.950](19) OVERSEER: Received OPENING# from door
[02.950](1) SIMULATOR: Door sim (#4) woke up. Status = o
[02.960](1) SIMULATOR: Door sim (#4) changed status to = O
[02.960](0) DOOR.501: OPENED#
[02.960](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[03.050](17) SIMULATOR: Destselect sim (#6): scanned code 4b6f9c1d4d55506c and floor 2
[03.050](0) DESTSELECT.502: Scanned code: 4b6f9c1d4d55506c and floor: 2 - connecting to overseer
[03.050](18) OVERSEER: Received message from client: DESTSELECT 502 SCANNED 4b6f9c1d4d55506c 2#
[03.050](18) OVERSEER: Got scan from destselect 502: 4b6f9c1d4d55506c, floor 2
[03.053](0) ELEVATOR.2: Received message: FROM 5 TO 2#
[03.060](0) DESTSELECT.502: Received response: ALLOWED#
[03.060](17) SIMULATOR: Destselect sim (#6): response to scan: Y
[03.060](0) DOOR.501: Received message: CLOSE#
[03.060](0) DOOR.501: Current status: O
[03.060](0) DOOR.501: CLOSING#
[03.060](19) OVERSEER: Received CLOSING# from door
[03.060](1) SIMULATOR: Door sim (#4) woke up. Status = c
[03.070](1) SIMULATOR: Door sim (#4) changed status to = C
[03.070](0) DOOR.501: CLOSED#
[03.071](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.273](3) SIMULATOR: Elevator sim (#1): Status is now C
[03.293](3) SIMULATOR: Elevator sim (#1): Status is now O
[03.613](3) SIMULATOR: Elevator sim (#1) moved from floor 5 to 4. Status is now C
[03.713](3) SIMULATOR: Elevator sim (#1) moved from floor 4 to 3
[03.750](20) SIMULATOR: Camera sim (#2) simulated motion (angle: 135, status: O)
[03.750](19) OVERSEER: Received message from client: CAMERA 33 MOTION#
[03.750](19) OVERSEER: Received motion event from camera #33
[03.813](3) SIMULATOR: Elevator sim (#1) moved from floor 3 to 2
[03.833](3) SIMULATOR: Elevator sim (#1): Status is now O
[03.850](5) SIMULATOR: Cardreader sim (#5): scanned code 4b6f9c1d4d55506c
[03.850](19) OVERSEER: Received message from client: CARDREADER 202 SCANNED 4b6f9c1d4d55506c#
[03.850](19) OVERSEER: Got scan from cardreader 202: 4b6f9c1d4d55506c
[03.850](5) SIMULATOR: Cardreader sim (#5): response to scan: Y
[03.850](0) DOOR.201: Received message: OPEN#
[03.850](0) DOOR.201: Current status: C
[03.850](0) DOOR.201: OPENING#
[03.850](19) OVERSEER: Received OPENING# from door
[03.850](2) SIMULATOR: Door sim (#2) woke up. Status = o
[03.860](2) SIMULATOR: Door sim (#2) changed status to = O
[03.860](0) DOOR.201: OPENED#
[03.860](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[03.950](23) SIMULATOR: Camera sim (#1) simulated motion (angle: 330, status: O)
[03.950](18) OVERSEER: Received message from client: CAMERA 22 MOTION#
[03.950](18) OVERSEER: Received motion event from camera #22
[03.960](0) DOOR.201: Received message: CLOSE#
[03.960](0) DOOR.201: Current status: O
[03.960](0) DOOR.201: CLOSING#
[03.960](19) OVERSEER: Received CLOSING# from door
[03.960](2) SIMULATOR: Door sim (#2) woke up. Status = c
[03.970](2) SIMULATOR: Door sim (#2) changed status to = C
[03.970](0) DOOR.201: CLOSED#
[03.971](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[04.050](11) SIMULATOR: Destselect sim (#1): scanned code 4b6f9c1d4d55506c and floor 1
[04.050](0) DESTSELECT.201: Scanned code: 4b6f9c1d4d55506c and floor: 1 - connecting to overseer
[04.050](19) OVERSEER: Received message from client: DESTSELECT 201 SCANNED 4b6f9c1d4d55506c 1#
[04.050](19) OVERSEER: Got scan from destselect 201: 4b6f9c1d4d55506c, floor 1
[04.054](0) ELEVATOR.1: Received message: FROM 2 TO 1#
[04.060](0) DESTSELECT.201: Received response: ALLOWED#
[04.060](11) SIMULATOR: Destselect sim (#1): response to scan: Y
[04.274](7) SIMULATOR: Elevator sim (#0): Status is now C
[04.294](7) SIMULATOR: Elevator sim (#0): Status is now O
[04.614](7) SIMULATOR: Elevator sim (#0) moved from floor 2 to 1. Status is now C
[04.635](7) SIMULATOR: Elevator sim (#0): Status is now O
[04.750](8) SIMULATOR: Cardreader sim (#1): scanned code 4b6f9c1d4d55506c
[04.750](19) OVERSEER: Received message from client: CARDREADER 102 SCANNED 4b6f9c1d4d55506c#
[04.750](19) OVERSEER: Got scan from cardreader 102: 4b6f9c1d4d55506c
[04.750](8) SIMULATOR: Cardreader sim (#1): response to scan: Y
[04.750](0) DOOR.101: Received message: OPEN#
[04.750](0) DOOR.101: Current status: C
[04.750](0) DOOR.101: OPENING#
[04.750](19) OVERSEER: Received OPENING# from door
[04.750](4) SIMULATOR: Door sim (#0) woke up. Status = o
[04.760](4) SIMULATOR: Door sim (#0) changed status to = O
[04.760](0) DOOR.101: OPENED#
[04.760](19) OVERSEER: Received OPENED# from door (should be OPENED#)
[04.850](13) SIMULATOR: Camera sim (#4) simulated motion (angle: 105, status: O)
[04.850](18) OVERSEER: Received message from client: CAMERA 55 MOTION#
[04.850](18) OVERSEER: Received motion event from camera #55
[04.850](18) OVERSEER: Alert in sector 9
Security alarm triggered!
[04.850](25) SIMULATOR: Security alarm has been triggered.
[04.850](0) DOOR.102: Received message: CLOSE_SECURE#
[04.850](0) DOOR.102: Current status: C
[04.850](0) DOOR.501: Received message: CLOSE_SECURE#
[04.850](0) DOOR.102: CLOSING# (security)
[04.851](0) DOOR.501: Current status: C
[04.851](0) DOOR.501: CLOSING# (security)
[04.851](10) SIMULATOR: Door sim (#1) woke up. Status = c
[04.851](1) SIMULATOR: Door sim (#4) woke up. Status = c
[04.860](0) DOOR.101: Received message: CLOSE#
[04.860](0) DOOR.101: Current status: O
[04.860](0) DOOR.101: CLOSING#
[04.860](4) SIMULATOR: Door sim (#0) woke up. Status = c
[04.860](19) OVERSEER: Received CLOSING# from door
[04.861](10) SIMULATOR: Door sim (#1) changed status to = C
[04.861](1) SIMULATOR: Door sim (#4) changed status to = C
[04.861](0) DOOR.102: CLOSED# (security)
[04.861](0) DOOR.501: CLOSED# (security)
[04.870](4) SIMULATOR: Door sim (#0) changed status to = C
[04.870](0) DOOR.101: CLOSED#
[04.870](19) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[05.850](26) SIMULATOR: Simulation ended, shutting down
"""

cardreader_3_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 10000us Datagram resend delay: 2500us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Launching firealarm
[00.250](0) SIMULATOR: Launching tempsensor
[00.250](0) SIMULATOR: Launching tempsensor
[00.252](1) SIMULATOR: Cardreader sim (#5) started
[00.252](2) SIMULATOR: Cardreader sim (#9) started
[00.252](3) SIMULATOR: Door sim (#2) started
[00.252](4) SIMULATOR: Elevator sim (#1) started
[00.252](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4200
[00.252](0) DOOR.101: Binding addr 127.0.0.1:4202
[00.252](0) DOOR.301: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7024. Overseer addr: 127.0.0.1:4200
[00.252](0) DOOR.301: Binding addr 127.0.0.1:4205
[00.252](5) SIMULATOR: Tempsensor sim (#2) started
[00.252](6) SIMULATOR: Cardreader sim (#3) started
[00.252](7) SIMULATOR: Cardreader sim (#7) started
[00.252](8) SIMULATOR: Destselect sim (#2) started
[00.252](9) SIMULATOR: Destselect sim (#3) started
[00.253](0) TEMPSENSOR.101: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9472.
[00.253](0) TEMPSENSOR.101: Receiver #1: 127.0.0.1:4200
[00.253](0) TEMPSENSOR.101: Receiver #2: 127.0.0.1:4209
[00.253](0) TEMPSENSOR.101: Binding addr 127.0.0.1:4207
[00.253](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.253](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.253](10) SIMULATOR: Cardreader sim (#4) started
[00.252](11) SIMULATOR: Destselect sim (#5) started
[00.253](0) SIMULATOR: Launching tempsensor
[00.253](2) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.253](2) OVERSEER: Got reg event from cardreader 103
[00.254](0) SIMULATOR: Launching tempsensor
[00.252](12) SIMULATOR: Destselect sim (#0) started
[00.254](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 10. Detection period: 100000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4200
[00.252](13) SIMULATOR: Tempsensor sim (#0) started
[00.252](14) SIMULATOR: Tempsensor sim (#3) started
[00.252](15) SIMULATOR: Tempsensor sim (#4) started
[00.252](16) SIMULATOR: Elevator sim (#0) started
[00.252](17) SIMULATOR: Destselect sim (#1) started
[00.254](18) SIMULATOR: Door sim (#3) started
[00.253](19) SIMULATOR: Door sim (#0) started
[00.254](20) SIMULATOR: Destselect sim (#6) started
[00.254](0) FIREALARM: Binding addr 127.0.0.1:4201
[00.253](21) SIMULATOR: Door sim (#1) started
[00.253](22) SIMULATOR: Camera sim (#3) started
[00.253](23) SIMULATOR: Door sim (#4) started
[00.253](24) SIMULATOR: Camera sim (#4) started
[00.253](25) SIMULATOR: Tempsensor sim (#1) started
[00.253](26) SIMULATOR: Cardreader sim (#6) started
[00.254](27) SIMULATOR: Camera sim (#0) started
[00.254](28) SIMULATOR: Cardreader sim (#2) started
[00.254](29) SIMULATOR: Camera sim (#1) started
[00.254](3) OVERSEER: Received message from client: CARDREADER 501 HELLO#
[00.254](30) SIMULATOR: Camera sim (#2) started
[00.254](3) OVERSEER: Got reg event from cardreader 501
[00.254](31) SIMULATOR: Cardreader sim (#8) started
[00.254](32) SIMULATOR: Cardreader sim (#1) started
[00.254](33) SIMULATOR: Cardreader sim (#0) started
[00.254](4) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.254](4) OVERSEER: Got reg event from cardreader 102
[00.254](5) OVERSEER: Received message from client: CARDREADER 502 HELLO#
[00.254](5) OVERSEER: Got reg event from cardreader 502
[00.252](34) SIMULATOR: Destselect sim (#4) started
[00.254](0) SIMULATOR: Launching tempsensor
[00.254](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4201 HELLO#
[00.254](2) OVERSEER: Registered fire alarm @127.0.0.1:4201
[00.254](3) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.254](3) OVERSEER: Got reg event from cardreader 101
[00.254](6) OVERSEER: Received message from client: DOOR 301 127.0.0.1:4205 FAIL_SAFE#
[00.254](6) OVERSEER: Registered door #301 @127.0.0.1:4205 (FAIL_SAFE#)
[00.255](0) FIREALARM: Got door registration packet
[00.256](7) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4202 FAIL_SAFE#
[00.256](7) OVERSEER: Registered door #101 @127.0.0.1:4202 (FAIL_SAFE#)
[00.256](0) FIREALARM: Got door registration packet
[00.259](0) DESTSELECT.301: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50128. Overseer addr: 127.0.0.1:4200
[00.259](0) TEMPSENSOR.102: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9568.
[00.259](0) TEMPSENSOR.102: Receiver #1: 127.0.0.1:4210
[00.259](0) TEMPSENSOR.102: Binding addr 127.0.0.1:4208
[00.259](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.259](0) DOOR.102: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4200
[00.260](0) DOOR.102: Binding addr 127.0.0.1:4203
[00.260](0) TEMPSENSOR.103: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9664.
[00.260](0) TEMPSENSOR.103: Receiver #1: 127.0.0.1:4208
[00.260](0) TEMPSENSOR.103: Binding addr 127.0.0.1:4209
[00.260](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.260](0) DOOR.501: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 7168. Overseer addr: 127.0.0.1:4200
[00.260](0) DOOR.501: Binding addr 127.0.0.1:4206
[00.260](0) TEMPSENSOR.105: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9856.
[00.260](0) TEMPSENSOR.105: Receiver #1: 127.0.0.1:4209
[00.260](0) TEMPSENSOR.105: Receiver #2: 127.0.0.1:4201
[00.260](0) TEMPSENSOR.105: Binding addr 127.0.0.1:4211
[00.260](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.260](0) FIREALARM: Received temperature (22.00)
[00.261](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.261](0) DESTSELECT.502: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50800. Overseer addr: 127.0.0.1:4200
[00.261](0) DESTSELECT.502: Attempting to connect to 127.0.0.1:4200
[00.261](0) DESTSELECT.502: Sending HELLO#
[00.261](0) DESTSELECT.301: Attempting to connect to 127.0.0.1:4200
[00.261](0) DESTSELECT.301: Sending HELLO#
[00.261](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.261](7) OVERSEER: Received message from client: DOOR 501 127.0.0.1:4206 FAIL_SAFE#
[00.261](7) OVERSEER: Registered door #501 @127.0.0.1:4206 (FAIL_SAFE#)
[00.261](0) FIREALARM: Got door registration packet
[00.261](0) TEMPSENSOR.104: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9760.
[00.261](4) OVERSEER: Received message from client: DESTSELECT 502 HELLO#
[00.261](4) OVERSEER: Got reg event from destselect 502
[00.261](5) OVERSEER: Received message from client: CARDREADER 301 HELLO#
[00.261](5) OVERSEER: Got reg event from cardreader 301
[00.261](0) TEMPSENSOR.104: Receiver #1: 127.0.0.1:4207
[00.261](0) TEMPSENSOR.104: Binding addr 127.0.0.1:4210
[00.261](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.261](2) OVERSEER: Received message from client: DESTSELECT 301 HELLO#
[00.261](2) OVERSEER: Got reg event from destselect 301
[00.261](0) DOOR.201: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6880. Overseer addr: 127.0.0.1:4200
[00.262](0) DOOR.201: Binding addr 127.0.0.1:4204
[00.262](0) CAMERA.33: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 16960. Overseer addr: 127.0.0.1:4200
[00.262](0) CAMERA.33: Binding addr 127.0.0.1:4216
[00.262](0) DESTSELECT.202: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50296. Overseer addr: 127.0.0.1:4200
[00.262](0) DESTSELECT.202: Attempting to connect to 127.0.0.1:4200
[00.262](0) DESTSELECT.202: Sending HELLO#
[00.262](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.262](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.262](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.263](0) CAMERA.44: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 18784. Overseer addr: 127.0.0.1:4200
[00.263](0) CAMERA.44: Binding addr 127.0.0.1:4217
[00.263](0) DESTSELECT.402: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50632. Overseer addr: 127.0.0.1:4200
[00.263](0) DESTSELECT.101: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49792. Overseer addr: 127.0.0.1:4200
[00.263](0) DESTSELECT.402: Attempting to connect to 127.0.0.1:4200
[00.263](0) DESTSELECT.101: Attempting to connect to 127.0.0.1:4200
[00.263](0) DESTSELECT.101: Sending HELLO#
[00.263](0) DESTSELECT.402: Sending HELLO#
[00.263](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.263](8) OVERSEER: Received message from client: CAMERA 44 127.0.0.1:4217 HELLO#
[00.263](0) ELEVATOR.1: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53152. Overseer addr: 127.0.0.1:4200
[00.263](5) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.263](5) OVERSEER: Got reg event from cardreader 104
[00.263](8) OVERSEER: Registered camera #44 @127.0.0.1:4217
[00.263](0) ELEVATOR.1: Binding addr 127.0.0.1:4212
[00.263](2) OVERSEER: Received message from client: DOOR 201 127.0.0.1:4204 FAIL_SAFE#
[00.263](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.263](2) OVERSEER: Registered door #201 @127.0.0.1:4204 (FAIL_SAFE#)
[00.263](9) OVERSEER: Received message from client: DESTSELECT 101 HELLO#
[00.263](9) OVERSEER: Got reg event from destselect 101
[00.263](10) OVERSEER: Received message from client: DESTSELECT 402 HELLO#
[00.263](10) OVERSEER: Got reg event from destselect 402
[00.263](4) OVERSEER: Received message from client: CAMERA 33 127.0.0.1:4216 HELLO#
[00.263](4) OVERSEER: Registered camera #33 @127.0.0.1:4216
[00.263](7) OVERSEER: Received message from client: DESTSELECT 202 HELLO#
[00.263](7) OVERSEER: Got reg event from destselect 202
[00.264](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.264](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.264](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.264](0) DESTSELECT.201: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49960. Overseer addr: 127.0.0.1:4200
[00.264](0) DESTSELECT.201: Attempting to connect to 127.0.0.1:4200
[00.264](0) DESTSELECT.201: Sending HELLO#
[00.264](0) ELEVATOR.2: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53296. Overseer addr: 127.0.0.1:4200
[00.264](6) OVERSEER: Received message from client: CARDREADER 201 HELLO#
[00.264](6) OVERSEER: Got reg event from cardreader 201
[00.264](0) ELEVATOR.2: Binding addr 127.0.0.1:4213
[00.265](4) OVERSEER: Received message from client: CARDREADER 202 HELLO#
[00.265](4) OVERSEER: Got reg event from cardreader 202
[00.265](0) DESTSELECT.302: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50464. Overseer addr: 127.0.0.1:4200
[00.265](0) DESTSELECT.302: Attempting to connect to 127.0.0.1:4200
[00.265](0) DESTSELECT.302: Sending HELLO#
[00.265](4) OVERSEER: Received message from client: DESTSELECT 302 HELLO#
[00.265](4) OVERSEER: Got reg event from destselect 302
[00.265](8) OVERSEER: Received message from client: ELEVATOR 1 127.0.0.1:4212 HELLO#
[00.265](8) OVERSEER: Registered elevator #1 @127.0.0.1:4212
[00.265](0) CAMERA.22: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 15136. Overseer addr: 127.0.0.1:4200
[00.266](0) CAMERA.22: Binding addr 127.0.0.1:4215
[00.266](11) OVERSEER: Received message from client: DESTSELECT 201 HELLO#
[00.266](11) OVERSEER: Got reg event from destselect 201
[00.266](6) OVERSEER: Received message from client: CARDREADER 302 HELLO#
[00.266](6) OVERSEER: Got reg event from cardreader 302
[00.266](0) FIREALARM: Got door registration packet
[00.266](7) OVERSEER: Received message from client: ELEVATOR 2 127.0.0.1:4213 HELLO#
[00.266](7) OVERSEER: Registered elevator #2 @127.0.0.1:4213
[00.266](3) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4203 FAIL_SAFE#
[00.266](3) OVERSEER: Registered door #102 @127.0.0.1:4203 (FAIL_SAFE#)
[00.266](8) OVERSEER: Received message from client: CAMERA 22 127.0.0.1:4215 HELLO#
[00.266](8) OVERSEER: Registered camera #22 @127.0.0.1:4215
[00.267](0) CAMERA.55: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 20608. Overseer addr: 127.0.0.1:4200
[00.267](0) CAMERA.55: Binding addr 127.0.0.1:4218
[00.267](0) FIREALARM: Got door registration packet
[00.267](8) OVERSEER: Received message from client: CAMERA 55 127.0.0.1:4218 HELLO#
[00.267](8) OVERSEER: Registered camera #55 @127.0.0.1:4218
[00.267](0) CAMERA.11: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 13312. Overseer addr: 127.0.0.1:4200
[00.267](0) CAMERA.11: Binding addr 127.0.0.1:4214
[00.267](8) OVERSEER: Received message from client: CAMERA 11 127.0.0.1:4214 HELLO#
[00.268](8) OVERSEER: Registered camera #11 @127.0.0.1:4214
[00.303](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.303](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.303](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.303](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.310](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.310](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.310](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.310](0) FIREALARM: Received temperature (22.00)
[00.310](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.310](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.310](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.311](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.311](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.311](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.311](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.311](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.312](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.312](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.312](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.313](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.313](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.313](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.313](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.313](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.314](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.314](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.353](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.353](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.353](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.353](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.361](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.361](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.361](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.361](0) FIREALARM: Received temperature (22.00)
[00.361](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.361](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.361](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.362](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.362](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.362](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.362](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.363](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.363](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.363](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.363](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.363](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.364](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.364](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.364](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.365](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.365](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.365](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.404](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.404](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.405](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.405](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.412](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.412](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.412](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.412](0) FIREALARM: Received temperature (22.00)
[00.413](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.413](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.413](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.413](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.413](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.413](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.413](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.413](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.414](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.414](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.414](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.414](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.414](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.415](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.415](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.415](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.416](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.416](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.455](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.455](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.456](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.456](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.463](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.463](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.463](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.463](0) FIREALARM: Received temperature (22.00)
[00.464](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.464](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.464](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.464](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.464](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.464](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.464](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.464](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.465](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.465](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.465](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.465](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.465](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.466](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.466](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.466](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.467](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.467](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.506](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.506](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.507](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.508](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.513](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.514](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.514](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.514](0) FIREALARM: Received temperature (22.00)
[00.515](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.515](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.515](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.515](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.515](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.515](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.516](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.516](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.516](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.516](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.516](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.517](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.517](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.517](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.517](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.518](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.518](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.518](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.557](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.557](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.557](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.558](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.564](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.565](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.565](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.565](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.565](0) FIREALARM: Received temperature (22.00)
[00.565](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.566](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.566](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.566](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.566](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.566](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.566](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.567](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.567](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.567](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.567](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.567](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.568](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.568](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.568](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.569](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.569](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.607](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.607](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.607](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.608](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.615](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.616](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.616](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.616](0) FIREALARM: Received temperature (22.00)
[00.616](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.616](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.617](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.617](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.617](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.617](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.617](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.617](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.617](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.618](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.618](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.618](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.618](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.619](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.619](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.619](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.620](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.620](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.657](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.657](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.657](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.658](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.666](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.667](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.667](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.667](0) FIREALARM: Received temperature (22.00)
[00.667](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.667](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.668](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.668](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.668](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.668](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.668](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.668](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.668](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.669](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.669](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.669](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.669](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.670](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.670](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.670](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.671](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.671](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.708](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.708](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.709](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.710](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.717](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.718](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.718](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.718](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.718](0) FIREALARM: Received temperature (22.00)
[00.718](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.719](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.719](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.719](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.719](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.719](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.719](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.719](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.720](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.720](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.720](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.720](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.721](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.721](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.721](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.722](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.722](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.759](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.759](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.760](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.761](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.768](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.769](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.769](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.769](0) FIREALARM: Received temperature (22.00)
[00.769](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.769](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.770](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.770](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.770](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.770](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.770](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.770](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.770](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.771](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.771](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.771](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.771](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.772](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.772](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.772](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.773](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.773](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.809](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.809](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.810](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.811](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.819](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.820](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.820](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.820](0) FIREALARM: Received temperature (22.00)
[00.820](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.820](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.821](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.821](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.821](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.821](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.821](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.821](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.821](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.822](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.822](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.822](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.822](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.823](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.823](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.823](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.824](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.824](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.860](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.860](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.861](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.862](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.870](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.871](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.871](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.871](0) FIREALARM: Received temperature (22.00)
[00.871](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.871](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.872](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.872](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.872](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.872](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.872](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.872](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.872](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.873](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.873](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.873](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.873](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.874](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.874](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.874](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.875](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.875](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.911](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.911](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.912](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.913](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.921](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.921](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.922](0) FIREALARM: Received temperature (22.00)
[00.922](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.922](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.922](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.922](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.923](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.923](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.923](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.923](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.923](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.923](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.924](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.924](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.924](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.924](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.925](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.925](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.925](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.926](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.926](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.962](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.962](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.963](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[00.964](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[00.972](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.972](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.972](0) FIREALARM: Received temperature (22.00)
[00.973](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.973](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[00.973](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[00.973](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[00.974](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[00.974](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[00.974](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.974](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.974](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[00.974](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[00.975](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[00.975](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[00.975](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[00.975](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.976](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[00.976](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[00.976](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.977](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[00.977](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.012](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.012](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.013](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.014](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.023](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.023](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.023](0) FIREALARM: Received temperature (22.00)
[01.024](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.024](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.024](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.024](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.025](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.025](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.025](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.025](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.025](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.025](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.026](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.026](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.026](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.026](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.027](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.027](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.027](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.028](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.028](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.063](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.063](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.064](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.064](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.074](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.074](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.074](0) FIREALARM: Received temperature (22.00)
[01.075](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.075](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.075](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.075](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.075](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.075](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.075](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.076](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.076](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.076](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.076](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.076](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.076](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.077](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.077](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.077](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.077](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.078](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.078](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.114](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.114](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.115](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.115](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.125](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.125](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.125](0) FIREALARM: Received temperature (22.00)
[01.126](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.126](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.126](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.126](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.126](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.126](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.126](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.127](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.127](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.127](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.127](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.127](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.127](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.128](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.128](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.128](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.128](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.129](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.129](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.165](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.165](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.166](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.167](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.175](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.176](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.176](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.176](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.176](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.176](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.176](0) FIREALARM: Received temperature (22.00)
[01.176](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.177](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.178](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.178](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.178](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.178](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.178](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.178](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.178](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.179](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.179](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.179](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.179](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.180](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.180](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.216](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.216](1) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.217](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4208
[01.218](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4210
[01.226](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.227](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4207
[01.227](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.227](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4200
[01.227](0) FIREALARM: Received temperature (22.00)
[01.227](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4209
[01.227](1) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.228](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.228](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4208
[01.228](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4210
[01.229](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.229](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4207
[01.229](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4200
[01.229](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4210
[01.229](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4209
[01.229](1) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.230](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4208
[01.230](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4207
[01.230](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4200
[01.230](1) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.231](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4200
[01.231](1) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.256](33) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.256](7) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.256](7) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.256](33) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.257](0) DOOR.101: Received message: OPEN#
[01.257](0) DOOR.101: Current status: C
[01.257](0) DOOR.101: OPENING#
[01.257](7) OVERSEER: Received OPENING# from door
[01.257](19) SIMULATOR: Door sim (#0) woke up. Status = o
[01.258](19) SIMULATOR: Door sim (#0) changed status to = O
[01.258](0) DOOR.101: OPENED#
[01.258](7) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.265](13) SIMULATOR: Tempsensor sim (#0): temperature changed to 24.58
[01.265](0) TEMPSENSOR.101: Temperature is 24.58 - sending update
[01[...(truncated)...]83
[02.192](19) SIMULATOR: Door sim (#0) changed status to = C
[02.192](0) DOOR.101: CLOSED#
[02.192](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.192](29) SIMULATOR: Camera sim (#1) simulated motion (angle: 0, status: O)
[02.192](3) OVERSEER: Received message from client: CAMERA 22 MOTION#
[02.192](3) OVERSEER: Received motion event from camera #22
[02.195](16) SIMULATOR: Elevator sim (#0): Status is now C
[02.196](16) SIMULATOR: Elevator sim (#0): Status is now O
[02.197](5) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.197](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.198](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.199](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.199](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.199](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.200](15) SIMULATOR: Tempsensor sim (#4): temperature changed to 30.00
[02.200](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.200](0) FIREALARM: Received temperature (30.00)
[02.200](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.201](0) DOOR.201: Received message: CLOSE#
[02.201](0) DOOR.201: Current status: O
[02.201](0) DOOR.201: CLOSING#
[02.201](3) SIMULATOR: Door sim (#2) woke up. Status = c
[02.201](7) OVERSEER: Received CLOSING# from door
[02.201](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.202](10) SIMULATOR: Cardreader sim (#4): scanned code db4ed0a0bfbb00ac
[02.202](3) OVERSEER: Received message from client: CARDREADER 201 SCANNED db4ed0a0bfbb00ac#
[02.202](3) OVERSEER: Got scan from cardreader 201: db4ed0a0bfbb00ac
[02.202](10) SIMULATOR: Cardreader sim (#4): response to scan: Y
[02.202](3) SIMULATOR: Door sim (#2) changed status to = C
[02.202](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.202](0) DOOR.201: CLOSED#
[02.202](7) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.202](0) DOOR.201: Received message: OPEN#
[02.202](0) DOOR.201: Current status: C
[02.202](0) DOOR.201: OPENING#
[02.202](3) SIMULATOR: Door sim (#2) woke up. Status = o
[02.202](3) OVERSEER: Received OPENING# from door
[02.202](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.202](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.203](3) SIMULATOR: Door sim (#2) changed status to = O
[02.203](0) DOOR.201: OPENED#
[02.203](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.203](0) TEMPSENSOR.102: Temperature is 27.66 - sending update
[02.203](30) SIMULATOR: Camera sim (#2) simulated motion (angle: 0, status: O)
[02.204](7) OVERSEER: Received message from client: CAMERA 33 MOTION#
[02.204](7) OVERSEER: Received motion event from camera #33
[02.204](0) TEMPSENSOR.104: Propagating update (102:27.66) to 127.0.0.1:4207
[02.204](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4200
[02.204](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4209
[02.204](1) OVERSEER: Received UDP TEMP packet: id=102 temp=27.66
[02.208](9) SIMULATOR: Destselect sim (#3): scanned code db4ed0a0bfbb00ac and floor 3
[02.208](0) DESTSELECT.202: Scanned code: db4ed0a0bfbb00ac and floor: 3 - connecting to overseer
[02.208](7) OVERSEER: Received message from client: DESTSELECT 202 SCANNED db4ed0a0bfbb00ac 3#
[02.208](7) OVERSEER: Got scan from destselect 202: db4ed0a0bfbb00ac, floor 3
[02.210](25) SIMULATOR: Tempsensor sim (#1): temperature changed to 28.13
[02.210](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.210](16) SIMULATOR: Elevator sim (#0) moved from floor 3 to 2. Status is now C
[02.211](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.211](0) DESTSELECT.202: Received response: ALLOWED#
[02.211](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.211](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.211](9) SIMULATOR: Destselect sim (#3): response to scan: Y
[02.211](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.211](0) ELEVATOR.2: Received message: FROM 2 TO 3#
[02.212](16) SIMULATOR: Elevator sim (#0) moved from floor 2 to 1
[02.213](2) SIMULATOR: Cardreader sim (#9): scanned code 4b6f9c1d4d55506c
[02.213](7) OVERSEER: Received message from client: CARDREADER 502 SCANNED 4b6f9c1d4d55506c#
[02.213](7) OVERSEER: Got scan from cardreader 502: 4b6f9c1d4d55506c
[02.213](2) SIMULATOR: Cardreader sim (#9): response to scan: Y
[02.213](0) DOOR.501: Received message: OPEN#
[02.213](0) DOOR.501: Current status: C
[02.213](0) DOOR.501: OPENING#
[02.213](23) SIMULATOR: Door sim (#4) woke up. Status = o
[02.213](7) OVERSEER: Received OPENING# from door
[02.213](0) DOOR.201: Received message: CLOSE#
[02.213](0) DOOR.201: Current status: O
[02.213](0) DOOR.201: CLOSING#
[02.213](3) OVERSEER: Received CLOSING# from door
[02.213](3) SIMULATOR: Door sim (#2) woke up. Status = c
[02.214](16) SIMULATOR: Elevator sim (#0): Status is now O
[02.214](23) SIMULATOR: Door sim (#4) changed status to = O
[02.214](0) DOOR.501: OPENED#
[02.214](7) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.214](3) SIMULATOR: Door sim (#2) changed status to = C
[02.214](0) DOOR.201: CLOSED#
[02.215](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.221](13) SIMULATOR: Tempsensor sim (#0): temperature changed to 26.77
[02.221](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.221](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.222](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.222](4) SIMULATOR: Elevator sim (#1): Status is now C
[02.223](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.223](5) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.223](4) SIMULATOR: Elevator sim (#1): Status is now O
[02.223](33) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[02.224](3) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[02.224](3) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[02.224](33) SIMULATOR: Cardreader sim (#0): response to scan: Y
[02.224](0) DOOR.101: Received message: OPEN#
[02.224](0) DOOR.101: Current status: C
[02.224](0) DOOR.101: OPENING#
[02.224](3) OVERSEER: Received OPENING# from door
[02.224](19) SIMULATOR: Door sim (#0) woke up. Status = o
[02.224](0) DOOR.501: Received message: CLOSE#
[02.224](0) DOOR.501: Current status: O
[02.224](0) DOOR.501: CLOSING#
[02.224](23) SIMULATOR: Door sim (#4) woke up. Status = c
[02.224](7) OVERSEER: Received CLOSING# from door
[02.224](12) SIMULATOR: Destselect sim (#0): scanned code cae0efe252087308 and floor 3
[02.225](0) DESTSELECT.101: Scanned code: cae0efe252087308 and floor: 3 - connecting to overseer
[02.225](4) OVERSEER: Received message from client: DESTSELECT 101 SCANNED cae0efe252087308 3#
[02.225](4) OVERSEER: Got scan from destselect 101: cae0efe252087308, floor 3
[02.225](19) SIMULATOR: Door sim (#0) changed status to = O
[02.225](0) DOOR.101: OPENED#
[02.225](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.225](31) SIMULATOR: Cardreader sim (#8): scanned code 4b6f9c1d4d55506c
[02.225](4) OVERSEER: Received message from client: CARDREADER 501 SCANNED 4b6f9c1d4d55506c#
[02.225](4) OVERSEER: Got scan from cardreader 501: 4b6f9c1d4d55506c
[02.226](23) SIMULATOR: Door sim (#4) changed status to = C
[02.226](31) SIMULATOR: Cardreader sim (#8): response to scan: Y
[02.226](0) DOOR.501: CLOSED#
[02.226](7) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.226](0) DOOR.501: Received message: OPEN#
[02.226](0) DOOR.501: Current status: C
[02.226](0) DOOR.501: OPENING#
[02.226](23) SIMULATOR: Door sim (#4) woke up. Status = o
[02.226](4) OVERSEER: Received OPENING# from door
[02.226](0) ELEVATOR.1: Received message: FROM 1 TO 3#
[02.227](23) SIMULATOR: Door sim (#4) changed status to = O
[02.227](0) DOOR.501: OPENED#
[02.227](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.227](0) DESTSELECT.101: Received response: ALLOWED#
[02.227](12) SIMULATOR: Destselect sim (#0): response to scan: Y
[02.230](22) SIMULATOR: Camera sim (#3) simulated motion (angle: 0, status: O)
[02.230](7) OVERSEER: Received message from client: CAMERA 44 MOTION#
[02.230](7) OVERSEER: Received motion event from camera #44
[02.235](28) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[02.235](7) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[02.235](7) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[02.235](0) DOOR.101: Received message: CLOSE#
[02.235](0) DOOR.101: Current status: O
[02.235](0) DOOR.101: CLOSING#
[02.235](3) OVERSEER: Received CLOSING# from door
[02.235](19) SIMULATOR: Door sim (#0) woke up. Status = c
[02.235](0) DOOR.102: Received message: OPEN#
[02.235](28) SIMULATOR: Cardreader sim (#2): response to scan: Y
[02.235](0) DOOR.102: Current status: C
[02.235](0) DOOR.102: OPENING#
[02.235](7) OVERSEER: Received OPENING# from door
[02.235](21) SIMULATOR: Door sim (#1) woke up. Status = o
[02.236](19) SIMULATOR: Door sim (#0) changed status to = C
[02.236](0) DOOR.101: CLOSED#
[02.236](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.236](21) SIMULATOR: Door sim (#1) changed status to = O
[02.236](0) DOOR.102: OPENED#
[02.236](7) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.237](0) DOOR.501: Received message: CLOSE#
[02.237](4) SIMULATOR: Elevator sim (#1) moved from floor 2 to 3. Status is now C
[02.237](0) DOOR.501: Current status: O
[02.237](0) DOOR.501: CLOSING#
[02.237](23) SIMULATOR: Door sim (#4) woke up. Status = c
[02.237](4) OVERSEER: Received CLOSING# from door
[02.238](16) SIMULATOR: Elevator sim (#0): Status is now C
[02.238](14) SIMULATOR: Tempsensor sim (#3): temperature changed to 27.03
[02.238](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.238](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.238](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.238](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.238](4) SIMULATOR: Elevator sim (#1): Status is now O
[02.238](23) SIMULATOR: Door sim (#4) changed status to = C
[02.238](0) DOOR.501: CLOSED#
[02.238](4) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.239](16) SIMULATOR: Elevator sim (#0): Status is now O
[02.239](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.245](26) SIMULATOR: Cardreader sim (#6): scanned code cae0efe252087308
[02.245](4) OVERSEER: Received message from client: CARDREADER 301 SCANNED cae0efe252087308#
[02.245](4) OVERSEER: Got scan from cardreader 301: cae0efe252087308
[02.245](26) SIMULATOR: Cardreader sim (#6): response to scan: Y
[02.245](0) DOOR.301: Received message: OPEN#
[02.245](0) DOOR.301: Current status: C
[02.245](0) DOOR.301: OPENING#
[02.245](4) OVERSEER: Received OPENING# from door
[02.245](18) SIMULATOR: Door sim (#3) woke up. Status = o
[02.246](18) SIMULATOR: Door sim (#3) changed status to = O
[02.246](0) DOOR.301: OPENED#
[02.246](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.246](0) DOOR.102: Received message: CLOSE#
[02.246](0) DOOR.102: Current status: O
[02.246](0) DOOR.102: CLOSING#
[02.246](7) OVERSEER: Received CLOSING# from door
[02.246](21) SIMULATOR: Door sim (#1) woke up. Status = c
[02.247](21) SIMULATOR: Door sim (#1) changed status to = C
[02.247](0) DOOR.102: CLOSED#
[02.248](7) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.248](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.249](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.249](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.250](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.250](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.251](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.251](0) FIREALARM: Received temperature (30.00)
[02.251](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.252](16) SIMULATOR: Elevator sim (#0) moved from floor 1 to 2. Status is now C
[02.252](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.253](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.254](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.254](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.255](16) SIMULATOR: Elevator sim (#0) moved from floor 2 to 3
[02.256](16) SIMULATOR: Elevator sim (#0): Status is now O
[02.256](0) DOOR.301: Received message: CLOSE#
[02.256](0) DOOR.301: Current status: O
[02.256](0) DOOR.301: CLOSING#
[02.256](18) SIMULATOR: Door sim (#3) woke up. Status = c
[02.256](4) OVERSEER: Received CLOSING# from door
[02.257](18) SIMULATOR: Door sim (#3) changed status to = C
[02.257](0) DOOR.301: CLOSED#
[02.257](4) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.260](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.260](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.261](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.261](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.261](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.272](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.272](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.273](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.274](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.289](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.290](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.290](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.290](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.291](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.299](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.300](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.300](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.300](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.300](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.302](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.302](0) FIREALARM: Received temperature (30.00)
[02.302](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.303](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.303](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.304](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.304](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.311](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.311](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.311](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.311](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.311](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.323](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.323](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.323](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.323](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.340](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.341](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.341](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.341](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.341](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.350](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.350](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.350](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.351](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.351](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.353](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.353](0) FIREALARM: Received temperature (30.00)
[02.354](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.354](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.354](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.355](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.355](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.362](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.362](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.363](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.363](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.363](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.373](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.373](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.374](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.374](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.390](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.392](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.392](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.392](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.392](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.401](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.401](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.401](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.402](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.402](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.404](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.404](0) FIREALARM: Received temperature (30.00)
[02.405](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.405](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.405](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.406](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.406](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.413](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.413](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.414](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.414](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.414](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.424](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.424](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.424](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.424](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.441](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.442](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.442](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.442](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.442](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.452](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.452](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.452](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.452](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.452](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.455](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.455](0) FIREALARM: Received temperature (30.00)
[02.455](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.455](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.455](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.455](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.455](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.464](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.464](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.464](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.464](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.464](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.475](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.475](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.475](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.475](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.492](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.493](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.493](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.493](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.493](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.502](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.503](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.503](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.503](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.503](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.506](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.506](0) FIREALARM: Received temperature (30.00)
[02.506](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.506](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.506](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.507](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.507](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.515](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.515](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.515](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.515](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.515](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.525](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.525](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.525](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.525](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.543](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.544](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.544](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.544](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.544](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.553](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.554](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.554](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.554](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.554](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.556](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.557](0) FIREALARM: Received temperature (30.00)
[02.557](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.557](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.557](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.558](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.558](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.566](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.566](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.566](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.566](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.566](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.576](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.576](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.576](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.576](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.594](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.595](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.595](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.595](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.595](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.604](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.605](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.605](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.605](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.605](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.607](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.607](0) FIREALARM: Received temperature (30.00)
[02.608](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.608](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.608](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.609](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.609](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.617](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.617](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.617](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.617](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.617](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.627](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.627](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.627](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.627](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.645](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.646](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.646](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.646](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.646](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.655](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.656](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.657](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.657](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.657](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.658](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.659](0) FIREALARM: Received temperature (30.00)
[02.659](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.659](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.660](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.661](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.661](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.668](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.669](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.669](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.669](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.669](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.678](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.678](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.678](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.678](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.696](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.697](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.697](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.697](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.698](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.706](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.707](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.708](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.708](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.708](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.709](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.709](0) FIREALARM: Received temperature (30.00)
[02.709](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.710](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.710](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.711](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.711](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.719](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.720](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.720](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.720](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.720](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.729](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.729](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.730](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.730](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.747](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.747](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.747](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.747](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.748](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.757](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.758](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.759](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.760](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.760](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.760](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.760](0) FIREALARM: Received temperature (30.00)
[02.761](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.761](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.762](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.763](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.763](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.769](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.769](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.769](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.769](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.769](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.779](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.779](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.780](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.781](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.797](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.798](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.798](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.798](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.799](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.808](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.809](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.809](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.810](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.810](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.811](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.811](0) FIREALARM: Received temperature (30.00)
[02.812](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.812](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.812](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.813](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.813](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.820](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.820](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.820](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.820](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.820](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.829](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.829](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.830](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.830](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.849](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.849](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.849](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.849](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.850](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.859](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.860](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.860](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.861](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.861](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.862](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.862](0) FIREALARM: Received temperature (30.00)
[02.862](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.863](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.863](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.864](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.864](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.871](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.871](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.871](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.871](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.871](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.880](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.880](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.881](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.881](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.899](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.900](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.900](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.900](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.901](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.910](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.911](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.912](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.913](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.913](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.913](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.913](0) FIREALARM: Received temperature (30.00)
[02.913](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.914](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.915](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.916](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.916](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.922](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.923](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.923](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.923](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.923](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.931](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.931](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.931](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.932](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[02.950](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.951](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[02.951](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[02.951](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.952](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[02.961](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.962](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[02.963](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[02.964](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[02.964](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.964](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.964](0) FIREALARM: Received temperature (30.00)
[02.964](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[02.965](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[02.966](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[02.967](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[02.967](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.973](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.974](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[02.974](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[02.974](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[02.974](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.982](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.982](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.982](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[02.983](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.001](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.002](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.002](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.002](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.003](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.012](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.013](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.014](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.015](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.015](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.015](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.015](0) FIREALARM: Received temperature (30.00)
[03.015](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.016](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.017](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.018](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.018](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.024](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.025](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.025](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.025](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.025](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.033](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.033](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.033](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.034](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.052](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.053](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.053](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.053](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.054](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.063](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.064](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.065](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.066](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.066](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.066](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.066](0) FIREALARM: Received temperature (30.00)
[03.066](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.067](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.068](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.069](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.069](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.075](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.076](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.076](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.076](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.076](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.083](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.083](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.083](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.084](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.103](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.104](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.104](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.104](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.104](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.114](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.115](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.116](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.117](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.117](0) FIREALARM: Received temperature (30.00)
[03.117](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.117](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.117](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.118](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.119](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.120](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.120](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.126](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.127](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.127](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.127](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.127](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.134](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.134](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.134](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.135](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.154](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.155](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.155](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.155](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.155](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.165](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.166](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.167](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.168](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.168](0) FIREALARM: Received temperature (30.00)
[03.168](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.168](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.168](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.169](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.170](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.171](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.171](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.177](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.178](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.178](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.178](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.178](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.185](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.185](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.185](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.186](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.205](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.206](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4200
[03.206](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4209
[03.206](1) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.206](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4208
[03.216](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.216](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4210
[03.217](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4207
[03.217](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4200
[03.217](1) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.219](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.219](0) FIREALARM: Received temperature (30.00)
[03.219](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4208
[03.220](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4210
[03.221](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4207
[03.221](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4200
[03.221](1) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.228](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.228](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4207
[03.228](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4200
[03.228](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4209
[03.228](1) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.235](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.235](1) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.235](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4208
[03.236](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4210
[03.245](0) SIMULATOR: Simulation ended, shutting down
"""

# Door logs
door_1_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Door sim (#0) started
[00.249](1) SIMULATOR: Door sim (#1) started
[00.249](2) SIMULATOR: Cardreader sim (#0) started
[00.249](3) SIMULATOR: Cardreader sim (#2) started
[00.249](4) SIMULATOR: Cardreader sim (#1) started
[00.249](5) SIMULATOR: Cardreader sim (#3) started
[00.251](0) CARDREADER.102: Starting up. Shm path: /shm. Offset: 352. Overseer addr: 127.0.0.1:4300
[00.251](0) CARDREADER.102: Attempting to connect to 127.0.0.1:4300
[00.251](0) CARDREADER.101: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4300
[00.251](0) CARDREADER.102: Sending HELLO#
[00.251](0) CARDREADER.104: Starting up. Shm path: /shm. Offset: 672. Overseer addr: 127.0.0.1:4300
[00.251](0) CARDREADER.101: Attempting to connect to 127.0.0.1:4300
[00.251](0) CARDREADER.104: Attempting to connect to 127.0.0.1:4300
[00.251](0) CARDREADER.104: Sending HELLO#
[00.251](0) CARDREADER.101: Sending HELLO#
[00.251](1) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.251](1) OVERSEER: Got reg event from cardreader 102
[00.251](2) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.251](2) OVERSEER: Got reg event from cardreader 101
[00.251](3) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4301 FAIL_SAFE#
[00.251](4) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4302 FAIL_SECURE#
[00.251](5) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.251](5) OVERSEER: Got reg event from cardreader 104
[00.251](3) OVERSEER: Registered door #101 @127.0.0.1:4301 (FAIL_SAFE#)
[00.251](4) OVERSEER: Registered door #102 @127.0.0.1:4302 (FAIL_SECURE#)
[00.251](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 512. Overseer addr: 127.0.0.1:4300
[00.252](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4300
[00.252](0) CARDREADER.103: Sending HELLO#
[00.252](4) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.252](4) OVERSEER: Got reg event from cardreader 103
[01.299](6) SIMULATOR: Simulated input to overseer: DOOR LIST
101 127.0.0.1:4301 FAIL_SAFE
102 127.0.0.1:4302 FAIL_SECURE
[01.349](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 102
[01.349](2) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.349](0) CARDREADER.101: Scanned code: db4ed0a0bfbb00ac - connecting to overseer
[01.349](1) SIMULATOR: Door sim (#1) woke up. Status = o
[01.349](4) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.349](4) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.349](0) CARDREADER.101: Received response: ALLOWED#
[01.349](2) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.349](4) OVERSEER: Received OPENING# from door
[01.349](0) SIMULATOR: Door sim (#0) woke up. Status = o
[01.359](1) SIMULATOR: Door sim (#1) changed status to = O
[01.359](0) SIMULATOR: Door sim (#0) changed status to = O
[01.359](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.449](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 102
[01.449](1) SIMULATOR: Door sim (#1) woke up. Status = c
[01.459](1) SIMULATOR: Door sim (#1) changed status to = C
[01.459](4) OVERSEER: Received CLOSING# from door
[01.459](0) SIMULATOR: Door sim (#0) woke up. Status = c
[01.469](0) SIMULATOR: Door sim (#0) changed status to = C
[01.469](4) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.549](2) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](0) CARDREADER.101: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.549](4) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[01.549](4) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[01.549](0) CARDREADER.101: Received response: ALLOWED#
[01.549](2) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](4) OVERSEER: Received OPENING# from door
[01.549](0) SIMULATOR: Door sim (#0) woke up. Status = o
[01.559](0) SIMULATOR: Door sim (#0) changed status to = O
[01.559](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.569](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.569](0) SIMULATOR: Door sim (#0) woke up. Status = c
[01.579](0) SIMULATOR: Door sim (#0) changed status to = C
[01.659](4) OVERSEER: Received ALREADY# from door
[01.749](3) SIMULATOR: Cardreader sim (#2): scanned code db4ed0a0bfbb00ac
[01.749](0) CARDREADER.103: Scanned code: db4ed0a0bfbb00ac - connecting to overseer
[01.749](4) OVERSEER: Received message from client: CARDREADER 103 SCANNED db4ed0a0bfbb00ac#
[01.749](4) OVERSEER: Got scan from cardreader 103: db4ed0a0bfbb00ac
[01.749](0) CARDREADER.103: Received response: DENIED#
[01.749](3) SIMULATOR: Cardreader sim (#2): response to scan: N
[01.949](3) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[01.949](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.949](4) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.949](4) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.949](0) CARDREADER.103: Received response: ALLOWED#
[01.949](3) SIMULATOR: Cardreader sim (#2): response to scan: Y
[01.949](4) OVERSEER: Received OPENING# from door
[01.949](1) SIMULATOR: Door sim (#1) woke up. Status = o
[01.959](1) SIMULATOR: Door sim (#1) changed status to = O
[01.959](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.049](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 101
[02.049](0) SIMULATOR: Door sim (#0) woke up. Status = o
[02.059](0) SIMULATOR: Door sim (#0) changed status to = O
[02.059](4) OVERSEER: Received CLOSING# from door
[02.059](1) SIMULATOR: Door sim (#1) woke up. Status = c
[02.070](1) SIMULATOR: Door sim (#1) changed status to = C
[02.070](4) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.149](5) SIMULATOR: Cardreader sim (#3): scanned code 2214a7ba5943d923
[02.149](0) CARDREADER.104: Scanned code: 2214a7ba5943d923 - connecting to overseer
[02.149](4) OVERSEER: Received message from client: CARDREADER 104 SCANNED 2214a7ba5943d923#
[02.149](4) OVERSEER: Got scan from cardreader 104: 2214a7ba5943d923
[02.149](0) CARDREADER.104: Received response: ALLOWED#
[02.149](5) SIMULATOR: Cardreader sim (#3): response to scan: Y
[02.149](4) OVERSEER: Received OPENING# from door
[02.149](1) SIMULATOR: Door sim (#1) woke up. Status = o
[02.159](1) SIMULATOR: Door sim (#1) changed status to = O
[02.159](4) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.259](4) OVERSEER: Received CLOSING# from door
[02.259](1) SIMULATOR: Door sim (#1) woke up. Status = c
[02.270](1) SIMULATOR: Door sim (#1) changed status to = C
[02.270](4) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.149](6) SIMULATOR: Simulation ended, shutting down
"""

door_2_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Launching firealarm
[00.249](1) SIMULATOR: Door sim (#1) started
[00.249](2) SIMULATOR: Door sim (#0) started
[00.249](3) SIMULATOR: Cardreader sim (#0) started
[00.251](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 3. Detection period: 20000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4400
[00.251](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4400
[00.251](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4400
[00.251](0) CARDREADER.103: Sending HELLO#
[00.251](0) FIREALARM: Binding addr 127.0.0.1:4401
[00.251](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4402 FAIL_SAFE#
[00.251](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4401 HELLO#
[00.251](3) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.251](3) OVERSEER: Got reg event from cardreader 103
[00.251](2) OVERSEER: Registered fire alarm @127.0.0.1:4401
[00.251](1) OVERSEER: Registered door #101 @127.0.0.1:4402 (FAIL_SAFE#)
[00.251](4) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4403 FAIL_SECURE#
[00.251](4) OVERSEER: Registered door #102 @127.0.0.1:4403 (FAIL_SECURE#)
[00.251](0) FIREALARM: Got door registration packet
[01.399](0) SIMULATOR: Simulated input to overseer: FIRE ALARM
Fire alarm triggered!
[01.399](0) FIREALARM: Fire alarm activated!
[01.399](0) FIREALARM: Contacting door #0 @ 127.0.0.1:4402
[01.399](4) SIMULATOR: Security alarm has been triggered.
[01.399](0) FIREALARM: Got reply: 
[01.399](2) SIMULATOR: Door sim (#0) woke up. Status = o
[01.409](2) SIMULATOR: Door sim (#0) changed status to = O
[01.449](0) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
Door reports that it open due to an emergency and cannot be closed
[01.549](3) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.549](5) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.549](5) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.549](0) CARDREADER.103: Received response: ALLOWED#
[01.549](3) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](5) OVERSEER: Received OPENING# from door
[01.549](1) SIMULATOR: Door sim (#1) woke up. Status = o
[01.559](1) SIMULATOR: Door sim (#1) changed status to = O
[01.560](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.660](5) OVERSEER: Received CLOSING# from door
[01.660](1) SIMULATOR: Door sim (#1) woke up. Status = c
[01.670](1) SIMULATOR: Door sim (#1) changed status to = C
[01.670](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.549](0) SIMULATOR: Simulation ended, shutting down
"""

door_3_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 10000us Datagram resend delay: 2500us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.250](0) SIMULATOR: Launching tempsensor
[00.251](0) SIMULATOR: Launching tempsensor
[00.251](0) SIMULATOR: Launching tempsensor
[00.251](0) SIMULATOR: Launching tempsensor
[00.252](1) SIMULATOR: Cardreader sim (#0) started
[00.252](0) CARDREADER.302: Starting up. Shm path: /shm. Offset: 1312. Overseer addr: 127.0.0.1:4500
[00.252](0) SIMULATOR: Launching tempsensor
[00.253](0) CARDREADER.302: Attempting to connect to 127.0.0.1:4500
[00.253](2) SIMULATOR: Cardreader sim (#5) started
[00.253](0) CARDREADER.102: Starting up. Shm path: /shm. Offset: 352. Overseer addr: 127.0.0.1:4500
[00.253](0) CARDREADER.102: Attempting to connect to 127.0.0.1:4500
[00.253](0) CARDREADER.102: Sending HELLO#
[00.252](3) SIMULATOR: Cardreader sim (#1) started
[00.253](4) SIMULATOR: Cardreader sim (#6) started
[00.252](5) SIMULATOR: Cardreader sim (#2) started
[00.252](6) SIMULATOR: Cardreader sim (#3) started
[00.253](7) SIMULATOR: Cardreader sim (#7) started
[00.253](0) CARDREADER.302: Sending HELLO#
[00.253](1) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.253](1) OVERSEER: Got reg event from cardreader 102
[00.253](8) SIMULATOR: Cardreader sim (#9) started
[00.253](2) OVERSEER: Received message from client: CARDREADER 302 HELLO#
[00.253](2) OVERSEER: Got reg event from cardreader 302
[00.253](9) SIMULATOR: Cardreader sim (#8) started
[00.253](10) SIMULATOR: Door sim (#0) started
[00.253](11) SIMULATOR: Door sim (#1) started
[00.253](12) SIMULATOR: Tempsensor sim (#0) started
[00.253](13) SIMULATOR: Door sim (#4) started
[00.253](14) SIMULATOR: Door sim (#3) started
[00.253](15) SIMULATOR: Door sim (#2) started
[00.253](16) SIMULATOR: Tempsensor sim (#2) started
[00.253](17) SIMULATOR: Tempsensor sim (#3) started
[00.253](18) SIMULATOR: Tempsensor sim (#1) started
[00.253](19) SIMULATOR: Tempsensor sim (#4) started
[00.252](20) SIMULATOR: Cardreader sim (#4) started
[00.253](21) SIMULATOR: Destselect sim (#1) started
[00.253](22) SIMULATOR: Elevator sim (#1) started
[00.253](23) SIMULATOR: Destselect sim (#0) started
[00.253](24) SIMULATOR: Elevator sim (#0) started
[00.253](25) SIMULATOR: Destselect sim (#2) started
[00.254](26) SIMULATOR: Destselect sim (#3) started
[00.254](27) SIMULATOR: Destselect sim (#4) started
[00.254](28) SIMULATOR: Destselect sim (#5) started
[00.254](29) SIMULATOR: Camera sim (#2) started
[00.254](30) SIMULATOR: Camera sim (#1) started
[00.254](31) SIMULATOR: Destselect sim (#6) started
[00.254](32) SIMULATOR: Camera sim (#0) started
[00.255](33) SIMULATOR: Camera sim (#3) started
[00.255](34) SIMULATOR: Camera sim (#4) started
[00.255](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 512. Overseer addr: 127.0.0.1:4500
[00.255](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4500
[00.255](0) CARDREADER.103: Sending HELLO#
[00.255](2) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.255](2) OVERSEER: Got reg event from cardreader 103
[00.257](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 10. Detection period: 100000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4500
[00.257](0) FIREALARM: Binding addr 127.0.0.1:4501
[00.257](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4501 HELLO#
[00.257](2) OVERSEER: Registered fire alarm @127.0.0.1:4501
[00.258](0) CARDREADER.104: Starting up. Shm path: /shm. Offset: 672. Overseer addr: 127.0.0.1:4500
[00.258](0) CARDREADER.202: Starting up. Shm path: /shm. Offset: 992. Overseer addr: 127.0.0.1:4500
[00.258](0) CARDREADER.202: Attempting to connect to 127.0.0.1:4500
[00.259](0) CARDREADER.202: Sending HELLO#
[00.259](0) CARDREADER.101: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4500
[00.259](0) CARDREADER.101: Attempting to connect to 127.0.0.1:4500
[00.259](0) CARDREADER.101: Sending HELLO#
[00.259](0) CARDREADER.501: Starting up. Shm path: /shm. Offset: 1472. Overseer addr: 127.0.0.1:4500
[00.259](0) CARDREADER.501: Attempting to connect to 127.0.0.1:4500
[00.259](0) CARDREADER.501: Sending HELLO#
[00.259](0) CARDREADER.104: Attempting to connect to 127.0.0.1:4500
[00.259](0) CARDREADER.104: Sending HELLO#
[00.259](0) DESTSELECT.402: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50632. Overseer addr: 127.0.0.1:4500
[00.259](0) DESTSELECT.402: Attempting to connect to 127.0.0.1:4500
[00.259](0) DESTSELECT.402: Sending HELLO#
[00.260](0) TEMPSENSOR.104: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9760.
[00.260](0) TEMPSENSOR.104: Receiver #1: 127.0.0.1:4507
[00.260](0) TEMPSENSOR.104: Binding addr 127.0.0.1:4510
[00.260](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.260](0) CAMERA.55: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 20608. Overseer addr: 127.0.0.1:4500
[00.260](0) CAMERA.55: Binding addr 127.0.0.1:4518
[00.260](3) OVERSEER: Received message from client: CARDREADER 501 HELLO#
[00.260](3) OVERSEER: Got reg event from cardreader 501
[00.260](0) CARDREADER.201: Starting up. Shm path: /shm. Offset: 832. Overseer addr: 127.0.0.1:4500
[00.260](0) CARDREADER.201: Attempting to connect to 127.0.0.1:4500
[00.260](4) OVERSEER: Received message from client: DESTSELECT 402 HELLO#
[00.260](4) OVERSEER: Got reg event from destselect 402
[00.260](0) CARDREADER.201: Sending HELLO#
[00.261](0) TEMPSENSOR.105: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9856.
[00.261](0) TEMPSENSOR.105: Receiver #1: 127.0.0.1:4509
[00.261](0) TEMPSENSOR.105: Receiver #2: 127.0.0.1:4501
[00.261](0) TEMPSENSOR.105: Binding addr 127.0.0.1:4511
[00.261](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.261](0) CARDREADER.502: Starting up. Shm path: /shm. Offset: 1632. Overseer addr: 127.0.0.1:4500
[00.261](0) CARDREADER.502: Attempting to connect to 127.0.0.1:4500
[00.261](0) ELEVATOR.2: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53296. Overseer addr: 127.0.0.1:4500
[00.261](0) CARDREADER.502: Sending HELLO#
[00.261](0) ELEVATOR.2: Binding addr 127.0.0.1:4513
[00.262](0) TEMPSENSOR.103: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9664.
[00.262](0) CAMERA.33: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 16960. Overseer addr: 127.0.0.1:4500
[00.262](0) TEMPSENSOR.103: Receiver #1: 127.0.0.1:4508
[00.262](0) CAMERA.33: Binding addr 127.0.0.1:4516
[00.262](0) TEMPSENSOR.103: Binding addr 127.0.0.1:4509
[00.262](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.262](0) CAMERA.44: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 18784. Overseer addr: 127.0.0.1:4500
[00.262](0) TEMPSENSOR.101: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9472.
[00.262](0) TEMPSENSOR.101: Receiver #1: 127.0.0.1:4500
[00.262](0) TEMPSENSOR.101: Receiver #2: 127.0.0.1:4509
[00.262](0) CAMERA.44: Binding addr 127.0.0.1:4517
[00.262](0) TEMPSENSOR.101: Binding addr 127.0.0.1:4507
[00.262](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.262](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.262](0) DESTSELECT.202: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50296. Overseer addr: 127.0.0.1:4500
[00.262](0) DESTSELECT.202: Attempting to connect to 127.0.0.1:4500
[00.262](0) DESTSELECT.202: Sending HELLO#
[00.263](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.263](0) DESTSELECT.302: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50464. Overseer addr: 127.0.0.1:4500
[00.263](0) DESTSELECT.302: Attempting to connect to 127.0.0.1:4500
[00.263](0) DESTSELECT.302: Sending HELLO#
[00.263](0) DESTSELECT.502: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50800. Overseer addr: 127.0.0.1:4500
[00.263](0) DESTSELECT.502: Attempting to connect to 127.0.0.1:4500
[00.263](0) DESTSELECT.502: Sending HELLO#
[00.264](6) OVERSEER: Received message from client: DESTSELECT 202 HELLO#
[00.264](6) OVERSEER: Got reg event from destselect 202
[00.264](7) OVERSEER: Received message from client: DESTSELECT 502 HELLO#
[00.264](7) OVERSEER: Got reg event from destselect 502
[00.264](0) DESTSELECT.301: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 50128. Overseer addr: 127.0.0.1:4500
[00.265](0) DESTSELECT.301: Attempting to connect to 127.0.0.1:4500
[00.265](0) DESTSELECT.301: Sending HELLO#
[00.265](0) FIREALARM: Received temperature (22.00)
[00.265](0) TEMPSENSOR.102: Starting up. Condvar wait: 1000us. Update wait: 50000us. Shm path: /shm. Offset: 9568.
[00.265](0) TEMPSENSOR.102: Receiver #1: 127.0.0.1:4510
[00.265](0) TEMPSENSOR.102: Binding addr 127.0.0.1:4508
[00.265](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.265](8) OVERSEER: Received message from client: DOOR 501 127.0.0.1:4506 FAIL_SAFE#
[00.265](8) OVERSEER: Registered door #501 @127.0.0.1:4506 (FAIL_SAFE#)
[00.265](0) FIREALARM: Got door registration packet
[00.265](0) DESTSELECT.101: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49792. Overseer addr: 127.0.0.1:4500
[00.265](0) DESTSELECT.101: Attempting to connect to 127.0.0.1:4500
[00.265](0) DESTSELECT.101: Sending HELLO#
[00.266](9) OVERSEER: Received message from client: CAMERA 55 127.0.0.1:4518 HELLO#
[00.266](9) OVERSEER: Registered camera #55 @127.0.0.1:4518
[00.266](3) OVERSEER: Received message from client: CARDREADER 502 HELLO#
[00.266](3) OVERSEER: Got reg event from cardreader 502
[00.266](10) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4503 FAIL_SAFE#
[00.266](10) OVERSEER: Registered door #102 @127.0.0.1:4503 (FAIL_SAFE#)
[00.266](11) OVERSEER: Received message from client: CAMERA 33 127.0.0.1:4516 HELLO#
[00.266](11) OVERSEER: Registered camera #33 @127.0.0.1:4516
[00.266](0) CAMERA.11: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 13312. Overseer addr: 127.0.0.1:4500
[00.266](12) OVERSEER: Received message from client: CAMERA 44 127.0.0.1:4517 HELLO#
[00.266](12) OVERSEER: Registered camera #44 @127.0.0.1:4517
[00.266](0) CAMERA.11: Binding addr 127.0.0.1:4514
[00.266](1) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.266](1) OVERSEER: Got reg event from cardreader 101
[00.266](7) OVERSEER: Received message from client: DESTSELECT 301 HELLO#
[00.266](7) OVERSEER: Got reg event from destselect 301
[00.266](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.266](2) OVERSEER: Received message from client: CARDREADER 202 HELLO#
[00.266](2) OVERSEER: Got reg event from cardreader 202
[00.266](0) CAMERA.22: Starting up. Temperature threshold: 10.Shm path: /shm. Offset: 15136. Overseer addr: 127.0.0.1:4500
[00.266](13) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.266](13) OVERSEER: Got reg event from cardreader 104
[00.266](0) CAMERA.22: Binding addr 127.0.0.1:4515
[00.267](13) OVERSEER: Received message from client: CAMERA 22 127.0.0.1:4515 HELLO#
[00.267](13) OVERSEER: Registered camera #22 @127.0.0.1:4515
[00.267](0) CARDREADER.301: Starting up. Shm path: /shm. Offset: 1152. Overseer addr: 127.0.0.1:4500
[00.267](0) CARDREADER.301: Attempting to connect to 127.0.0.1:4500
[00.267](0) CARDREADER.301: Sending HELLO#
[00.267](0) DESTSELECT.201: Starting up. Wait time: 2500us. Shm path: /shm. Offset: 49960. Overseer addr: 127.0.0.1:4500
[00.267](0) DESTSELECT.201: Attempting to connect to 127.0.0.1:4500
[00.267](13) OVERSEER: Received message from client: CARDREADER 301 HELLO#
[00.267](13) OVERSEER: Got reg event from cardreader 301
[00.267](4) OVERSEER: Received message from client: CARDREADER 201 HELLO#
[00.267](4) OVERSEER: Got reg event from cardreader 201
[00.267](14) OVERSEER: Received message from client: ELEVATOR 2 127.0.0.1:4513 HELLO#
[00.267](14) OVERSEER: Registered elevator #2 @127.0.0.1:4513
[00.267](15) OVERSEER: Received message from client: DOOR 201 127.0.0.1:4504 FAIL_SAFE#
[00.267](15) OVERSEER: Registered door #201 @127.0.0.1:4504 (FAIL_SAFE#)
[00.267](0) FIREALARM: Got door registration packet
[00.267](16) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4502 FAIL_SAFE#
[00.267](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.267](16) OVERSEER: Registered door #101 @127.0.0.1:4502 (FAIL_SAFE#)
[00.267](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.267](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.267](0) FIREALARM: Got door registration packet
[00.267](17) OVERSEER: Received message from client: DESTSELECT 302 HELLO#
[00.267](17) OVERSEER: Got reg event from destselect 302
[00.267](18) OVERSEER: Received message from client: DOOR 301 127.0.0.1:4505 FAIL_SAFE#
[00.267](0) ELEVATOR.1: Starting up. Wait time: 2500us. Door open duration: 10000us. Shm path: /shm. Offset: 53152. Overseer addr: 127.0.0.1:4500
[00.267](18) OVERSEER: Registered door #301 @127.0.0.1:4505 (FAIL_SAFE#)
[00.267](0) FIREALARM: Got door registration packet
[00.267](0) ELEVATOR.1: Binding addr 127.0.0.1:4512
[00.267](0) FIREALARM: Got door registration packet
[00.267](12) OVERSEER: Received message from client: CAMERA 11 127.0.0.1:4514 HELLO#
[00.267](12) OVERSEER: Registered camera #11 @127.0.0.1:4514
[00.267](0) DESTSELECT.201: Sending HELLO#
[00.267](8) OVERSEER: Received message from client: DESTSELECT 101 HELLO#
[00.267](8) OVERSEER: Got reg event from destselect 101
[00.267](18) OVERSEER: Received message from client: ELEVATOR 1 127.0.0.1:4512 HELLO#
[00.267](18) OVERSEER: Registered elevator #1 @127.0.0.1:4512
[00.267](16) OVERSEER: Received message from client: DESTSELECT 201 HELLO#
[00.267](16) OVERSEER: Got reg event from destselect 201
[00.310](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.310](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.311](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.311](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.311](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.311](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.311](0) FIREALARM: Received temperature (22.00)
[00.312](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.312](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.313](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.313](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.313](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.313](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.313](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.314](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.314](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.314](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.314](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.315](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.315](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.315](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.315](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.315](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.316](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.316](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.316](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.361](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.362](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.362](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.362](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.362](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.362](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.362](0) FIREALARM: Received temperature (22.00)
[00.363](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.363](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.363](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.364](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.364](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.364](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.364](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.365](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.365](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.365](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.365](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.366](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.366](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.366](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.366](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.366](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.367](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.367](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.367](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.411](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.412](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.412](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.412](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.412](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.413](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.413](0) FIREALARM: Received temperature (22.00)
[00.414](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.414](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.414](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.414](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.414](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.415](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.415](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.416](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.416](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.416](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.416](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.417](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.417](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.417](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.417](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.417](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.418](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.418](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.418](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.462](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.463](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.463](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.463](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.463](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.464](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.464](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.464](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.464](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.464](0) FIREALARM: Received temperature (22.00)
[00.464](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.465](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.465](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.466](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.466](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.467](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.467](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.467](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.467](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.468](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.468](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.468](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.468](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.469](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.469](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.469](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.513](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.514](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.514](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.514](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.515](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.515](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.515](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.515](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.515](0) FIREALARM: Received temperature (22.00)
[00.516](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.516](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.516](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.517](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.517](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.518](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.518](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.518](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.519](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.519](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.519](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.520](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.520](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.520](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.520](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.521](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.521](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.564](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.565](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.565](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.565](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.565](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.566](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.566](0) FIREALARM: Received temperature (22.00)
[00.566](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.566](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.566](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.566](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.567](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.567](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.567](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.568](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.568](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.568](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.568](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.569](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.569](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.569](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.569](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.569](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.570](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.570](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.570](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.615](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.616](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.616](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.616](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.617](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.617](0) FIREALARM: Received temperature (22.00)
[00.617](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.617](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.617](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.617](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.617](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.618](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.618](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.619](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.619](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.619](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.620](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.620](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.620](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.621](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.621](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.621](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.621](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.621](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.622](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.622](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.666](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.666](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.666](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.666](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.667](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.667](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.667](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.668](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.668](0) FIREALARM: Received temperature (22.00)
[00.668](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.668](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.668](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.669](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.669](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.669](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.669](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.670](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.671](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.671](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.671](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.671](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.671](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.671](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.672](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.672](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.672](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.717](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.718](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.718](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.718](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.718](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.718](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.719](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.719](0) FIREALARM: Received temperature (22.00)
[00.719](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.719](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.719](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.720](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.720](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.721](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.721](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.721](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.721](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.722](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.722](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.722](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.722](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.722](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.723](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.723](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.723](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.723](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.768](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.769](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.769](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.769](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.769](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.769](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.770](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.770](0) FIREALARM: Received temperature (22.00)
[00.770](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.770](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.770](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.771](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.771](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.772](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.772](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.772](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.772](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.773](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.773](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.774](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.774](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.774](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.774](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.774](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.775](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.775](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.818](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.819](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.819](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.819](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.820](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.820](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.820](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.821](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.821](0) FIREALARM: Received temperature (22.00)
[00.821](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.821](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.821](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.822](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.822](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.823](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.823](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.823](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.824](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.824](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.824](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.825](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.825](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.825](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.825](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.826](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.826](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.868](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.869](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.869](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.869](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.869](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.871](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.871](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.871](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.871](0) FIREALARM: Received temperature (22.00)
[00.871](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.871](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.871](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.872](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.872](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.872](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.873](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.873](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.873](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.874](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.874](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.874](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.875](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.875](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.876](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.876](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.876](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.918](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.919](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.919](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.919](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.920](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.922](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.922](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.922](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.922](0) FIREALARM: Received temperature (22.00)
[00.922](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.922](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.922](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.923](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.923](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.923](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.924](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.924](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.924](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.924](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.925](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.925](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.926](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.926](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.927](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.927](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.927](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.968](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.969](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[00.969](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[00.969](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.970](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[00.972](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.972](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.973](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.973](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.973](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[00.973](0) FIREALARM: Received temperature (22.00)
[00.973](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[00.974](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[00.974](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[00.974](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[00.975](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[00.975](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.976](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[00.977](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[00.977](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.977](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[00.977](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.978](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[00.978](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[00.978](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[00.978](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.018](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.019](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[01.019](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[01.019](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.020](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[01.022](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.022](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.023](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[01.023](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[01.024](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.024](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.024](0) FIREALARM: Received temperature (22.00)
[01.024](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[01.025](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[01.025](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[01.026](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[01.026](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[01.026](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.027](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[01.027](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[01.027](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.028](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.029](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[01.030](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[01.030](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[01.030](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.069](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.070](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[01.070](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[01.070](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.071](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[01.072](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.072](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.073](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[01.073](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[01.075](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.075](0) FIREALARM: Received temperature (22.00)
[01.075](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.075](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[01.076](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[01.077](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[01.077](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[01.077](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[01.078](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.078](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[01.078](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.079](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[01.079](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.079](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[01.080](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[01.080](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[01.080](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.119](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.120](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[01.120](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[01.120](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.120](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[01.122](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.122](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.123](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[01.123](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[01.126](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.126](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.126](0) FIREALARM: Received temperature (22.00)
[01.126](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[01.127](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[01.128](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[01.128](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[01.129](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[01.129](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.129](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[01.129](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.130](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[01.130](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.130](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[01.131](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[01.131](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[01.131](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.169](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.170](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[01.170](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[01.170](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.170](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[01.172](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.172](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.173](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[01.173](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[01.176](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.177](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.177](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[01.177](0) FIREALARM: Received temperature (22.00)
[01.177](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[01.178](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[01.178](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[01.179](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[01.179](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.179](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[01.180](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[01.180](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.180](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.181](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[01.182](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[01.182](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4509
[01.182](5) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.220](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.221](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4500
[01.221](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:4509
[01.221](5) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.221](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:4508
[01.222](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.222](5) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.223](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:4508
[01.223](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:4510
[01.227](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.228](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.228](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:4510
[01.228](0) FIREALARM: Received temperature (22.00)
[01.228](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:4508
[01.229](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:4507
[01.229](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:4500
[01.229](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:4510
[01.229](5) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.230](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:4507
[01.230](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:4500
[01.230](5) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.231](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.232](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:4507
[01.232](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:4500
[01.232](0) TEMPSEN[...(truncated)...]ENSOR.104: Propagating update (103:28.83) to 127.0.0.1:4507
[02.191](0) TEMPSENSOR.101: Propagating update (104:26.62) to 127.0.0.1:4500
[02.191](0) TEMPSENSOR.101: Propagating update (104:26.62) to 127.0.0.1:4509
[02.191](5) OVERSEER: Received UDP TEMP packet: id=104 temp=26.62
[02.191](0) TEMPSENSOR.103: Propagating update (104:26.62) to 127.0.0.1:4508
[02.191](1) OVERSEER: Received CLOSING# from door
[02.192](13) SIMULATOR: Door sim (#4) woke up. Status = c
[02.192](15) SIMULATOR: Door sim (#2) changed status to = O
[02.192](0) TEMPSENSOR.101: Propagating update (103:28.83) to 127.0.0.1:4500
[02.192](5) OVERSEER: Received UDP TEMP packet: id=103 temp=28.83
[02.192](2) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.192](3) OVERSEER: Received CLOSING# from door
[02.192](10) SIMULATOR: Door sim (#0) woke up. Status = c
[02.193](13) SIMULATOR: Door sim (#4) changed status to = C
[02.193](1) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.193](10) SIMULATOR: Door sim (#0) changed status to = C
[02.193](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.193](30) SIMULATOR: Camera sim (#1) simulated motion (angle: 0, status: O)
[02.194](3) OVERSEER: Received message from client: CAMERA 22 MOTION#
[02.194](3) OVERSEER: Received motion event from camera #22
[02.198](24) SIMULATOR: Elevator sim (#0): Status is now C
[02.199](16) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.199](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.199](24) SIMULATOR: Elevator sim (#0): Status is now O
[02.199](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.200](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.200](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.200](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.201](19) SIMULATOR: Tempsensor sim (#4): temperature changed to 30.00
[02.201](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.201](0) FIREALARM: Received temperature (30.00)
[02.202](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.202](2) OVERSEER: Received CLOSING# from door
[02.202](15) SIMULATOR: Door sim (#2) woke up. Status = c
[02.203](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.203](20) SIMULATOR: Cardreader sim (#4): scanned code db4ed0a0bfbb00ac
[02.203](0) CARDREADER.201: Scanned code: db4ed0a0bfbb00ac - connecting to overseer
[02.203](3) OVERSEER: Received message from client: CARDREADER 201 SCANNED db4ed0a0bfbb00ac#
[02.203](3) OVERSEER: Got scan from cardreader 201: db4ed0a0bfbb00ac
[02.203](15) SIMULATOR: Door sim (#2) changed status to = C
[02.203](0) CARDREADER.201: Received response: ALLOWED#
[02.203](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.203](2) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.203](3) OVERSEER: Received OPENING# from door
[02.203](20) SIMULATOR: Cardreader sim (#4): response to scan: Y
[02.204](15) SIMULATOR: Door sim (#2) woke up. Status = o
[02.204](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.204](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.205](15) SIMULATOR: Door sim (#2) changed status to = O
[02.205](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.205](0) TEMPSENSOR.102: Temperature is 27.66 - sending update
[02.205](29) SIMULATOR: Camera sim (#2) simulated motion (angle: 0, status: O)
[02.205](2) OVERSEER: Received message from client: CAMERA 33 MOTION#
[02.205](2) OVERSEER: Received motion event from camera #33
[02.206](0) TEMPSENSOR.104: Propagating update (102:27.66) to 127.0.0.1:4507
[02.206](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4500
[02.206](0) TEMPSENSOR.101: Propagating update (102:27.66) to 127.0.0.1:4509
[02.206](5) OVERSEER: Received UDP TEMP packet: id=102 temp=27.66
[02.209](26) SIMULATOR: Destselect sim (#3): scanned code db4ed0a0bfbb00ac and floor 3
[02.209](0) DESTSELECT.202: Scanned code: db4ed0a0bfbb00ac and floor: 3 - connecting to overseer
[02.210](2) OVERSEER: Received message from client: DESTSELECT 202 SCANNED db4ed0a0bfbb00ac 3#
[02.210](2) OVERSEER: Got scan from destselect 202: db4ed0a0bfbb00ac, floor 3
[02.211](18) SIMULATOR: Tempsensor sim (#1): temperature changed to 28.13
[02.211](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.211](0) ELEVATOR.2: Received message: FROM 2 TO 3#
[02.212](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.212](0) DESTSELECT.202: Received response: ALLOWED#
[02.212](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.212](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.212](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.212](26) SIMULATOR: Destselect sim (#3): response to scan: Y
[02.213](24) SIMULATOR: Elevator sim (#0) moved from floor 3 to 2. Status is now C
[02.214](8) SIMULATOR: Cardreader sim (#9): scanned code 4b6f9c1d4d55506c
[02.214](0) CARDREADER.502: Scanned code: 4b6f9c1d4d55506c - connecting to overseer
[02.215](2) OVERSEER: Received message from client: CARDREADER 502 SCANNED 4b6f9c1d4d55506c#
[02.215](2) OVERSEER: Got scan from cardreader 502: 4b6f9c1d4d55506c
[02.215](0) CARDREADER.502: Received response: ALLOWED#
[02.215](15) SIMULATOR: Door sim (#2) woke up. Status = c
[02.215](3) OVERSEER: Received CLOSING# from door
[02.215](8) SIMULATOR: Cardreader sim (#9): response to scan: Y
[02.215](13) SIMULATOR: Door sim (#4) woke up. Status = o
[02.215](2) OVERSEER: Received OPENING# from door
[02.215](24) SIMULATOR: Elevator sim (#0) moved from floor 2 to 1
[02.216](15) SIMULATOR: Door sim (#2) changed status to = C
[02.216](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.216](13) SIMULATOR: Door sim (#4) changed status to = O
[02.216](2) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.216](24) SIMULATOR: Elevator sim (#0): Status is now O
[02.222](12) SIMULATOR: Tempsensor sim (#0): temperature changed to 26.77
[02.222](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.222](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.223](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.224](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.224](16) SIMULATOR: Tempsensor sim (#2): temperature changed to 30.00
[02.225](22) SIMULATOR: Elevator sim (#1) moved from floor 5 to 4. Status is now C
[02.225](1) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[02.225](0) CARDREADER.101: Scanned code: 2214a7ba5943d923 - connecting to overseer
[02.225](3) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[02.225](3) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[02.225](0) CARDREADER.101: Received response: ALLOWED#
[02.225](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[02.225](3) OVERSEER: Received OPENING# from door
[02.225](10) SIMULATOR: Door sim (#0) woke up. Status = o
[02.226](23) SIMULATOR: Destselect sim (#0): scanned code cae0efe252087308 and floor 3
[02.226](0) DESTSELECT.101: Scanned code: cae0efe252087308 and floor: 3 - connecting to overseer
[02.226](1) OVERSEER: Received message from client: DESTSELECT 101 SCANNED cae0efe252087308 3#
[02.226](1) OVERSEER: Got scan from destselect 101: cae0efe252087308, floor 3
[02.226](2) OVERSEER: Received CLOSING# from door
[02.226](13) SIMULATOR: Door sim (#4) woke up. Status = c
[02.226](10) SIMULATOR: Door sim (#0) changed status to = O
[02.226](3) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.227](9) SIMULATOR: Cardreader sim (#8): scanned code 4b6f9c1d4d55506c
[02.227](0) CARDREADER.501: Scanned code: 4b6f9c1d4d55506c - connecting to overseer
[02.227](0) ELEVATOR.1: Received message: FROM 1 TO 3#
[02.227](1) OVERSEER: Received message from client: CARDREADER 501 SCANNED 4b6f9c1d4d55506c#
[02.227](1) OVERSEER: Got scan from cardreader 501: 4b6f9c1d4d55506c
[02.227](0) CARDREADER.501: Received response: ALLOWED#
[02.227](9) SIMULATOR: Cardreader sim (#8): response to scan: Y
[02.227](13) SIMULATOR: Door sim (#4) changed status to = C
[02.227](2) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.227](13) SIMULATOR: Door sim (#4) woke up. Status = o
[02.227](1) OVERSEER: Received OPENING# from door
[02.227](22) SIMULATOR: Elevator sim (#1) moved from floor 4 to 3
[02.228](13) SIMULATOR: Door sim (#4) changed status to = O
[02.229](1) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.229](0) DESTSELECT.101: Received response: ALLOWED#
[02.229](23) SIMULATOR: Destselect sim (#0): response to scan: Y
[02.230](22) SIMULATOR: Elevator sim (#1) moved from floor 3 to 2
[02.231](33) SIMULATOR: Camera sim (#3) simulated motion (angle: 0, status: O)
[02.231](22) SIMULATOR: Elevator sim (#1): Status is now O
[02.231](2) OVERSEER: Received message from client: CAMERA 44 MOTION#
[02.231](2) OVERSEER: Received motion event from camera #44
[02.236](5) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[02.236](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[02.236](2) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[02.236](2) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[02.236](0) CARDREADER.103: Received response: ALLOWED#
[02.236](5) SIMULATOR: Cardreader sim (#2): response to scan: Y
[02.236](11) SIMULATOR: Door sim (#1) woke up. Status = o
[02.236](2) OVERSEER: Received OPENING# from door
[02.237](10) SIMULATOR: Door sim (#0) woke up. Status = c
[02.237](3) OVERSEER: Received CLOSING# from door
[02.237](11) SIMULATOR: Door sim (#1) changed status to = O
[02.237](2) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.238](10) SIMULATOR: Door sim (#0) changed status to = C
[02.238](3) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.238](24) SIMULATOR: Elevator sim (#0): Status is now C
[02.239](1) OVERSEER: Received CLOSING# from door
[02.239](13) SIMULATOR: Door sim (#4) woke up. Status = c
[02.239](17) SIMULATOR: Tempsensor sim (#3): temperature changed to 27.03
[02.239](24) SIMULATOR: Elevator sim (#0): Status is now O
[02.239](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.239](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.239](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.239](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.240](13) SIMULATOR: Door sim (#4) changed status to = C
[02.240](1) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.240](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.245](22) SIMULATOR: Elevator sim (#1) moved from floor 2 to 3. Status is now C
[02.246](22) SIMULATOR: Elevator sim (#1): Status is now O
[02.246](4) SIMULATOR: Cardreader sim (#6): scanned code cae0efe252087308
[02.246](0) CARDREADER.301: Scanned code: cae0efe252087308 - connecting to overseer
[02.246](1) OVERSEER: Received message from client: CARDREADER 301 SCANNED cae0efe252087308#
[02.246](1) OVERSEER: Got scan from cardreader 301: cae0efe252087308
[02.246](0) CARDREADER.301: Received response: ALLOWED#
[02.246](4) SIMULATOR: Cardreader sim (#6): response to scan: Y
[02.246](1) OVERSEER: Received OPENING# from door
[02.246](14) SIMULATOR: Door sim (#3) woke up. Status = o
[02.248](14) SIMULATOR: Door sim (#3) changed status to = O
[02.248](1) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.248](2) OVERSEER: Received CLOSING# from door
[02.248](11) SIMULATOR: Door sim (#1) woke up. Status = c
[02.249](11) SIMULATOR: Door sim (#1) changed status to = C
[02.249](2) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.250](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.250](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.251](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.251](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.251](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.252](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.252](0) FIREALARM: Received temperature (30.00)
[02.253](24) SIMULATOR: Elevator sim (#0) moved from floor 1 to 2. Status is now C
[02.253](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.254](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.254](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.254](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.254](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.255](24) SIMULATOR: Elevator sim (#0) moved from floor 2 to 3
[02.256](24) SIMULATOR: Elevator sim (#0): Status is now O
[02.258](1) OVERSEER: Received CLOSING# from door
[02.258](14) SIMULATOR: Door sim (#3) woke up. Status = c
[02.259](14) SIMULATOR: Door sim (#3) changed status to = C
[02.259](1) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.261](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.261](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.261](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.261](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.261](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.272](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.272](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.273](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.274](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.290](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.290](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.290](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.290](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.291](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.301](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.301](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.302](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.302](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.302](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.303](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.303](0) FIREALARM: Received temperature (30.00)
[02.304](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.305](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.305](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.305](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.305](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.312](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.312](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.312](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.312](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.313](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.323](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.323](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.324](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.325](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.341](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.341](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.341](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.341](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.342](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.352](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.352](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.353](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.353](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.353](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.354](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.354](0) FIREALARM: Received temperature (30.00)
[02.355](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.356](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.356](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.356](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.356](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.363](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.363](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.365](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.365](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.365](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.374](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.374](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.375](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.376](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.391](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.392](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.392](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.392](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.393](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.403](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.403](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.404](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.405](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.405](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.405](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.405](0) FIREALARM: Received temperature (30.00)
[02.406](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.406](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.407](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.408](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.408](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.414](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.414](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.416](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.416](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.416](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.425](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.425](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.426](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.427](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.442](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.443](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.443](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.443](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.444](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.453](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.453](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.454](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.455](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.455](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.456](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.456](0) FIREALARM: Received temperature (30.00)
[02.457](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.457](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.458](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.459](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.459](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.465](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.465](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.465](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.465](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.465](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.476](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.476](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.477](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.478](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.493](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.494](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.494](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.494](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.495](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.504](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.504](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.505](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.506](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.506](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.507](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.507](0) FIREALARM: Received temperature (30.00)
[02.508](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.508](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.509](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.510](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.510](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.516](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.516](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.518](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.518](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.518](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.526](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.526](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.527](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.528](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.543](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.543](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.543](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.543](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.544](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.555](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.555](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.556](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.556](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.556](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.558](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.558](0) FIREALARM: Received temperature (30.00)
[02.559](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.559](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.560](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.560](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.560](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.567](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.568](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.569](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.569](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.569](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.577](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.577](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.578](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.579](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.594](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.595](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.595](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.595](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.596](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.606](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.606](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.607](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.608](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.608](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.609](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.609](0) FIREALARM: Received temperature (30.00)
[02.609](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.609](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.610](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.611](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.611](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.618](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.618](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.620](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.620](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.620](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.628](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.628](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.629](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.630](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.645](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.646](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.646](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.646](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.647](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.657](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.657](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.658](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.659](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.659](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.660](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.660](0) FIREALARM: Received temperature (30.00)
[02.661](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.661](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.662](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.663](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.663](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.669](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.669](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.669](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.670](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.670](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.678](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.678](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.679](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.679](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.696](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.697](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.697](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.697](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.698](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.707](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.707](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.708](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.708](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.708](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.711](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.711](0) FIREALARM: Received temperature (30.00)
[02.711](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.711](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.712](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.713](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.713](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.720](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.720](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.722](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.722](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.722](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.729](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.729](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.730](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.730](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.747](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.747](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.747](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.747](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.748](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.758](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.758](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.759](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.759](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.759](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.762](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.762](0) FIREALARM: Received temperature (30.00)
[02.762](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.762](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.763](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.763](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.763](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.771](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.772](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.773](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.773](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.773](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.780](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.780](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.781](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.782](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.798](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.799](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.799](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.799](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.800](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.809](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.809](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.810](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.810](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.810](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.813](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.813](0) FIREALARM: Received temperature (30.00)
[02.813](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.813](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.814](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.814](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.814](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.822](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.822](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.823](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.823](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.823](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.831](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.831](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.832](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.832](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.849](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.849](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.849](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.849](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.850](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.860](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.860](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.861](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.861](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.861](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.864](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.864](0) FIREALARM: Received temperature (30.00)
[02.864](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.864](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.865](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.865](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.865](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.873](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.873](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.874](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.874](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.874](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.881](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.881](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.882](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.882](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.900](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.900](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.900](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.900](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.901](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.911](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.911](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.912](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.912](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.912](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.915](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.915](0) FIREALARM: Received temperature (30.00)
[02.915](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.915](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.916](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.916](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.916](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.924](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.924](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.925](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.925](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.925](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.931](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.931](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.932](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.932](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[02.951](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[02.951](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[02.951](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[02.951](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[02.952](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[02.961](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[02.961](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[02.962](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[02.962](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[02.962](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[02.966](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[02.966](0) FIREALARM: Received temperature (30.00)
[02.966](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[02.966](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[02.967](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[02.967](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[02.967](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[02.975](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[02.976](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[02.976](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[02.976](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[02.976](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[02.982](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[02.982](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[02.983](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[02.983](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.001](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.001](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[03.001](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[03.001](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.002](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[03.012](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.012](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[03.013](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[03.013](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[03.013](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.017](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.017](0) FIREALARM: Received temperature (30.00)
[03.017](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[03.017](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[03.018](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[03.018](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[03.018](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.025](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.026](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[03.026](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[03.026](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[03.026](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.033](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.033](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.034](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[03.034](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.052](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.052](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[03.052](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[03.052](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.053](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[03.063](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.063](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[03.064](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[03.064](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[03.064](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.068](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.068](0) FIREALARM: Received temperature (30.00)
[03.068](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[03.068](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[03.069](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[03.069](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[03.069](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.076](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.077](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[03.077](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[03.077](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[03.077](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.084](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.084](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.085](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[03.085](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.103](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.103](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[03.103](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[03.103](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.104](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[03.114](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.114](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[03.115](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[03.115](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[03.115](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.119](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.119](0) FIREALARM: Received temperature (30.00)
[03.119](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[03.119](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[03.120](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[03.120](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[03.120](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.127](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.128](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[03.128](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[03.128](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[03.128](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.135](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.135](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.136](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[03.136](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.154](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.154](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[03.154](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[03.154](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.155](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[03.165](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.165](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[03.166](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[03.166](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[03.166](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.170](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.170](0) FIREALARM: Received temperature (30.00)
[03.170](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[03.170](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[03.171](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[03.171](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[03.171](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.178](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.179](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[03.179](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[03.179](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[03.179](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.185](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.185](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.186](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[03.186](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.205](0) TEMPSENSOR.104: Temperature is 27.03 - sending update
[03.205](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4500
[03.205](0) TEMPSENSOR.101: Propagating update (104:27.03) to 127.0.0.1:4509
[03.205](5) OVERSEER: Received UDP TEMP packet: id=104 temp=27.03
[03.206](0) TEMPSENSOR.103: Propagating update (104:27.03) to 127.0.0.1:4508
[03.216](0) TEMPSENSOR.103: Temperature is 30.00 - sending update
[03.216](0) TEMPSENSOR.102: Propagating update (103:30.00) to 127.0.0.1:4510
[03.217](0) TEMPSENSOR.104: Propagating update (103:30.00) to 127.0.0.1:4507
[03.217](0) TEMPSENSOR.101: Propagating update (103:30.00) to 127.0.0.1:4500
[03.217](5) OVERSEER: Received UDP TEMP packet: id=103 temp=30.00
[03.221](0) TEMPSENSOR.105: Temperature is 30.00 - sending update
[03.221](0) FIREALARM: Received temperature (30.00)
[03.221](0) TEMPSENSOR.103: Propagating update (105:30.00) to 127.0.0.1:4508
[03.221](0) TEMPSENSOR.102: Propagating update (105:30.00) to 127.0.0.1:4510
[03.222](0) TEMPSENSOR.104: Propagating update (105:30.00) to 127.0.0.1:4507
[03.222](0) TEMPSENSOR.101: Propagating update (105:30.00) to 127.0.0.1:4500
[03.222](5) OVERSEER: Received UDP TEMP packet: id=105 temp=30.00
[03.229](0) TEMPSENSOR.102: Temperature is 28.13 - sending update
[03.230](0) TEMPSENSOR.104: Propagating update (102:28.13) to 127.0.0.1:4507
[03.230](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4500
[03.230](0) TEMPSENSOR.101: Propagating update (102:28.13) to 127.0.0.1:4509
[03.230](5) OVERSEER: Received UDP TEMP packet: id=102 temp=28.13
[03.236](0) TEMPSENSOR.101: Temperature is 26.77 - sending update
[03.236](5) OVERSEER: Received UDP TEMP packet: id=101 temp=26.77
[03.237](0) TEMPSENSOR.103: Propagating update (101:26.77) to 127.0.0.1:4508
[03.237](0) TEMPSENSOR.102: Propagating update (101:26.77) to 127.0.0.1:4510
[03.246](0) SIMULATOR: Simulation ended, shutting down
"""

door_1_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Cardreader sim (#2) started
[00.249](1) SIMULATOR: Cardreader sim (#3) started
[00.249](2) SIMULATOR: Cardreader sim (#0) started
[00.249](3) SIMULATOR: Cardreader sim (#1) started
[00.249](4) SIMULATOR: Door sim (#1) started
[00.249](5) SIMULATOR: Door sim (#0) started
[00.252](0) CARDREADER.104: Starting up. Shm path: /shm. Offset: 672. Overseer addr: 127.0.0.1:4300
[00.252](0) CARDREADER.104: Attempting to connect to 127.0.0.1:4300
[00.252](0) CARDREADER.104: Sending HELLO#
[00.252](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 512. Overseer addr: 127.0.0.1:4300
[00.252](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4300
[00.252](0) CARDREADER.103: Sending HELLO#
[00.253](0) CARDREADER.101: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4300
[00.253](0) CARDREADER.101: Attempting to connect to 127.0.0.1:4300
[00.253](0) CARDREADER.102: Starting up. Shm path: /shm. Offset: 352. Overseer addr: 127.0.0.1:4300
[00.253](0) CARDREADER.102: Attempting to connect to 127.0.0.1:4300
[00.253](0) CARDREADER.102: Sending HELLO#
[00.253](0) CARDREADER.101: Sending HELLO#
[00.253](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4301 FAIL_SAFE#
[00.253](2) OVERSEER: Received message from client: CARDREADER 104 HELLO#
[00.253](3) OVERSEER: Received message from client: CARDREADER 101 HELLO#
[00.253](2) OVERSEER: Got reg event from cardreader 104
[00.253](3) OVERSEER: Got reg event from cardreader 101
[00.253](4) OVERSEER: Received message from client: CARDREADER 102 HELLO#
[00.253](4) OVERSEER: Got reg event from cardreader 102
[00.253](5) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.253](5) OVERSEER: Got reg event from cardreader 103
[00.253](1) OVERSEER: Registered door #101 @127.0.0.1:4301 (FAIL_SAFE#)
[00.253](6) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4302 FAIL_SECURE#
[00.253](6) OVERSEER: Registered door #102 @127.0.0.1:4302 (FAIL_SECURE#)
[01.298](6) SIMULATOR: Simulated input to overseer: DOOR LIST
101 127.0.0.1:4301 FAIL_SAFE
102 127.0.0.1:4302 FAIL_SECURE
[01.348](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 102
[01.348](2) SIMULATOR: Cardreader sim (#0): scanned code db4ed0a0bfbb00ac
[01.348](0) CARDREADER.101: Scanned code: db4ed0a0bfbb00ac - connecting to overseer
[01.348](4) SIMULATOR: Door sim (#1) woke up. Status = o
[01.348](6) OVERSEER: Received message from client: CARDREADER 101 SCANNED db4ed0a0bfbb00ac#
[01.348](6) OVERSEER: Got scan from cardreader 101: db4ed0a0bfbb00ac
[01.349](0) CARDREADER.101: Received response: ALLOWED#
[01.349](2) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.349](6) OVERSEER: Received OPENING# from door
[01.349](5) SIMULATOR: Door sim (#0) woke up. Status = o
[01.358](4) SIMULATOR: Door sim (#1) changed status to = O
[01.359](5) SIMULATOR: Door sim (#0) changed status to = O
[01.359](6) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.448](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 102
[01.448](4) SIMULATOR: Door sim (#1) woke up. Status = c
[01.458](4) SIMULATOR: Door sim (#1) changed status to = C
[01.459](6) OVERSEER: Received CLOSING# from door
[01.459](5) SIMULATOR: Door sim (#0) woke up. Status = c
[01.469](5) SIMULATOR: Door sim (#0) changed status to = C
[01.469](6) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[01.548](2) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.548](0) CARDREADER.101: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.548](6) OVERSEER: Received message from client: CARDREADER 101 SCANNED 2214a7ba5943d923#
[01.548](6) OVERSEER: Got scan from cardreader 101: 2214a7ba5943d923
[01.549](0) CARDREADER.101: Received response: ALLOWED#
[01.549](2) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](6) OVERSEER: Received OPENING# from door
[01.549](5) SIMULATOR: Door sim (#0) woke up. Status = o
[01.559](5) SIMULATOR: Door sim (#0) changed status to = O
[01.559](6) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.568](6) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.568](5) SIMULATOR: Door sim (#0) woke up. Status = c
[01.578](5) SIMULATOR: Door sim (#0) changed status to = C
[01.659](6) OVERSEER: Received ALREADY# from door
[01.748](0) SIMULATOR: Cardreader sim (#2): scanned code db4ed0a0bfbb00ac
[01.748](0) CARDREADER.103: Scanned code: db4ed0a0bfbb00ac - connecting to overseer
[01.748](6) OVERSEER: Received message from client: CARDREADER 103 SCANNED db4ed0a0bfbb00ac#
[01.748](6) OVERSEER: Got scan from cardreader 103: db4ed0a0bfbb00ac
[01.749](0) CARDREADER.103: Received response: DENIED#
[01.749](0) SIMULATOR: Cardreader sim (#2): response to scan: N
[01.948](0) SIMULATOR: Cardreader sim (#2): scanned code 2214a7ba5943d923
[01.948](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.948](6) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.948](6) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.948](0) CARDREADER.103: Received response: ALLOWED#
[01.949](0) SIMULATOR: Cardreader sim (#2): response to scan: Y
[01.949](6) OVERSEER: Received OPENING# from door
[01.949](4) SIMULATOR: Door sim (#1) woke up. Status = o
[01.959](4) SIMULATOR: Door sim (#1) changed status to = O
[01.959](6) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.048](6) SIMULATOR: Simulated input to overseer: DOOR OPEN 101
[02.048](5) SIMULATOR: Door sim (#0) woke up. Status = o
[02.058](5) SIMULATOR: Door sim (#0) changed status to = O
[02.059](6) OVERSEER: Received CLOSING# from door
[02.059](4) SIMULATOR: Door sim (#1) woke up. Status = c
[02.069](4) SIMULATOR: Door sim (#1) changed status to = C
[02.069](6) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.148](1) SIMULATOR: Cardreader sim (#3): scanned code 2214a7ba5943d923
[02.148](0) CARDREADER.104: Scanned code: 2214a7ba5943d923 - connecting to overseer
[02.148](6) OVERSEER: Received message from client: CARDREADER 104 SCANNED 2214a7ba5943d923#
[02.148](6) OVERSEER: Got scan from cardreader 104: 2214a7ba5943d923
[02.148](0) CARDREADER.104: Received response: ALLOWED#
[02.149](1) SIMULATOR: Cardreader sim (#3): response to scan: Y
[02.149](6) OVERSEER: Received OPENING# from door
[02.149](4) SIMULATOR: Door sim (#1) woke up. Status = o
[02.159](4) SIMULATOR: Door sim (#1) changed status to = O
[02.159](6) OVERSEER: Received OPENED# from door (should be OPENED#)
[02.259](6) OVERSEER: Received CLOSING# from door
[02.259](4) SIMULATOR: Door sim (#1) woke up. Status = c
[02.269](4) SIMULATOR: Door sim (#1) changed status to = C
[02.269](6) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[03.148](6) SIMULATOR: Simulation ended, shutting down
"""

door_2_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.247](0) SIMULATOR: Launching firealarm
[00.248](1) SIMULATOR: Cardreader sim (#0) started
[00.248](2) SIMULATOR: Door sim (#1) started
[00.248](3) SIMULATOR: Door sim (#0) started
[00.250](1) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4403 FAIL_SECURE#
[00.250](1) OVERSEER: Registered door #102 @127.0.0.1:4403 (FAIL_SECURE#)
[00.251](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4402 FAIL_SAFE#
[00.251](1) OVERSEER: Registered door #101 @127.0.0.1:4402 (FAIL_SAFE#)
[00.251](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 3. Detection period: 20000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4400
[00.251](0) FIREALARM: Binding addr 127.0.0.1:4401
[00.251](1) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4401 HELLO#
[00.251](1) OVERSEER: Registered fire alarm @127.0.0.1:4401
[00.251](2) OVERSEER: Sending packet to 127.0.0.1:4402
[00.251](0) FIREALARM: Got door registration packet
[00.252](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4400
[00.253](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4400
[00.253](0) CARDREADER.103: Sending HELLO#
[00.253](1) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.253](1) OVERSEER: Got reg event from cardreader 103
[01.397](0) SIMULATOR: Simulated input to overseer: FIRE ALARM
Fire alarm triggered!
[01.398](0) FIREALARM: Fire alarm activated!
[01.398](0) FIREALARM: Contacting door #0 @ 127.0.0.1:4402
[01.398](4) SIMULATOR: Security alarm has been triggered.
[01.398](0) FIREALARM: Got reply: 
[01.398](3) SIMULATOR: Door sim (#0) woke up. Status = o
[01.408](3) SIMULATOR: Door sim (#0) changed status to = O
[01.447](0) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
Door reports that it open due to an emergency and cannot be closed
[01.548](1) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.548](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.548](2) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.548](2) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.548](0) CARDREADER.103: Received response: ALLOWED#
[01.548](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.548](2) OVERSEER: Received OPENING# from door
[01.548](2) SIMULATOR: Door sim (#1) woke up. Status = o
[01.558](2) SIMULATOR: Door sim (#1) changed status to = O
[01.558](2) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.658](2) OVERSEER: Received CLOSING# from door
[01.658](2) SIMULATOR: Door sim (#1) woke up. Status = c
[01.668](2) SIMULATOR: Door sim (#1) changed status to = C
[01.668](2) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.547](0) SIMULATOR: Simulation ended, shutting down
"""

door_3_submission = """

"""

callpoint_1_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.248](0) SIMULATOR: Launching callpoint
[00.248](1) SIMULATOR: Door sim (#1) started
[00.248](2) SIMULATOR: Callpoint sim (#0) started
[00.248](3) SIMULATOR: Door sim (#0) started
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4600
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4600
[00.251](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 1. Detection period: 1000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4600
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4603
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4602
[00.251](0) FIREALARM: Binding addr 127.0.0.1:4601
[00.251](1) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4603 FAIL_SECURE#
[00.251](1) OVERSEER: Registered door #102 @127.0.0.1:4603 (FAIL_SECURE#)
[00.251](2) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4602 FAIL_SAFE#
[00.251](2) OVERSEER: Registered door #101 @127.0.0.1:4602 (FAIL_SAFE#)
[00.251](3) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4601 HELLO#
[00.251](3) OVERSEER: Registered fire alarm @127.0.0.1:4601
[00.251](4) OVERSEER: Sending packet to 127.0.0.1:4602
[00.251](0) FIREALARM: Got door registration packet
[01.258](2) SIMULATOR: Callpoint sim (#0) was triggered
[01.258](0) FIREALARM: Fire alarm activated!
[01.258](0) FIREALARM: Contacting door #0 @ 127.0.0.1:4602
[01.258](4) SIMULATOR: Security alarm has been triggered.
[01.258](0) FIREALARM: Got reply: 
[01.258](0) DOOR.101: Received message: OPEN_EMERG#
[01.258](0) DOOR.101: Current status: C
[01.258](0) DOOR.101: OPENING# (emergency)
[01.258](3) SIMULATOR: Door sim (#0) woke up. Status = o
[01.269](3) SIMULATOR: Door sim (#0) changed status to = O
[01.269](0) DOOR.101: OPENED# (emergency)
[02.258](0) SIMULATOR: Simulation ended, shutting down
"""

callpoint_1_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.249](0) SIMULATOR: Launching callpoint
[00.249](0) SIMULATOR: Launching firealarm
[00.249](1) SIMULATOR: Callpoint sim (#0) started
[00.249](2) SIMULATOR: Door sim (#1) started
[00.249](3) SIMULATOR: Door sim (#0) started
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4600
[00.251](0) FIREALARM: Starting up. Temperature threshold: 50.00. Min detections: 1. Detection period: 1000us. Shm path: /shm. Offset: 0. Overseer addr: 127.0.0.1:4600
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4600
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4603
[00.251](0) FIREALARM: Binding addr 127.0.0.1:4601
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4602
[00.251](1) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4603 FAIL_SECURE#
[00.251](1) OVERSEER: Registered door #102 @127.0.0.1:4603 (FAIL_SECURE#)
[00.251](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4601 HELLO#
[00.251](2) OVERSEER: Registered fire alarm @127.0.0.1:4601
[00.251](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4602 FAIL_SAFE#
[00.251](1) OVERSEER: Registered door #101 @127.0.0.1:4602 (FAIL_SAFE#)
[00.251](0) FIREALARM: Got door registration packet
[01.259](1) SIMULATOR: Callpoint sim (#0) was triggered
[01.259](0) FIREALARM: Fire alarm activated!
[01.259](0) FIREALARM: Contacting door #0 @ 127.0.0.1:4602
[01.259](4) SIMULATOR: Security alarm has been triggered.
[01.259](0) FIREALARM: Got reply: 
[01.259](0) DOOR.101: Received message: OPEN_EMERG#
[01.259](0) DOOR.101: Current status: C
[01.259](0) DOOR.101: OPENING# (emergency)
[01.259](3) SIMULATOR: Door sim (#0) woke up. Status = o
[01.269](3) SIMULATOR: Door sim (#0) changed status to = O
[01.269](0) DOOR.101: OPENED# (emergency)
[02.259](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_3_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.249](1) SIMULATOR: Tempsensor sim (#1) started
[00.249](2) SIMULATOR: Tempsensor sim (#2) started
[00.249](3) SIMULATOR: Tempsensor sim (#6) started
[00.249](4) SIMULATOR: Tempsensor sim (#3) started
[00.249](5) SIMULATOR: Door sim (#0) started
[00.249](6) SIMULATOR: Tempsensor sim (#5) started
[00.249](7) SIMULATOR: Tempsensor sim (#0) started
[00.249](8) SIMULATOR: Tempsensor sim (#4) started
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:5000
[00.251](0) DOOR.101: Binding addr 127.0.0.1:5002
[00.251](0) TEMPSENSOR.106: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9952.
[00.252](0) TEMPSENSOR.106: Receiver #1: 127.0.0.1:5005
[00.252](0) TEMPSENSOR.106: Receiver #2: 127.0.0.1:5006
[00.252](0) TEMPSENSOR.106: Receiver #3: 127.0.0.1:5007
[00.252](0) TEMPSENSOR.106: Receiver #4: 127.0.0.1:5009
[00.252](0) TEMPSENSOR.105: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9856.
[00.252](0) TEMPSENSOR.105: Receiver #1: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.106: Binding addr 127.0.0.1:5008
[00.252](0) TEMPSENSOR.102: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9568.
[00.252](0) TEMPSENSOR.105: Receiver #2: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.102: Receiver #1: 127.0.0.1:5003
[00.252](0) TEMPSENSOR.102: Receiver #2: 127.0.0.1:5005
[00.252](0) TEMPSENSOR.102: Receiver #3: 127.0.0.1:5006
[00.252](0) TEMPSENSOR.105: Binding addr 127.0.0.1:5007
[00.252](0) TEMPSENSOR.107: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 10048.
[00.252](0) TEMPSENSOR.102: Receiver #4: 127.0.0.1:5007
[00.252](0) TEMPSENSOR.107: Receiver #1: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.107: Receiver #2: 127.0.0.1:5001
[00.252](0) TEMPSENSOR.102: Binding addr 127.0.0.1:5004
[00.252](0) TEMPSENSOR.107: Binding addr 127.0.0.1:5009
[00.252](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[00.252](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.252](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:5002 FAIL_SAFE#
[00.252](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[00.252](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[00.252](1) OVERSEER: Registered door #101 @127.0.0.1:5002 (FAIL_SAFE#)
[00.252](0) TEMPSENSOR.103: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9664.
[00.252](0) TEMPSENSOR.103: Receiver #1: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.103: Receiver #2: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.103: Binding addr 127.0.0.1:5005
[00.252](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.252](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:5001 HELLO#
[00.252](2) OVERSEER: Registered fire alarm @127.0.0.1:5001
[00.252](0) TEMPSENSOR.101: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9472.
[00.252](0) TEMPSENSOR.101: Receiver #1: 127.0.0.1:5000
[00.252](0) TEMPSENSOR.101: Receiver #2: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.101: Binding addr 127.0.0.1:5003
[00.252](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.252](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.253](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.253](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.253](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.253](0) TEMPSENSOR.105: Propagating update (102:22.00) to 127.0.0.1:5008
[00.253](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.253](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.253](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.253](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.253](0) TEMPSENSOR.104: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9760.
[00.253](0) TEMPSENSOR.104: Receiver #1: 127.0.0.1:5004
[00.253](0) TEMPSENSOR.104: Receiver #2: 127.0.0.1:5008
[00.253](0) TEMPSENSOR.104: Binding addr 127.0.0.1:5006
[00.253](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.253](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[00.254](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.254](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[00.254](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5008
[00.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[00.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[00.254](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[00.254](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[00.254](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[00.254](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[00.254](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[00.255](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[00.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.255](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.255](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.255](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.255](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[00.255](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[00.256](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.256](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.256](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.256](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[00.256](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.256](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.256](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.256](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.256](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.256](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[00.256](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[00.257](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.257](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.257](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.257](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[00.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.258](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.258](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.258](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.258](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[00.258](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.258](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.258](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.258](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.258](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.259](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[00.259](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.259](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.259](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.259](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[00.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.259](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.259](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.259](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.260](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.260](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.260](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.260](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.260](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.261](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.261](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.261](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.261](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.261](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.261](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.261](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.261](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.262](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.262](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.262](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.262](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.262](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.263](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.263](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.263](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.263](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.263](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.264](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.264](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.264](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.264](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.264](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.264](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.264](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.752](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[00.753](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[00.753](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[00.753](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.105: Propagating update (102:22.00) to 127.0.0.1:5008
[00.753](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.103: Propagating update (102:22.00) to 127.0.0.1:5008
[00.753](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[00.753](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:5000
[00.753](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.753](3) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.753](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.754](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:5008
[00.754](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.754](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.754](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.754](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[00.754](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[00.755](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.755](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.755](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.755](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[00.755](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.755](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.755](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.755](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.755](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.755](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.755](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[00.755](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[00.756](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.756](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.756](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.756](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[00.756](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[00.756](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[00.756](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[00.756](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.756](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.756](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.756](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5008
[00.756](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5008
[00.757](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.757](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5008
[00.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.757](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[00.757](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[00.758](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.758](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.758](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.758](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5004
[00.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[00.758](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.758](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[00.758](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.758](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[00.759](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.759](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.759](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.759](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5008
[00.759](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.759](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.759](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.759](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[00.759](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[00.760](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.760](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.760](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.760](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.760](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.760](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[00.760](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.760](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[00.761](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[00.761](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.761](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.761](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.761](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[00.761](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[00.761](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.761](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.761](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.761](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.761](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.762](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.762](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.762](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.762](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[00.762](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.762](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.762](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.762](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.762](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.763](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[00.763](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.763](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.763](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.763](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.763](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.763](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.764](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.764](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.764](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.765](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.765](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.765](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.765](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.765](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.765](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.765](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.766](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.766](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.766](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.766](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.766](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.766](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.766](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.767](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.767](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.767](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.767](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.767](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.767](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.767](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.767](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.768](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.768](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.768](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.768](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.768](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.768](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.769](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.769](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.769](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.769](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.769](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.769](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.770](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.770](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.770](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.770](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.770](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.771](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.771](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.253](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[01.253](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[01.253](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[01.253](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.253](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.253](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.254](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.254](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[01.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[01.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[01.254](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[01.254](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.254](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:5008
[01.254](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.254](0) TEMPSENSOR.105: Propagating update (102:22.00) to 127.0.0.1:5008
[01.254](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:5000
[01.254](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.254](3) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.254](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.254](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[01.255](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[01.255](0) TEMPSENSOR.103: Propagating update (102:22.00) to 127.0.0.1:5008
[01.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[01.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[01.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.255](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.255](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[01.255](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.255](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.256](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[01.256](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[01.256](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.256](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.256](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5008
[01.256](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[01.257](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.257](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.257](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.257](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[01.257](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[01.257](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[01.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.257](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.257](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.258](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5004
[01.258](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[01.258](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.258](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.258](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5008
[01.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[01.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[01.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.258](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.259](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5008
[01.259](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.259](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.259](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.259](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.259](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.259](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[01.259](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[01.259](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[01.259](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.259](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.260](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[01.260](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[01.260](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.260](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.260](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[01.260](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[01.260](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.261](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.261](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5008
[01.261](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.261](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.261](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[01.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[01.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[01.261](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[01.261](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.262](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.262](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.262](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.262](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.262](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[01.262](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[01.262](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[01.262](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.263](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.263](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[01.263](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.263](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.263](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[01.263](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.263](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[01.263](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[01.263](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[01.263](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.264](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.264](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[01.264](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[01.264](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.264](3) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.264](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.264](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[01.264](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[01.265](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.265](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.265](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.265](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.265](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[01.265](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.265](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[01.266](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.266](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.266](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.266](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.266](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.266](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.266](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[01.267](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.267](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.267](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.267](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.267](3) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.268](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.268](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[01.268](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.268](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.268](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.268](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.268](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.268](3) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.269](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.269](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.269](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.269](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.269](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.269](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.269](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.269](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.270](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.270](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.270](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.270](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.270](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.270](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.270](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.271](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.348](2) SIMULATOR: Tempsensor sim (#2): temperature changed to 33.50
[01.349](0) TEMPSENSOR.103: Temperature is 33.50 - sending update
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.350](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.350](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.350](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.350](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5008
[01.350](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5008
[01.350](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.350](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.351](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.351](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.351](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.351](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5004
[01.351](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5004
[01.351](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.351](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.352](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.352](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.352](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.352](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.352](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.352](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.352](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.353](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.353](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.353](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.398](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 103:33.50 104:22.00 105:22.00 107:22.00 102:22.00 106:22.00 
[01.448](1) SIMULATOR: Tempsensor sim (#1): temperature changed to 31.70
[01.448](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[01.449](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[01.449](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[01.449](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[01.449](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[01.449](3) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.451](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.452](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.453](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.498](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 103:33.50 104:22.00 105:22.00 107:22.00 102:31.70 106:22.00 
[01.548](3) SIMULATOR: Tempsensor sim (#6): temperature changed to 25.40
[01.548](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[01.549](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[01.549](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[01.549](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.549](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[01.549](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[01.550](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[01.550](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.550](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[01.551](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.551](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[01.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[01.552](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.552](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.598](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 103:33.50 104:22.00 105:22.00 107:25.40 102:31.70 106:22.00 
[01.648](8) SIMULATOR: Tempsensor sim (#4): temperature changed to 29.10
[01.648](0) TEMPSENSOR.105: Temperature is 29.10 - sending update
[01.649](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.649](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5005
[01.649](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5006
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5005
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5006
[01.649](0) TEMPSENSOR.104: Propagating update (105:29.10) to 127.0.0.1:5008
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.649](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.649](3) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.649](0) TEMPSENSOR.103: Propagating update (105:29.10) to 127.0.0.1:5008
[01.650](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.650](0) TEMPSENSOR.104: Propagating update (105:29.10) to 127.0.0.1:5004
[01.650](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5005
[01.650](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.650](0) TEMPSENSOR.103: Propagating update (105:29.10) to 127.0.0.1:5004
[01.651](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.651](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5005
[01.651](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.651](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5006
[01.651](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.651](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.651](3) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.652](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.652](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5006
[01.652](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.653](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.653](3) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.748](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 103:33.50 104:22.00 105:29.10 107:25.40 102:31.70 106:22.00 
[01.753](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[01.753](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[01.753](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[01.754](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.754](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.754](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.754](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[01.754](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[01.754](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.754](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.755](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.755](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.755](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.755](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.755](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.755](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.755](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.755](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.756](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.756](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.756](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[01.756](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.756](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.757](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.757](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.757](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.758](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[01.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[01.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[01.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[01.758](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[01.758](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.758](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[01.758](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.759](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[01.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.759](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.760](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.760](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.760](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.760](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.760](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.760](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.761](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.761](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.761](3) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.761](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.761](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.763](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.764](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.849](0) TEMPSENSOR.103: Temperature is 33.50 - sending update
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.849](2) SIMULATOR: Tempsensor sim (#2): temperature changed to 53.10
[01.849](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[01.850](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.850](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.850](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.850](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.850](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.850](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5008
[01.850](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5008
[01.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[01.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[01.850](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.850](4) SIMULATOR: Tempsensor sim (#3): temperature changed to 56.20
[01.850](0) TEMPSENSOR.104: Temperature is 56.20 - sending update
[01.850](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5004
[01.851](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[01.851](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.851](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[01.851](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.851](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.851](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5004
[01.851](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.851](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[01.851](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[01.851](8) SIMULATOR: Tempsensor sim (#4): temperature changed to 58.40
[01.851](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.851](0) TEMPSENSOR.105: Temperature is 58.40 - sending update
[01.851](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5008
[01.852](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5008
[01.852](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5008
[01.852](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.852](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.852](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.852](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.852](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.853](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.853](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.853](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5004
[01.853](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5004
[01.853](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.853](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.853](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.853](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.854](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.854](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.854](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.854](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5008
[01.854](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.854](3) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.854](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[01.854](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[01.854](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.855](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[01.855](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5004
[01.855](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.855](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.855](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[01.855](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[01.855](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.856](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.856](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.856](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[01.856](9) SIMULATOR: Security alarm has been triggered.
[01.856](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5008
[01.856](0) DOOR.101: Received message: OPEN_EMERG#
[01.856](0) DOOR.101: Current status: C
[01.856](0) DOOR.101: OPENING# (emergency)
[01.856](5) SIMULATOR: Door sim (#0) woke up. Status = o
[01.856](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5008
[01.856](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.856](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.856](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[01.856](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.857](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.857](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5004
[01.857](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.857](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[01.857](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5004
[01.857](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5004
[01.857](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.857](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.857](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[01.857](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.858](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.858](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.858](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[01.858](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.858](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.858](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[01.858](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.858](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 103:53.10 104:56.20 105:58.40 107:25.40 102:31.70 106:22.00 
[01.859](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.859](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.859](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[01.859](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.859](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.859](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[01.859](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.860](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.860](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.860](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[01.860](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.860](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.861](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[01.861](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.861](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.861](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.861](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[01.861](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.861](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.862](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[01.862](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.862](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.866](5) SIMULATOR: Door sim (#0) changed status to = O
[01.866](0) DOOR.101: OPENED# (emergency)
[01.949](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[01.949](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[01.949](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[01.950](3) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[01.950](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.950](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.950](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.950](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.950](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[01.950](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.951](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.952](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.049](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[02.050](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[02.050](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[02.050](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[02.051](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[02.051](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[02.051](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.052](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.052](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.053](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.053](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.053](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.053](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.053](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.054](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.054](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.054](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.054](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.054](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.254](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[02.254](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[02.255](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.255](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.255](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[02.255](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.255](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.256](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[02.256](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.256](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[02.256](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.257](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.257](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.257](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.257](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.257](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.258](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[02.258](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[02.258](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[02.258](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[02.258](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.258](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.258](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.258](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[02.259](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.259](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[02.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.259](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.260](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.260](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.261](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.350](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[02.351](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.351](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.351](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.351](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.351](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.351](0) TEMPSENSOR.104: Temperature is 56.20 - sending update
[02.351](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[02.351](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5008
[02.351](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[02.351](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5008
[02.351](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.352](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.352](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.352](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[02.352](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[02.352](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.352](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.352](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5004
[02.352](0) TEMPSENSOR.105: Temperature is 58.40 - sending update
[02.352](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[02.352](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5004
[02.353](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[02.353](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.353](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5008
[02.353](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.353](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.353](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.353](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.353](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.354](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5008
[02.354](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[02.354](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.354](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5004
[02.354](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.355](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.355](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[02.355](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[02.355](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.355](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.355](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5004
[02.355](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[02.355](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.355](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5008
[02.355](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.356](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.356](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.356](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5008
[02.356](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[02.356](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[02.356](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.356](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5004
[02.356](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.357](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.357](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.357](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[02.357](3) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.357](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[02.357](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.357](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.358](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.358](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.358](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.358](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[02.358](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5004
[02.358](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[02.358](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.358](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.359](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.359](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.359](3) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.359](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[02.359](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[02.359](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.360](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.360](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.360](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.360](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.360](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[02.360](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[02.360](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.361](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.361](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.361](3) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.450](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[02.450](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[02.450](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[02.450](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[02.450](3) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[02.451](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.452](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.453](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.453](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[02.453](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[02.453](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.454](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.550](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[02.551](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[02.551](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[02.551](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[02.551](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[02.551](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[02.551](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.552](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.552](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.553](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.553](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.554](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.554](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.554](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.554](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.554](3) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.754](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[02.754](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[02.755](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[02.755](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[02.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.755](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.755](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[02.755](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.755](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.756](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[02.756](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.756](3) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[02.756](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.757](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.757](3) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[02.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[02.758](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[02.758](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[02.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.759](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[02.759](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.759](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[02.759](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.759](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.759](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.760](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.761](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.851](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[02.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.851](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_3_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.248](0) SIMULATOR: Launching tempsensor
[00.249](0) SIMULATOR: Launching tempsensor
[00.249](1) SIMULATOR: Door sim (#0) started
[00.249](2) SIMULATOR: Tempsensor sim (#0) started
[00.249](3) SIMULATOR: Tempsensor sim (#1) started
[00.249](4) SIMULATOR: Tempsensor sim (#2) started
[00.249](5) SIMULATOR: Tempsensor sim (#3) started
[00.249](6) SIMULATOR: Tempsensor sim (#4) started
[00.249](7) SIMULATOR: Tempsensor sim (#5) started
[00.250](0) SIMULATOR: Launching tempsensor
[00.250](8) SIMULATOR: Tempsensor sim (#6) started
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:5000
[00.251](0) DOOR.101: Binding addr 127.0.0.1:5002
[00.251](0) TEMPSENSOR.101: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9472.
[00.251](1) OVERSEER: Received message from client: DOOR 101 127.0.0.1:5002 FAIL_SAFE#
[00.251](0) TEMPSENSOR.101: Receiver #1: 127.0.0.1:5000
[00.251](0) TEMPSENSOR.101: Receiver #2: 127.0.0.1:5004
[00.251](0) TEMPSENSOR.101: Binding addr 127.0.0.1:5003
[00.251](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.251](0) TEMPSENSOR.106: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9952.
[00.251](0) TEMPSENSOR.106: Receiver #1: 127.0.0.1:5005
[00.251](1) OVERSEER: Registered door #101 @127.0.0.1:5002 (FAIL_SAFE#)
[00.251](0) TEMPSENSOR.106: Receiver #2: 127.0.0.1:5006
[00.251](0) TEMPSENSOR.106: Receiver #3: 127.0.0.1:5007
[00.251](0) TEMPSENSOR.106: Receiver #4: 127.0.0.1:5009
[00.251](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.251](0) TEMPSENSOR.106: Binding addr 127.0.0.1:5008
[00.251](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
min detections: 3
detection period: 20000
[00.251](1) OVERSEER: Received message from client: FIREALARM 127.0.0.1:5001 HELLO#
[00.251](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.251](1) OVERSEER: Registered fire alarm @127.0.0.1:5001
[00.252](0) TEMPSENSOR.104: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9760.
[00.252](0) TEMPSENSOR.104: Receiver #1: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.104: Receiver #2: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.104: Binding addr 127.0.0.1:5006
[00.252](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.107: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 10048.
[00.252](0) TEMPSENSOR.107: Receiver #1: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.107: Receiver #2: 127.0.0.1:5001
[00.252](0) TEMPSENSOR.107: Binding addr 127.0.0.1:5009
[00.252](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.103: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9664.
[00.252](0) TEMPSENSOR.103: Receiver #1: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.103: Receiver #2: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.103: Binding addr 127.0.0.1:5005
[00.252](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.102: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9568.
[00.252](0) TEMPSENSOR.102: Receiver #1: 127.0.0.1:5003
[00.252](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.252](0) TEMPSENSOR.102: Receiver #2: 127.0.0.1:5005
[00.252](0) TEMPSENSOR.102: Receiver #3: 127.0.0.1:5006
[00.252](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.252](0) TEMPSENSOR.102: Receiver #4: 127.0.0.1:5007
[00.252](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.252](0) TEMPSENSOR.102: Binding addr 127.0.0.1:5004
[00.252](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.252](0) TEMPSENSOR.105: Starting up. Condvar wait: 1000us. Update wait: 500000us. Shm path: /shm. Offset: 9856.
[00.252](0) TEMPSENSOR.105: Receiver #1: 127.0.0.1:5004
[00.252](0) TEMPSENSOR.105: Receiver #2: 127.0.0.1:5008
[00.252](0) TEMPSENSOR.105: Binding addr 127.0.0.1:5007
[00.252](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.253](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:5008
[00.253](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.253](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:5000
[00.253](2) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.253](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[00.253](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[00.253](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[00.253](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[00.253](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.253](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.253](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.254](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[00.254](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.254](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.254](0) TEMPSENSOR.103: Propagating update (102:22.00) to 127.0.0.1:5008
[00.254](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.254](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.254](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.254](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.254](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.255](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5008
[00.255](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.255](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.255](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.255](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[00.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.255](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.256](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.256](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.256](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.256](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[00.256](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.256](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.256](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.256](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5008
[00.257](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.257](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.257](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.257](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.257](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5004
[00.257](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.258](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.258](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.258](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[00.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.258](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.258](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.258](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.258](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.259](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.259](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.259](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.259](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.259](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.259](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.260](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.260](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.260](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.260](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.260](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.260](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.260](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.260](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[00.261](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.261](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.261](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.261](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.261](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[00.262](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.262](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.262](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.262](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.262](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.263](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.263](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.272](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.282](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.292](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.302](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.312](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.322](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.332](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.342](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.352](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.362](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.372](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.382](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.392](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.403](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.413](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.423](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.433](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.443](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.453](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.463](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.473](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.483](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.493](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.503](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.513](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.523](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.534](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.544](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.554](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.564](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.574](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.584](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.594](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.604](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.614](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.624](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.634](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.644](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.654](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.664](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.675](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.685](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.695](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.705](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.715](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.725](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.735](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.745](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.751](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[00.752](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[00.752](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[00.752](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[00.752](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.752](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[00.752](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[00.752](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[00.752](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[00.752](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[00.752](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[00.752](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.752](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.752](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.752](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.752](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.753](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[00.753](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.753](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[00.753](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.753](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[00.753](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[00.753](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:5000
[00.753](2) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.754](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.754](0) TEMPSENSOR.105: Propagating update (102:22.00) to 127.0.0.1:5008
[00.754](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[00.754](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.754](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.754](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.754](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.754](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:5008
[00.754](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.754](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.755](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.755](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.755](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.755](0) TEMPSENSOR.103: Propagating update (102:22.00) to 127.0.0.1:5008
[00.755](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.755](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.755](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[00.755](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[00.755](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[00.755](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.755](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.756](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[00.756](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[00.756](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[00.756](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[00.756](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[00.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[00.756](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5004
[00.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[00.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[00.756](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[00.756](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.757](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.757](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[00.757](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[00.757](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.757](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[00.757](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.757](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.757](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.757](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.757](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.758](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[00.758](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.758](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.758](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[00.758](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[00.758](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.758](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[00.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[00.759](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.759](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[00.759](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[00.759](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[00.759](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[00.759](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[00.760](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[00.760](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.760](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.760](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.760](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[00.760](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.760](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.761](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.761](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.761](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[00.761](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[00.761](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[00.761](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[00.761](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[00.762](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5008
[00.762](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[00.762](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[00.762](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.762](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[00.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.762](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.762](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5008
[00.762](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.763](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.763](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.763](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[00.763](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[00.763](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5008
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.763](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.764](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.764](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5008
[00.764](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[00.764](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[00.764](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.764](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[00.764](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[00.764](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[00.764](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[00.765](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[00.765](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.765](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.765](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[00.765](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[00.765](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.766](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[00.766](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.766](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.766](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[00.766](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[00.766](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.766](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.766](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.767](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[00.767](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[00.767](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[00.767](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.767](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.767](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.767](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[00.767](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.768](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[00.768](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.768](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.768](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.768](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.768](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[00.768](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[00.768](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[00.769](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[00.769](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[00.769](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[00.769](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[00.769](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[00.775](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.785](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.795](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.806](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.816](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.826](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.836](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.846](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.856](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.866](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.876](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.886](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.896](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.906](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.916](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.926](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.937](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.947](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.957](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.967](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.977](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.987](3) OVERSEER: Sending packet to 127.0.0.1:5002
[00.997](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.007](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.017](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.027](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.037](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.047](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.057](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.068](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.078](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.088](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.098](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.108](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.118](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.128](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.138](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.148](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.158](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.168](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.178](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.188](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.199](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.209](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.219](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.229](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.239](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.249](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.252](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[01.252](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.252](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[01.252](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.252](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.252](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[01.252](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[01.253](0) TEMPSENSOR.105: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[01.253](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.253](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.253](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.253](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.253](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.253](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.253](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.253](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.253](0) TEMPSENSOR.103: Temperature is 22.00 - sending update
[01.253](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[01.253](0) TEMPSENSOR.107: Temperature is 22.00 - sending update
[01.254](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.254](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[01.254](0) TEMPSENSOR.102: Temperature is 22.00 - sending update
[01.254](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.254](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.254](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.254](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[01.254](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[01.254](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.254](0) TEMPSENSOR.104: Propagating update (102:22.00) to 127.0.0.1:5008
[01.254](0) TEMPSENSOR.101: Propagating update (102:22.00) to 127.0.0.1:5000
[01.254](2) OVERSEER: Received UDP TEMP packet: id=102 temp=22.00
[01.255](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[01.255](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.255](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[01.255](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[01.255](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[01.255](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[01.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[01.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[01.255](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.255](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5004
[01.256](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.256](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.256](0) TEMPSENSOR.103: Propagating update (102:22.00) to 127.0.0.1:5008
[01.256](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.256](0) TEMPSENSOR.105: Propagating update (102:22.00) to 127.0.0.1:5008
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.256](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.256](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.257](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[01.257](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.257](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.257](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.257](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.257](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[01.257](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[01.257](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5005
[01.258](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5006
[01.258](0) TEMPSENSOR.106: Propagating update (107:22.00) to 127.0.0.1:5007
[01.258](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5004
[01.258](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.258](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.258](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5004
[01.258](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.259](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.259](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.259](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.259](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[01.259](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.259](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.259](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.259](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5004
[01.259](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.259](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[01.259](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[01.260](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.260](0) TEMPSENSOR.104: Propagating update (105:22.00) to 127.0.0.1:5008
[01.260](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.260](0) TEMPSENSOR.103: Propagating update (105:22.00) to 127.0.0.1:5008
[01.260](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.260](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.261](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.261](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.261](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[01.261](0) TEMPSENSOR.104: Propagating update (107:22.00) to 127.0.0.1:5004
[01.261](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5007
[01.261](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.261](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.261](0) TEMPSENSOR.103: Propagating update (107:22.00) to 127.0.0.1:5004
[01.261](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.261](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.262](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.262](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.262](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5005
[01.262](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5006
[01.262](0) TEMPSENSOR.106: Propagating update (102:22.00) to 127.0.0.1:5009
[01.262](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.262](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.262](0) TEMPSENSOR.107: Propagating update (102:22.00) to 127.0.0.1:5001
[01.262](0) TEMPSENSOR.105: Propagating update (107:22.00) to 127.0.0.1:5004
[01.263](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.263](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5005
[01.263](0) TEMPSENSOR.104: Propagating update (103:22.00) to 127.0.0.1:5008
[01.263](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.263](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.263](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.263](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.263](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.263](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.263](0) TEMPSENSOR.105: Propagating update (103:22.00) to 127.0.0.1:5008
[01.264](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.264](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5007
[01.264](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.264](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.264](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.264](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.264](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.264](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.265](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5003
[01.265](0) TEMPSENSOR.102: Propagating update (105:22.00) to 127.0.0.1:5006
[01.265](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.265](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.265](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.265](0) TEMPSENSOR.101: Propagating update (105:22.00) to 127.0.0.1:5000
[01.265](2) OVERSEER: Received UDP TEMP packet: id=105 temp=22.00
[01.265](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.266](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5003
[01.266](0) TEMPSENSOR.102: Propagating update (103:22.00) to 127.0.0.1:5006
[01.266](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5005
[01.266](0) TEMPSENSOR.101: Propagating update (103:22.00) to 127.0.0.1:5000
[01.266](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.266](2) OVERSEER: Received UDP TEMP packet: id=103 temp=22.00
[01.266](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.267](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.267](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[01.267](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[01.267](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.267](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5006
[01.267](0) TEMPSENSOR.106: Propagating update (105:22.00) to 127.0.0.1:5009
[01.267](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.267](0) TEMPSENSOR.107: Propagating update (105:22.00) to 127.0.0.1:5001
[01.268](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.268](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[01.268](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5007
[01.268](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.268](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.268](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5007
[01.268](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.269](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.269](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.269](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5003
[01.269](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5005
[01.269](0) TEMPSENSOR.102: Propagating update (107:22.00) to 127.0.0.1:5006
[01.270](0) TEMPSENSOR.101: Propagating update (107:22.00) to 127.0.0.1:5000
[01.270](2) OVERSEER: Received UDP TEMP packet: id=107 temp=22.00
[01.270](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5006
[01.270](0) TEMPSENSOR.106: Propagating update (103:22.00) to 127.0.0.1:5009
[01.270](0) TEMPSENSOR.107: Propagating update (103:22.00) to 127.0.0.1:5001
[01.279](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.289](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.299](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.309](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.319](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.330](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.340](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.348](4) SIMULATOR: Tempsensor sim (#2): temperature changed to 33.50
[01.348](0) TEMPSENSOR.103: Temperature is 33.50 - sending update
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.349](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.349](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.349](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.349](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.349](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5008
[01.349](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.349](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.350](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.350](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5008
[01.350](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.350](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5004
[01.350](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.350](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.351](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5004
[01.351](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.351](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.351](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.351](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.351](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.351](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.351](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.352](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.352](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.352](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.352](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.352](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.360](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.370](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.380](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.390](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.398](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 102:22.00 105:22.00 104:22.00 107:22.00 103:33.50 106:22.00 
[01.400](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.410](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.420](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.430](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.440](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.448](3) SIMULATOR: Tempsensor sim (#1): temperature changed to 31.70
[01.448](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[01.448](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[01.448](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[01.449](2) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[01.449](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[01.449](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[01.449](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.449](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.449](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.450](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.450](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.451](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.452](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.460](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.471](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.481](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.491](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.498](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 102:31.70 105:22.00 104:22.00 107:22.00 103:33.50 106:22.00 
[01.501](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.511](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.521](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.531](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.541](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.548](8) SIMULATOR: Tempsensor sim (#6): temperature changed to 25.40
[01.548](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[01.549](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[01.549](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[01.550](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[01.550](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[01.550](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[01.550](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.550](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[01.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[01.551](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.551](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.551](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[01.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[01.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[01.552](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[01.552](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[01.561](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.571](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.581](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.591](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.598](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 102:31.70 105:22.00 104:22.00 107:25.40 103:33.50 106:22.00 
[01.602](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.612](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.622](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.632](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.642](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.648](6) SIMULATOR: Tempsensor sim (#4): temperature changed to 29.10
[01.648](0) TEMPSENSOR.105: Temperature is 29.10 - sending update
[01.648](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.648](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5005
[01.648](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5006
[01.649](0) TEMPSENSOR.104: Propagating update (105:29.10) to 127.0.0.1:5008
[01.649](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.649](2) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5005
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5006
[01.649](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.649](0) TEMPSENSOR.103: Propagating update (105:29.10) to 127.0.0.1:5008
[01.650](0) TEMPSENSOR.104: Propagating update (105:29.10) to 127.0.0.1:5004
[01.650](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.650](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5005
[01.650](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.650](0) TEMPSENSOR.103: Propagating update (105:29.10) to 127.0.0.1:5004
[01.651](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.651](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5005
[01.651](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.651](2) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.651](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.651](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5006
[01.651](0) TEMPSENSOR.106: Propagating update (105:29.10) to 127.0.0.1:5009
[01.652](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5003
[01.652](0) TEMPSENSOR.102: Propagating update (105:29.10) to 127.0.0.1:5006
[01.652](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.652](0) TEMPSENSOR.101: Propagating update (105:29.10) to 127.0.0.1:5000
[01.652](2) OVERSEER: Received UDP TEMP packet: id=105 temp=29.10
[01.652](0) TEMPSENSOR.107: Propagating update (105:29.10) to 127.0.0.1:5001
[01.662](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.672](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.682](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.692](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.702](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.712](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.722](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.733](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.743](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.748](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 102:31.70 105:29.10 104:22.00 107:25.40 103:33.50 106:22.00 
[01.753](0) TEMPSENSOR.104: Temperature is 22.00 - sending update
[01.753](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.753](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[01.753](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[01.753](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[01.753](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.753](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.753](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.753](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[01.753](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[01.753](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.753](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.753](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.754](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[01.754](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.754](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[01.754](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.754](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5004
[01.754](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5004
[01.754](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[01.755](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[01.755](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[01.755](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[01.755](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.755](0) TEMPSENSOR.103: Propagating update (104:22.00) to 127.0.0.1:5008
[01.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.755](0) TEMPSENSOR.105: Propagating update (104:22.00) to 127.0.0.1:5008
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.756](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.756](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.756](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.756](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[01.756](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5007
[01.756](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.756](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[01.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[01.757](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.757](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.757](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.757](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5005
[01.757](0) TEMPSENSOR.106: Propagating update (104:22.00) to 127.0.0.1:5009
[01.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[01.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[01.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[01.758](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[01.758](0) TEMPSENSOR.107: Propagating update (104:22.00) to 127.0.0.1:5001
[01.758](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[01.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[01.758](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.759](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5007
[01.759](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.759](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.759](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[01.760](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[01.760](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5003
[01.760](0) TEMPSENSOR.102: Propagating update (104:22.00) to 127.0.0.1:5005
[01.760](0) TEMPSENSOR.101: Propagating update (104:22.00) to 127.0.0.1:5000
[01.760](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[01.760](2) OVERSEER: Received UDP TEMP packet: id=104 temp=22.00
[01.763](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.773](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.783](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.793](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.803](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.813](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.823](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.833](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.843](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.848](0) TEMPSENSOR.103: Temperature is 33.50 - sending update
[01.849](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.849](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.849](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.849](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5004
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.849](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.849](4) SIMULATOR: Tempsensor sim (#2): temperature changed to 53.10
[01.849](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[01.849](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.849](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.849](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.850](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5004
[01.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[01.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[01.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.850](0) TEMPSENSOR.104: Propagating update (103:33.50) to 127.0.0.1:5008
[01.850](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.850](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5007
[01.850](5) SIMULATOR: Tempsensor sim (#3): temperature changed to 56.20
[01.850](0) TEMPSENSOR.104: Temperature is 56.20 - sending update
[01.850](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5004
[01.850](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.850](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.850](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.851](0) TEMPSENSOR.105: Propagating update (103:33.50) to 127.0.0.1:5008
[01.851](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5007
[01.851](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.851](6) SIMULATOR: Tempsensor sim (#4): temperature changed to 58.40
[01.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[01.851](0) TEMPSENSOR.105: Temperature is 58.40 - sending update
[01.851](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[01.851](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5004
[01.851](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5008
[01.851](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.851](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.851](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.852](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[01.852](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[01.852](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.852](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5003
[01.852](0) TEMPSENSOR.102: Propagating update (103:33.50) to 127.0.0.1:5006
[01.852](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5004
[01.852](0) TEMPSENSOR.101: Propagating update (103:33.50) to 127.0.0.1:5000
[01.852](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.852](2) OVERSEER: Received UDP TEMP packet: id=103 temp=33.50
[01.853](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5006
[01.853](0) TEMPSENSOR.106: Propagating update (103:33.50) to 127.0.0.1:5009
[01.853](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.853](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[01.853](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[01.853](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5008
[01.853](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.854](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.854](0) TEMPSENSOR.107: Propagating update (103:33.50) to 127.0.0.1:5001
[01.854](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.854](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[01.854](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[01.854](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.854](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5008
[01.854](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.854](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[01.854](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5004
[01.854](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5004
[01.855](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.855](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.855](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.855](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[01.855](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.855](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5004
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[01.855](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[01.856](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5008
[01.856](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.856](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.856](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.856](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[01.856](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.856](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5008
[01.857](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5008
[01.857](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[01.857](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[01.857](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[01.857](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[01.857](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.857](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[01.857](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[01.858](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.858](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[01.858](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.858](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.858](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[01.858](0) SIMULATOR: Simulated input to overseer: TEMPSENSOR LIST
101:22.00 102:31.70 105:58.40 104:56.20 107:25.40 103:53.10 106:22.00 
[01.858](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[01.858](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.859](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.859](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[01.859](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.859](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.859](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.859](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[01.859](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[01.860](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[01.860](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[01.860](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[01.860](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[01.860](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[01.860](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[01.860](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[01.861](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[01.861](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[01.861](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[01.861](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[01.861](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[01.863](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.874](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.884](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.894](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.904](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.914](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.924](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.934](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.944](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.949](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[01.949](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[01.949](2) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[01.950](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[01.950](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[01.950](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.951](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.951](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.952](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.952](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.953](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[01.953](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[01.953](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[01.953](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[01.954](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.964](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.974](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.984](3) OVERSEER: Sending packet to 127.0.0.1:5002
[01.994](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.005](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.015](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.025](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.035](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.045](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.049](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[02.049](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[02.049](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[02.049](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[02.049](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[02.049](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[02.050](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[02.050](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.050](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.050](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.051](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.051](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.051](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.051](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.051](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.052](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.052](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.052](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.053](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.053](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.055](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.065](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.075](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.085](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.095](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.105](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.115](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.125](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.136](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.146](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.156](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.166](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.176](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.186](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.196](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.206](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.216](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.226](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.236](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.246](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.253](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[02.253](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[02.253](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[02.253](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[02.253](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[02.254](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[02.254](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[02.254](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[02.254](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[02.254](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[02.255](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.255](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.255](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.255](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[02.255](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[02.255](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.255](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.255](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.256](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.256](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.256](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.256](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.256](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.256](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.256](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.257](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.257](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.257](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.257](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.257](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.257](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.258](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.258](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.258](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.259](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.267](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.277](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.287](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.297](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.307](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.317](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.327](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.337](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.347](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.349](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[02.350](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.350](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.350](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.350](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[02.350](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[02.350](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.350](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5008
[02.350](0) TEMPSENSOR.104: Temperature is 56.20 - sending update
[02.350](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5008
[02.351](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.351](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.351](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.351](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[02.351](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[02.351](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.351](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[02.351](0) TEMPSENSOR.105: Temperature is 58.40 - sending update
[02.351](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.351](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5004
[02.351](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5008
[02.351](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5004
[02.352](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.352](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.352](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.352](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[02.352](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[02.352](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.352](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[02.352](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[02.352](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5008
[02.352](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.352](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5008
[02.353](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.353](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.353](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.353](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.353](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.353](0) TEMPSENSOR.105: Propagating update (104:56.20) to 127.0.0.1:5004
[02.353](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[02.353](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.354](0) TEMPSENSOR.103: Propagating update (104:56.20) to 127.0.0.1:5004
[02.354](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5008
[02.354](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.354](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.354](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.354](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.354](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.354](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[02.354](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[02.354](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.355](0) TEMPSENSOR.103: Propagating update (105:58.40) to 127.0.0.1:5004
[02.355](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.355](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.355](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.355](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5005
[02.355](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.355](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5007
[02.356](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.356](0) TEMPSENSOR.104: Propagating update (105:58.40) to 127.0.0.1:5004
[02.356](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.356](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.356](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5003
[02.356](0) TEMPSENSOR.102: Propagating update (104:56.20) to 127.0.0.1:5007
[02.356](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.357](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5005
[02.357](0) TEMPSENSOR.106: Propagating update (104:56.20) to 127.0.0.1:5009
[02.357](0) TEMPSENSOR.101: Propagating update (104:56.20) to 127.0.0.1:5000
[02.357](2) OVERSEER: Received UDP TEMP packet: id=104 temp=56.20
[02.357](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.357](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.357](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5006
[02.357](0) TEMPSENSOR.107: Propagating update (104:56.20) to 127.0.0.1:5001
[02.358](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5006
[02.358](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.358](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.358](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.358](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5003
[02.358](0) TEMPSENSOR.102: Propagating update (105:58.40) to 127.0.0.1:5005
[02.358](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.359](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5005
[02.359](0) TEMPSENSOR.106: Propagating update (105:58.40) to 127.0.0.1:5009
[02.359](0) TEMPSENSOR.101: Propagating update (105:58.40) to 127.0.0.1:5000
[02.359](2) OVERSEER: Received UDP TEMP packet: id=105 temp=58.40
[02.359](0) TEMPSENSOR.107: Propagating update (105:58.40) to 127.0.0.1:5001
[02.367](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.377](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.387](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.397](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.408](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.418](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.428](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.438](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.448](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.449](0) TEMPSENSOR.102: Temperature is 31.70 - sending update
[02.450](0) TEMPSENSOR.105: Propagating update (102:31.70) to 127.0.0.1:5008
[02.450](0) TEMPSENSOR.104: Propagating update (102:31.70) to 127.0.0.1:5008
[02.450](0) TEMPSENSOR.103: Propagating update (102:31.70) to 127.0.0.1:5008
[02.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[02.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[02.450](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.450](0) TEMPSENSOR.101: Propagating update (102:31.70) to 127.0.0.1:5000
[02.450](2) OVERSEER: Received UDP TEMP packet: id=102 temp=31.70
[02.450](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5005
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[02.451](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.452](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5006
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5007
[02.452](0) TEMPSENSOR.106: Propagating update (102:31.70) to 127.0.0.1:5009
[02.453](0) TEMPSENSOR.107: Propagating update (102:31.70) to 127.0.0.1:5001
[02.458](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.468](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.478](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.488](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.498](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.508](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.518](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.528](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.539](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.549](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.549](0) TEMPSENSOR.107: Temperature is 25.40 - sending update
[02.550](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5005
[02.550](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5006
[02.550](0) TEMPSENSOR.106: Propagating update (107:25.40) to 127.0.0.1:5007
[02.550](0) TEMPSENSOR.105: Propagating update (107:25.40) to 127.0.0.1:5004
[02.550](0) TEMPSENSOR.104: Propagating update (107:25.40) to 127.0.0.1:5004
[02.551](0) TEMPSENSOR.103: Propagating update (107:25.40) to 127.0.0.1:5004
[02.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.551](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.552](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.552](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5005
[02.552](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.553](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.553](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5003
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5006
[02.553](0) TEMPSENSOR.102: Propagating update (107:25.40) to 127.0.0.1:5007
[02.554](0) TEMPSENSOR.101: Propagating update (107:25.40) to 127.0.0.1:5000
[02.554](2) OVERSEER: Received UDP TEMP packet: id=107 temp=25.40
[02.559](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.569](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.579](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.589](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.599](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.609](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.619](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.629](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.639](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.649](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.659](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.669](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.680](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.690](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.700](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.710](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.720](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.730](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.740](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.750](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.753](0) TEMPSENSOR.101: Temperature is 22.00 - sending update
[02.754](2) OVERSEER: Received UDP TEMP packet: id=101 temp=22.00
[02.754](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5005
[02.754](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5006
[02.754](0) TEMPSENSOR.102: Propagating update (101:22.00) to 127.0.0.1:5007
[02.754](0) TEMPSENSOR.105: Propagating update (101:22.00) to 127.0.0.1:5008
[02.754](0) TEMPSENSOR.104: Propagating update (101:22.00) to 127.0.0.1:5008
[02.754](0) TEMPSENSOR.103: Propagating update (101:22.00) to 127.0.0.1:5008
[02.755](0) TEMPSENSOR.106: Temperature is 22.00 - sending update
[02.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.755](0) TEMPSENSOR.107: Propagating update (106:22.00) to 127.0.0.1:5001
[02.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.755](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.755](0) TEMPSENSOR.105: Propagating update (106:22.00) to 127.0.0.1:5004
[02.755](0) TEMPSENSOR.104: Propagating update (106:22.00) to 127.0.0.1:5004
[02.755](0) TEMPSENSOR.103: Propagating update (106:22.00) to 127.0.0.1:5004
[02.756](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.756](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5005
[02.756](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.756](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.756](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.757](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.757](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.757](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.757](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5006
[02.757](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5007
[02.757](0) TEMPSENSOR.106: Propagating update (101:22.00) to 127.0.0.1:5009
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5005
[02.757](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.758](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.758](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.758](0) TEMPSENSOR.107: Propagating update (101:22.00) to 127.0.0.1:5001
[02.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5003
[02.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5006
[02.758](0) TEMPSENSOR.102: Propagating update (106:22.00) to 127.0.0.1:5007
[02.759](0) TEMPSENSOR.101: Propagating update (106:22.00) to 127.0.0.1:5000
[02.759](2) OVERSEER: Received UDP TEMP packet: id=106 temp=22.00
[02.760](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.770](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.780](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.790](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.800](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.811](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.821](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.831](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.841](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.849](0) TEMPSENSOR.103: Temperature is 53.10 - sending update
[02.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5006
[02.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5007
[02.850](0) TEMPSENSOR.106: Propagating update (103:53.10) to 127.0.0.1:5009
[02.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5003
[02.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5006
[02.850](0) TEMPSENSOR.102: Propagating update (103:53.10) to 127.0.0.1:5007
[02.850](0) TEMPSENSOR.105: Propagating update (103:53.10) to 127.0.0.1:5004
[02.850](0) TEMPSENSOR.104: Temperature is 56.20 - sending update
[02.850](0) TEMPSENSOR.104: Propagating update (103:53.10) to 127.0.0.1:5004
[02.851](3) OVERSEER: Sending packet to 127.0.0.1:5002
[02.851](0) TEMPSENSOR.101: Propagating update (103:53.10) to 127.0.0.1:5000
[02.851](0) TEMPSENSOR.107: Propagating update (103:53.10) to 127.0.0.1:5001
[02.851](2) OVERSEER: Received UDP TEMP packet: id=103 temp=53.10
[02.851](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_1_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.248](0) SIMULATOR: Launching callpoint
[00.249](1) SIMULATOR: Door sim (#0) started
[00.249](2) SIMULATOR: Callpoint sim (#0) started
[00.249](3) SIMULATOR: Door sim (#1) started
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4700
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4700
[00.251](0) CALLPOINT: Starting up. Resend delay: 103us. Shm path: /shm. Offset: 11392. Firealarm addr: 127.0.0.1:4701
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4703
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4702
[00.251](1) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4703 FAIL_SECURE#
[00.251](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4701 HELLO#
[00.251](1) OVERSEER: Registered door #102 @127.0.0.1:4703 (FAIL_SECURE#)
[00.251](3) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4702 FAIL_SAFE#
[00.251](2) OVERSEER: Registered fire alarm @127.0.0.1:4701
[00.251](3) OVERSEER: Registered door #101 @127.0.0.1:4702 (FAIL_SAFE#)
[01.259](2) SIMULATOR: Callpoint sim (#0) was triggered
[01.259](0) CALLPOINT: Callpoint has been triggered
[01.259](4) SIMULATOR: Security alarm has been triggered.
[01.259](0) DOOR.101: Received message: OPEN_EMERG#
[01.259](0) DOOR.101: Current status: C
[01.259](0) DOOR.101: OPENING# (emergency)
[01.259](1) SIMULATOR: Door sim (#0) woke up. Status = o
[01.269](1) SIMULATOR: Door sim (#0) changed status to = O
[01.269](0) DOOR.101: OPENED# (emergency)
[02.259](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_2_reference = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.249](1) SIMULATOR: Cardreader sim (#0) started
[00.249](2) SIMULATOR: Door sim (#0) started
[00.249](3) SIMULATOR: Door sim (#1) started
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4800
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4802
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4800
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4803
[00.251](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4800
[00.251](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4800
[00.251](0) CARDREADER.103: Sending HELLO#
[00.251](1) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4801 HELLO#
[00.251](1) OVERSEER: Registered fire alarm @127.0.0.1:4801
[00.251](2) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4802 FAIL_SAFE#
[00.251](3) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4803 FAIL_SECURE#
[00.251](4) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.252](4) OVERSEER: Got reg event from cardreader 103
[00.252](3) OVERSEER: Registered door #102 @127.0.0.1:4803 (FAIL_SECURE#)
[00.251](2) OVERSEER: Registered door #101 @127.0.0.1:4802 (FAIL_SAFE#)
[01.399](0) SIMULATOR: Simulated input to overseer: FIRE ALARM
Fire alarm triggered!
[01.399](4) SIMULATOR: Security alarm has been triggered.
[01.399](0) DOOR.101: Received message: OPEN_EMERG#
[01.399](0) DOOR.101: Current status: C
[01.399](0) DOOR.101: OPENING# (emergency)
[01.399](2) SIMULATOR: Door sim (#0) woke up. Status = o
[01.409](2) SIMULATOR: Door sim (#0) changed status to = O
[01.409](0) DOOR.101: OPENED# (emergency)
[01.449](0) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.449](0) DOOR.101: Received message: CLOSE#
[01.449](0) DOOR.101: Current status: O
[01.449](0) DOOR.101: EMERGENCY_MODE#
Door reports that it open due to an emergency and cannot be closed
[01.549](1) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.549](5) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.549](5) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.549](0) CARDREADER.103: Received response: ALLOWED#
[01.549](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](0) DOOR.102: Received message: OPEN#
[01.549](0) DOOR.102: Current status: C
[01.549](0) DOOR.102: OPENING#
[01.549](5) OVERSEER: Received OPENING# from door
[01.549](3) SIMULATOR: Door sim (#1) woke up. Status = o
[01.559](3) SIMULATOR: Door sim (#1) changed status to = O
[01.559](0) DOOR.102: OPENED#
[01.559](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.659](0) DOOR.102: Received message: CLOSE#
[01.659](0) DOOR.102: Current status: O
[01.659](0) DOOR.102: CLOSING#
[01.660](5) OVERSEER: Received CLOSING# from door
[01.660](3) SIMULATOR: Door sim (#1) woke up. Status = c
[01.670](3) SIMULATOR: Door sim (#1) changed status to = C
[01.670](0) DOOR.102: CLOSED#
[01.670](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.549](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_1_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.248](0) SIMULATOR: Launching callpoint
[00.249](1) SIMULATOR: Door sim (#0) started
[00.249](2) SIMULATOR: Callpoint sim (#0) started
[00.249](3) SIMULATOR: Door sim (#1) started
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4700
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4700
[00.251](0) CALLPOINT: Starting up. Resend delay: 103us. Shm path: /shm. Offset: 11392. Firealarm addr: 127.0.0.1:4701
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4703
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4702
[00.251](1) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4703 FAIL_SECURE#
[00.251](2) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4701 HELLO#
[00.251](1) OVERSEER: Registered door #102 @127.0.0.1:4703 (FAIL_SECURE#)
[00.251](3) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4702 FAIL_SAFE#
[00.251](2) OVERSEER: Registered fire alarm @127.0.0.1:4701
[00.251](3) OVERSEER: Registered door #101 @127.0.0.1:4702 (FAIL_SAFE#)
[01.259](2) SIMULATOR: Callpoint sim (#0) was triggered
[01.259](0) CALLPOINT: Callpoint has been triggered
[01.259](4) SIMULATOR: Security alarm has been triggered.
[01.259](0) DOOR.101: Received message: OPEN_EMERG#
[01.259](0) DOOR.101: Current status: C
[01.259](0) DOOR.101: OPENING# (emergency)
[01.259](1) SIMULATOR: Door sim (#0) woke up. Status = o
[01.269](1) SIMULATOR: Door sim (#0) changed status to = O
[01.269](0) DOOR.101: OPENED# (emergency)
[02.259](0) SIMULATOR: Simulation ended, shutting down
"""

firealarm_2_submission = """
[00.000](0) OVERSEER: Starting up. Door open duration: 100000us Datagram resend delay: 10000us. Auth file: authorisation.txt. Connections file: connections.txt. Layout file: layout.txt. Shared memory space: /shm. Shared memory offset: 0
[00.248](0) SIMULATOR: Launching firealarm
[00.249](1) SIMULATOR: Cardreader sim (#0) started
[00.249](2) SIMULATOR: Door sim (#0) started
[00.249](3) SIMULATOR: Door sim (#1) started
[00.251](0) DOOR.101: Starting up. Mode: FAIL_SAFE. Shm path: /shm. Offset: 6592. Overseer addr: 127.0.0.1:4800
[00.251](0) DOOR.101: Binding addr 127.0.0.1:4802
[00.251](0) DOOR.102: Starting up. Mode: FAIL_SECURE. Shm path: /shm. Offset: 6736. Overseer addr: 127.0.0.1:4800
[00.251](0) DOOR.102: Binding addr 127.0.0.1:4803
[00.251](0) CARDREADER.103: Starting up. Shm path: /shm. Offset: 192. Overseer addr: 127.0.0.1:4800
[00.251](0) CARDREADER.103: Attempting to connect to 127.0.0.1:4800
[00.251](0) CARDREADER.103: Sending HELLO#
[00.251](1) OVERSEER: Received message from client: FIREALARM 127.0.0.1:4801 HELLO#
[00.251](1) OVERSEER: Registered fire alarm @127.0.0.1:4801
[00.251](2) OVERSEER: Received message from client: DOOR 101 127.0.0.1:4802 FAIL_SAFE#
[00.251](3) OVERSEER: Received message from client: DOOR 102 127.0.0.1:4803 FAIL_SECURE#
[00.251](4) OVERSEER: Received message from client: CARDREADER 103 HELLO#
[00.252](4) OVERSEER: Got reg event from cardreader 103
[00.252](3) OVERSEER: Registered door #102 @127.0.0.1:4803 (FAIL_SECURE#)
[00.251](2) OVERSEER: Registered door #101 @127.0.0.1:4802 (FAIL_SAFE#)
[01.399](0) SIMULATOR: Simulated input to overseer: FIRE ALARM
Fire alarm triggered!
[01.399](4) SIMULATOR: Security alarm has been triggered.
[01.399](0) DOOR.101: Received message: OPEN_EMERG#
[01.399](0) DOOR.101: Current status: C
[01.399](0) DOOR.101: OPENING# (emergency)
[01.399](2) SIMULATOR: Door sim (#0) woke up. Status = o
[01.409](2) SIMULATOR: Door sim (#0) changed status to = O
[01.409](0) DOOR.101: OPENED# (emergency)
[01.449](0) SIMULATOR: Simulated input to overseer: DOOR CLOSE 101
[01.449](0) DOOR.101: Received message: CLOSE#
[01.449](0) DOOR.101: Current status: O
[01.449](0) DOOR.101: EMERGENCY_MODE#
Door reports that it open due to an emergency and cannot be closed
[01.549](1) SIMULATOR: Cardreader sim (#0): scanned code 2214a7ba5943d923
[01.549](0) CARDREADER.103: Scanned code: 2214a7ba5943d923 - connecting to overseer
[01.549](5) OVERSEER: Received message from client: CARDREADER 103 SCANNED 2214a7ba5943d923#
[01.549](5) OVERSEER: Got scan from cardreader 103: 2214a7ba5943d923
[01.549](0) CARDREADER.103: Received response: ALLOWED#
[01.549](1) SIMULATOR: Cardreader sim (#0): response to scan: Y
[01.549](0) DOOR.102: Received message: OPEN#
[01.549](0) DOOR.102: Current status: C
[01.549](0) DOOR.102: OPENING#
[01.549](5) OVERSEER: Received OPENING# from door
[01.549](3) SIMULATOR: Door sim (#1) woke up. Status = o
[01.559](3) SIMULATOR: Door sim (#1) changed status to = O
[01.559](0) DOOR.102: OPENED#
[01.559](5) OVERSEER: Received OPENED# from door (should be OPENED#)
[01.659](0) DOOR.102: Received message: CLOSE#
[01.659](0) DOOR.102: Current status: O
[01.659](0) DOOR.102: CLOSING#
[01.660](5) OVERSEER: Received CLOSING# from door
[01.660](3) SIMULATOR: Door sim (#1) woke up. Status = c
[01.670](3) SIMULATOR: Door sim (#1) changed status to = C
[01.670](0) DOOR.102: CLOSED#
[01.670](5) OVERSEER: Received CLOSED# from door (should be CLOSED#)
[02.549](0) SIMULATOR: Simulation ended, shutting down
"""