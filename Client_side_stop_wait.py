import socket
import random

HOST = '127.0.0.1'
PORT = 12355
s = socket.socket()
s.connect((HOST, PORT))
inp = input("Enter data to be sent: ")
data = (''.join(format(ord(x), 'b') for x in inp))
l = len(data)
print("Size of data is", l)
if l % 7 > 0:
    data = "0"*(7-l % 7)+data
    l = len(data)
print("Size of modified data (with added 0s) is", l)
datalist = []
for i in range(0, l, 7):
    datalist.append(data[i:i+7])
print("Total number of frames is", len(datalist))
i = 0
while i < len(datalist):
    if random.randint(0, 10) > 0:
        s.send((str(i % 2)+datalist[i]).encode())
        print("Transmitted: Frame", i % 2)
    else:
        print("Frame lost while transmission")
        print("Time out!!")
        print("Resending the current frame")
        continue
    rmsg = s.recv(1024).decode()
    if rmsg == "0":
        print("Time out!!")
        print("Resending the current frame")
        continue
    print("Recieved:", rmsg)
    i += 1
print("Transmission complete!!")
s.close()
