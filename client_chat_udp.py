import socket
# Making a socket instance
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # For UDP
udp_host = socket.gethostname()
udp_port = 12345
print ("UDP target IP:", udp_host)
print ("UDP target Port:", udp_port)
print("Type 'Exit' to terminate the connection!!! ")
while True:
    
    # here we get the input from the user
    inp = input("Enter the message: ")
    # To terminate the server connection  type 'Exit'
    if inp == "Exit":
        sock.sendto(inp.encode('utf-8'), (udp_host, udp_port))
        break
    else:
        # Here we send the user input
        # to server socket by send Method
        sock.sendto(inp.encode('utf-8'), (udp_host, udp_port))
        # Here we received output from the server socket
        data, addr = sock.recvfrom(1024)
        print("Answer is::"+data.decode('utf-8'))
print("Connection is over")
sock.close()