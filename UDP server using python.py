import socket

# define the server address and port
server_address = ('localhost', 5000)

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
sock.bind(server_address)

# Listen for incoming data
print(f"UDP server listening on {server_address}")

while True:
    # Receive data from client
    data, address = sock.recvfrom(1024)

    # Decode the reveived data
    message = data.decode('utf-8')

    # Print the received message and client address
    print(f"Recieved message from: {message} from {address}")

    # send a response back to client
    response = "Response from server"
    sock.sendto(response.encode('utf-8'), address)