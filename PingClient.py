import socket
import os, sys
import json
from PingResult import PingResult

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10800        # The port used by the server

# Process the command line arguments, if none provided use 'google.com'
domainName = sys.argv[1] if len(sys.argv[1]) > 1 else 'google.com'

# Start the socket, connect to the server and send a request
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Sending ping request to server.')
    s.sendall(bytes(domainName, 'utf-8'))
    print('Waiting for response...')
    data = s.recv(1024)

# decode data into PingResult class
pingResult = PingResult(**json.loads(data.decode("utf-8")))

# inform user TODO move print message logic into PingResult class
print('Ping Results:' )
print('Domain name tested was', domainName)
if pingResult.errorOccured():
    print('Error - cannot resolve domain name to IP address. (', pingResult.errorMsg, ')')
else:
    print(pingResult.numPacketsTransmitted, 'pings were sent with', pingResult.numPacketsRecieved, 'pings succeeding.')
    print(pingResult.percentPacketLoss, '% of packets were lost.')
    if pingResult.percentPacketLoss < 100.0:
        print('Average RTT was', float(pingResult.averageRTT) / 1000, 'seconds')
    else:
        print('Average RTT is not applicable: all packets lost.')