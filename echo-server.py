# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creates a socket object
    s.bind((HOST, PORT)) # used to associate the socket woth a specific network interface
    s.listen() # enables a server tp acce[t cnnectons makes server listening socket
    conn, addr = s.accept() # The .accept() method blocks execution and waits for an incoming connection, a new socket object is created that is used to talk to the client
    with conn: 
        print(f"Connected by {addr} ")

        while True: # infante while loop to loop over blocking calls: What is a block call? socket func or method that temp suspends your app 
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
