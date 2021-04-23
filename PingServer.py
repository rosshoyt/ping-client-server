import subprocess
import socket

HOST = '127.0.0.1'
PORT = 10800

def ping(hostToPing):
    """
    Pings the requested domain-name 20 times
    Prints and returns the results of the ping request, including any error messages
    """
    
    # Ping the domain 20 times and store the result
    result = subprocess.run(['ping', '-c', '20', '-n', hostToPing], stderr=subprocess.PIPE, encoding='utf-8')

    print(result.stdout)
    print(result.stderr)

    return result

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
            conn.sendall(bytes('all set', 'utf-8'))