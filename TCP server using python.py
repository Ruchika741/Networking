import socket

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections(starts the connection)
server_socket.listen()
print('Server is listening on {}:{}'.format(*server_address))

while True:
    # wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(*client_address))

    try:
        while True:
            #Receive data from the client. We can receive only 1024 or 1KB of data here
            data = client_socket.recv(1024)
            if data:
                # Process the received data
                print("Received data: {}".format(data.decode()))

                # send a response back to the client
                response = 'Message received: {}'.format(data.decode())
                client_socket.sendall(response.encode())
            else:
                # No more data from the client
                print("No more data from {}:{}".format(*client_address))
                break
    finally:
        # clean up the connection
        client_socket.close()
        # server_socket.close()