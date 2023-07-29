import socket
import sys

try:
    # s is a socket instance, AF_INET refers to the address-family ipv4. 
    # The SOCK_STREAM means connection-oriented TCP protocol. 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Successfully created')
except socket.error as err:
    print("Socket creation failed with %s" %(err))

# default port for socket
port = 80

# find the IP of server
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")
