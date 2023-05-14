
import socket
import json
with open('data.json') as f:
  # Reading from file
 data = json.loads(f.read())
   
# Iterating through the json
# list
for i in data['dns_table']:
    print(i)
  
datar = json.dumps(i)    
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Starting Server....")
s.bind(("127.0.0.1",1234))
while True:
    datar,address=s.recvfrom(1024)
    print(f"{address}wants to fetch data!")
    datar=datar.decode()
    
    ip=i.get(datar,"Not Found!").encode()
    send=s.sendto(ip,address)
