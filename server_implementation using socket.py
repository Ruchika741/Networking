# run server implemtation in one terminal and client implementation in another
import socket

server_socket  = socket.socket()
print("Socket created successfully")

# reserve a port in your computer
port = 12345

# next bind our server to the port.
# Passing an empty string means that the server can listen to incoming connections from other computers as well. 
# If we would have passed 127.0.0.1/localhost then it would have listened to only those calls made within the local computer
server_socket.bind(('', port))
print('Socket binded to %s' %(port))

# put the server into listening mode.5 here means that 5 connections are kept waiting if the server 
# is busy and if a 6th socket tries to connect then the connection is refused.
server_socket.listen(5)
print("socket is listening")

# accept all incoming connections and close those connections after a thank you message to all connected sockets.
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print('Received:', data)

    # Send a response back to the client
    response = 'Hello from the server!'
    client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()


