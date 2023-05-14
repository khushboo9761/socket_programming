import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12380     # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    #with conn:
    print('Connected by', addr, conn)
      #while True:
    data = conn.recv(1024)
    strings = data.decode('utf8')
#get the num
    num = int('strings') 
    def factorial(num):
        if n < 0:
          return 0
        elif n == 0 or n == 1:
         return 1
        else:
         fact = 1
        while(n > 1):
            fact *= n
            n -= 1
            return fact
conn.send(str(factorial(num)).encode('utf8'))        
            #if not data:
                #break

       
     
# Driver Code
#print("Factorial of",a,"is",factorial(a))
#print ("Received Messages:",data.decode('utf-8')," from",addr)
#s.sendall(bytes(str(factorial(num)),'utf8'))
    
             
