import socket

max_size = 70000 #maximum size of message to be received.
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating a socket object

#IP address to which server will listen to when message is received
#defining it as localhost
hostname = '127.0.0.1'

#bind the created socket with the host machine on port 3000
s.bind((hostname, port))

print(f"Server is listening on {s.getsockname()}")

#listen infinitely until closed manually
while True:
    data, clientAdd = s.recvfrom(max_size)
    #decode bytes data to ascii type
    message = data.decode('ascii')
    print(f"Joey:{message}")
    message_send = input("Phoebe:")
    data = message_send.encode('ascii')
    s.sendto(data, clientAdd)
