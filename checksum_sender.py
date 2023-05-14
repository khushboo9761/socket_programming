import socket
HOST='127.0.0.1'
PORT=12346

def getChecksum(data,k):
    parts=[data[i:i+k] for i in range(0,len(data),k)]
    print("Partitions of data:",parts)
    sum='0'*k
    for x in parts:
        sum=bin(int(x,2)+int(sum,2))[2:]
        if len(sum)>k:
            x=len(sum)-k
            sum=bin(int(sum[0:x],2)+int(sum[x:],2))[2:]
        if len(sum)<k:
            sum='0'*(k-len(sum))+sum
    checksum=''
    for i in sum:
        if i=='1':
            checksum+='0'
        else:
            checksum+='1'
    return checksum

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    inp=input("Enter data to be sent: ")
    data=(''.join(format(ord(x),'b') for x in inp))
    print("Data(binary format):",data)
    print("Size of data is",len(data))
    size=int(input("Enter the partition size: "))
    while len(data)%size!=0:
        data='0'+data
    print("Updated data(with added 0s):",data)
    print("Size of updated data:",len(data))
    checkSum=getChecksum(data,size)
    print("Checksum:",checkSum)
    smsg=data+checkSum+' '+str(size)
    s.send(smsg.encode())
    rmsg=s.recv(1024).decode()
    print("Received feedback from server:",rmsg)
    con=input("Do you want to continue?(y/n): ")
    if con=='n':
        break
    print(" ")
s.close()
