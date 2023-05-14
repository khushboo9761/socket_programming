import socket

def getChecksum(data,k):
    parts=[data[i:i+k] for i in range(0,len(data),k)]
    sum='0'*k
    for x in parts:
        sum=bin(int(x,2)+int(sum,2))[2:]
        if(len(sum)>k):
            x=len(sum)-k
            sum=bin(int(sum[0:x],2)+int(sum[x:],2))[2:]
        if(len(sum)<k):
            sum='0'*(k-len(sum))+sum
    checksum=''
    for i in sum:
        if i=='1':
            checksum+='0'
        else:
            checksum+='1'
    return checksum

s=socket.socket()
print("Socket successfully created")
host="127.0.0.1"
port=12346
s.bind((host,port))
print("Socket binded to port",port)
s.listen(1)
print("Socket is listening")
c,addr=s.accept()
print("Got connection from", addr)
while True:
    rmsg=c.recv(1024).decode()
    if not rmsg:
        break
    temp=rmsg.split()
    data=temp[0]
    size=int(temp[1])
    ans=getChecksum(data,size)
    print("Answer is",ans)
    res='0'*size
    if ans==res:
        c.sendto(("No Error Found in data").encode(),(host, port))
    else:
        c.sendto("Error Found in data".encode(),(host, port))
        break
c.close()
