# run server implemtation in one terminal and client implementation in another
import socket

# create a socket object
client_socket = socket.socket()

# Define server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# send data to the server
message = "Hello from client"
client_socket.send(message.encode('utf-8'))

# receive a response from server
response = client_socket.recv(1024).decode('utf-8')
print('Response', response)

# close the client socket
client_socket.close()