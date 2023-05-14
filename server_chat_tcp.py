import socket

LOCALHOST = "127.0.0.1"
PORT = 8060
# calling server socket method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)  # here we are listening one client
print("Server started")
print("Waiting for client request..")
# Here server socket is ready for get input from the user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
# Running infinite loop
while True:
	data = clientConnection.recv(1024)
	msg = data.decode()
	if msg == "Over":
		print("Connection is Over")
		break
	else:
         print("Received fromclient:%s" %repr(msg))
         message=input("Enter message to client:")
         clientConnection.send(message.encode())
# Here we are closing the connection
clientConnection.close()
