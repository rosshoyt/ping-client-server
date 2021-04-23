import socket
import os, sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Process the command line arguments, if none provided use 'google.com'
    data = sys.argv[1] if len(sys.argv) > 1 else 'google.com'
    s.sendall(bytes(data, 'utf-8'))
    data = s.recv(1024)

print('Received', repr(data))