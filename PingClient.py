import socket
import os, sys
import json
from PingResult import PingResult

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10800        # The port used by the server

# Process the command line arguments, if none provided use 'google.com'
domainName = sys.argv[1] if len(sys.argv[1]) > 1 else 'google.com'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(domainName, 'utf-8'))
    data = s.recv(1024)

# decode data
pingResult = PingResult(**json.loads(data.decode("utf-8")))
print('Ping Results:' )
print('Domain name tested was', domainName)
if pingResult.errorOccured():
    print('Error - cannot resolve domain name to IP address. (',pingResult.errorMsg, ')')
else:
    print(pingResult.numPacketsTransmitted, 'pings were sent with', pingResult.numPacketsRecieved, 'pings succeeding.')
    print(pingResult.percentPacketLoss, '% of packets were lost.')
    print('Average RTT was', float(pingResult.averageRTT) / 1000, 'seconds')
