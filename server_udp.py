# Server Program for UDP Socket
# Import socket module
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
        print("Input is recievied")
        result = 0
        array = msg.split()
        oprnd1 = array[0]
        opreator = array[1]
        oprnd2 = array[2]
        num1 = int(oprnd1)
        num2 = int(oprnd2)
        if opreator == "+":
            result = num2+num1
        elif opreator == "-":
            result = num1-num2
        elif opreator == "*":
            result = num2*num1
        elif opreator == "/":
            result = num1/num2
        print("Send the result to client")
# change output int to string and encode
        output = str(result)
        sock.sendto(output.encode(), addr)
# Here we are closing the connection
sock.close()