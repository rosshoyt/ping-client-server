import socket
import os, sys
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10800        # The port used by the server
userArgs = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Process the command line arguments, if none provided use 'google.com'
    data = userArgs if len(sys.argv) > 1 else 'google.com'
    s.sendall(bytes(data, 'utf-8'))
    data = s.recv(1024)

# decode data
strData = data.decode("utf-8")

usrMessageStart = 'Ping ' + userArgs + ' Results: '
if 'ERROR' in strData:
    print(usrMessageStart, 'error - could not connect to provided domain name')
else:
    print(usrMessageStart, repr(strData))
    

