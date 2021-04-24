## Project 1: PING Client/Server
### Ross Hoyt - CPSC 5510 Computer Networks - SP2021
#
## Instructions (CS1):
## 1. Start Server
### python3 PingServer.py
## 2. Start Client in new terminal (pass in domain name)
### python3 PingClient.py facebook.com
#### Note: If no site passed in, 'google.com' is used
#
### Protocol Outline:
### 1. Client initiates TCP socket connection with Server over port 10800
### 2. Client sends the passed-in domain name to Server
### 3. Server attempts to ping the address 20 times
### 4. Server parses results returned by OS
### 5. Server Sends json data via socket to Client
### 6. Client recieves byte data and displays message to user
###