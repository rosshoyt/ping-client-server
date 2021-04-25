import subprocess
import socket
import json
import re
from _thread import *
from PingResult import PingResult

HOST = '127.0.0.1'
PORT = 10800
NUM_PINGS = '3'

def parsePingResult(result):
    """
    TODO handle error message in std err
    """
    pingResult = PingResult()
    
    if len(result.stderr) == 0:
        pingResult.numPacketsTransmitted = re.search("(\d+)(?=\s*packets transmitted)", result.stdout).group(0)
        pingResult.numPacketsRecieved = re.search("(\d+)(?=\s*received)", result.stdout).group(0)
        pingResult.percentPacketLoss = re.search("(\d+)(?=\s*% packet loss)", result.stdout).group(0)

        # Get decimal number before second to last slash (averageRTT)
        # TODO get averageRTT from regex, e.g (\d+)(?=.*?\/.*)
        slashCount = 0
        charStack = []
        for c in reversed(result.stdout):
            if c == '/':
                slashCount += 1
            elif slashCount == 2:
                charStack.insert(0,c)
            if slashCount == 3:
                break
        
        pingResult.averageRTT = ''.join(charStack)      
        
    else:        
          pingResult.errorMsg = re.search('(?<=ping: ).*$',result.stderr).group(0)

    return json.dumps(pingResult.__dict__)


def ping(hostToPing):
    """
    Pings the requested domain-name NUM_PING times
    Prints and returns the results of the ping request, including any error messages
    """
    # Ping the domain 20 times, parse and return the result
    result = subprocess.run(['ping', '-c', NUM_PINGS, '-n', hostToPing], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return parsePingResult(result)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            pingResult = ping(data) 
            conn.sendall(bytes(pingResult, 'utf-8'))