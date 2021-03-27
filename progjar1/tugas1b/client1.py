import sys
import socket

# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address1 = ('192.168.122.74', 10000)
server_address2 = ('192.168.122.216', 10000)
print(f"connecting to {server_address1}")
print(f"connecting to {server_address2}")
sock1.connect(server_address1)
sock2.connect(server_address2)

try:
    # Send data
    message1 = "logoyahoo.png"
    message2 = "logogoogle.jpg"
    fname1 = open(message1,'rb')
    fname2 = open(message2,'rb')
    img1 = fname1.read()
    img2 = fname2.read()
    print(f"sending {message1}")
    print(f"sending {message2}")
    sock1.sendall(img1)
    sock2.sendall(img2)

    # Look for the response
    amount_received1 = 0
    amount_expected1 = len(img1)
    msg1 = 'terima1' + message1
    #fname1b = open(msg1,'wb')
    #fname2b = open(msg2,'wb')
    with sock1, open(msg1,'wb') as file:
        while amount_received1 < amount_expected1:
            data1 = sock1.recv(16)
            amount_received1 += len(data1)
            if not data1:
                break
            file.write(data1)

    amount_received2 = 0
    amount_expected2 = len(img2)
    msg2 = 'terima2' + message2
    with sock2, open(msg2,'wb') as file:
        while amount_received2 < amount_expected2:
            data2 = sock2.recv(16)
            amount_received2 += len(data2)
            if not data2:
                break
            file.write(data2)
finally:
    print(f"received {msg1}")
    print(f"received {msg2}")
    sock1.close()
    sock2.close()
