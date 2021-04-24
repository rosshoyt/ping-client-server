import subprocess
import socket
import json
from _thread import *
from PingResult import PingResult

HOST = '127.0.0.1'
PORT = 10800
NUM_PINGS = '20'

def parsePingResult(result):
    """
    """
    print(result.stdout)
    print(result.stderr)

    pingResult = PingResult()
    pingResult.numPacketsRecieved = 10
    pingResult.numPacketsTransmitted = 10
    pingResult.averageRTT = 100

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