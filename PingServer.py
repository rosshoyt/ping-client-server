import subprocess
import socket
import json
import re
from threading import Thread
from PingResult import PingResult

HOST = '127.0.0.1'
PORT = 10800
NUM_PINGS = '20'

def parsePingResult(result, domain):
    """
    Returns a JSON version of a PingResult class containing data about the PING results
    """
    pingResult = PingResult(domainName = domain.decode('UTF-8'))
    # If no error msg, we'll parse the data fields for the ping result container class
    if len(result.stderr) == 0:
        pingResult.numPacketsTransmitted = int(re.search("(\d+)(?=\s*packets transmitted)", result.stdout).group(0))
        pingResult.numPacketsRecieved = int(re.search("(\d+)(?=\s*received)", result.stdout).group(0))
        pingResult.percentPacketLoss = float(re.search("(\d+)(?=\s*% packet loss)", result.stdout).group(0))

        # If we had 100% packet loss, we can't parse the averageRTT
        if pingResult.percentPacketLoss == 100.0:
            pingResult.averageRTT = 'Not applicable: all packets lost'
        else: 
            # Extract averageRTT from the decimal number before second to last slash
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
        # add the error message
        pingResult.errorMsg = re.search('(?<=ping: ).*$',result.stderr).group(0)

    return json.dumps(pingResult.__dict__)

def ping(hostToPing):
    """
    Pings the requested domain-name NUM_PING times
    Returns the results of the ping request, including any error messages
    """
    # Ping the domain 20 times, parse and return the result
    result = subprocess.run(['ping', '-c', NUM_PINGS, '-n', hostToPing], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return parsePingResult(result, hostToPing)

def clientThread(conn, addr):
    """
    Function that a thread can use to communicate with a client
    """
    with conn: 
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Pinging', data.decode('utf-8'), '...')
            pingResult = ping(data)
            print('Sending response with ping results to client', addr)
            conn.sendall(bytes(pingResult, 'utf-8'))

# Start the server, listen for connections, and spawn a thread when a connection occurs
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(6) # queue up to 6 requests
    while True:
        conn, addr = s.accept()
        print('Connected to', addr)
        try:
            Thread(target=clientThread, args=(conn, addr)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
    soc.close()