import socket
# calling server socket method
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12345
sock.bind((udp_host, udp_port))
while True:
    print("Waiting for client...")
    data, addr = sock.recvfrom(1024)
    # receive data from client
    print("Connected to the client", addr)
    msg = data.decode()
    if msg == "Exit":
        print("Connection is over")
        break
    
    else:
         print("Received fromclient:%s" %repr(msg))
         message=input("Enter message to client:")
        
# change output int to string and encode
         sock.sendto(message.encode(), addr)
# Here we are closing the connection
sock.close()