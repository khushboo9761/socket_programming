#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12380       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(b'Enter the number:')
    a=int(input())
    s.sendall(str(a).encode('utf8'))
    data = s.recv(1024)
    #print("data from server is::"+data.decode('utf-8'))
#print('Received', repr(data))
   
# decode to unicode string 
    strings = data.decode('utf8')
#get the num
    num = int('strings')
    print(f"The factorial is {num}")
    