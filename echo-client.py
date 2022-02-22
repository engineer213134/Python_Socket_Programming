# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Creates a socket object (s) 
    s.connect((HOST, PORT)) # connects to the server using HOST & PORT parameters 
    s.sendall(b"Hello, world") # Sends message to server 
    data = s.recv(1024) # This calls the server reply

print(f"Received {data!r}") #This prints the servers reply
