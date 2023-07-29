import socket

# create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to server address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

try:
    # send data to the server
    message = "Hello server!"
    client_socket.sendall(message.encode())

    # Receive the response from the server
    response = client_socket.recv(1024)
    print('Received response: {}'.format(response.decode()))

finally:
    # clean up the connection
    client_socket.close()