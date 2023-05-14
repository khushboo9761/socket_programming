import socket
import random

s = socket.socket()
print("Socket successfully created")
host = "127.0.0.1"
port = 12355
s.bind((host, port))
print("Socket binded to port", port)
s.listen(1)
print("Socket is listening")
c, addr = s.accept()
print("Got connection from", addr)
msg = ""
smsg = ""
r = 0
while True:
    rmsg = c.recv(1024).decode()
    if not rmsg:
        break
    seq = int(rmsg[0])
    data = chr(int(rmsg[1:], 2))
    if seq == r:
        msg += data
        r ^= 1
        data = "'"+data+"'"
        print("Recieved: Frame", seq, "with Data", data)
    else:
        print("Received duplicate frame")
    if random.randint(0, 10) > 0:
        smsg = "ACK"+str(seq)
        print("Transmitted:", smsg)
    else:
        smsg = "0"
        print("ACK lost while transmission")
    c.sendto(smsg.encode(), (host, port))
print("Collected all frames!!")
print("Overall Message:", msg)
c.close()
