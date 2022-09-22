import socket

port = 3000
max_size = 70000

#create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#letting the OS bind the socket object instead of explicity doing it
#ephermal ports

hostname = '127.0.0.1'

while True:
    s.connect((hostname, port))
    message = input("Joey:")
    data = message.encode('ascii')
    s.send(data)
    
    data = s.recv(max_size)
    text = data.decode('ascii')
    print(f"Phoebe:{text}")
