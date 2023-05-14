import socket

SERVER = "127.0.0.1"
PORT = 8060
# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))
# Running a infinite loop
print("Type 'Over' to terminate")
while True:
	# here we get the input from the user
	inp = input("Enter the message: ")
	# To terminate the server connection  type 'Over'
	if inp == "Over":
		client.send(inp.encode())
		print("Connection is Over")
		break
	else:
		# Here we send the user input
		# to server socket by send Method
		client.send(inp.encode())
		# Here we received output from the server socket
		answer = client.recv(1024)
		print("Answer is "+answer.decode())


client.close()
