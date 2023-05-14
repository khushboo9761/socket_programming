# Server Program for TCP Socket
# Import socket module
import socket

LOCALHOST ="10.1.19.143"#"127.0.0.1"
PORT = 1237#8060
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
		print("Input is received")
		result = 1
		# here we change str to int
		num1 = int(msg)
		# Here we are perform factorial
		for i in range(1, num1+1):
			result = result*i
		print("Send the result to client...")
		# Here we change int to string and
		# after encode, send the output to client
		output = str(result)
		clientConnection.send(output.encode())
# Here we are closing the connection
clientConnection.close()
