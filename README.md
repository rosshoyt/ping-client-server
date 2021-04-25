# Project 1: Ping Client/Server
### Ross Hoyt - CPSC 5510 Computer Networks - SP 2021
#
## Instructions:
## 1) Start Server:
### python3 PingServer.py
## 2) Start Client in new terminal (pass in domain name or IP Address):
### python3 PingClient.py rosshoyt.com
* #### If no domain name passed in, google.com is used
#
## Protocol Overview
## 1 Introduction
* ### This project uses an application-level protocol designed to allow a client host to communicate with a server, in order to 'ping' a desired domain name
* ### The protocol should communicate over a TCP connection or other reliable transport protocol
## 2 Parameters
### 2.1 Character Set
* ### All text content should be encoded in UTF-8 format
## 3 Messages
### 3.1 Message Types
* ### Protocol messages consist of a request from client to server and a response from server to client
### 3.4 Message Length
* ### All messages are all of size 1024 bytes
## 4 Request Message
* ### A request message from a client to a server contains  domain name or IP Address to ping. 
* #### Example Request:
"www.google.com"
## 5 Response Message
* ### After receiving and interpreting a request message, a server responds with a  response message formatted in JSON:
* #### Example Response:
{"domainName": "www.google.com", "errorMsg": "", "numPacketsTransmitted": 20, "numPacketsRecieved": 20, "percentPacketLoss": 0.0, "averageRTT": "9.059"}
#
## Protocol Use Case Example:
### Server starts and opens TCP socket on port 10800
### Client initiates socket connection with Server over port 10800
### Client sends server a request message with domain name passed in by client's user
### Server attempts to ping the address 20 times
### Server parses results returned by host OS
### Server sends JSON data via socket to client 
### Client recieves byte data and displays info message to user
### Client closes the connection with the server (Server remains open for other clients to connect)