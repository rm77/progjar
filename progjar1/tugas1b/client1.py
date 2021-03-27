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
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    print(f"sending {message}")
    sock1.sendall(message.encode())
    sock2.sendall(message.encode())
    # Look for the response
    amount_received1 = 0
    amount_expected1 = len(message)
    while amount_received1 < amount_expected1:
        data1 = sock1.recv(16)
        amount_received1 += len(data1)
        print(f"{data1}")

    amount_received2 = 0
    amount_expected2 = len(message)
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(16)
        amount_received2 += len(data2)
        print(f"{data2}")
finally:
    print("closing")
    sock1.close()
    sock2.close()
