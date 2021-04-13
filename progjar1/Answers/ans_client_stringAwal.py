import sys
import socket
import random
import string

ip = ['192.168.122.155', '192.168.122.21']

for x in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip[x], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
        print(f"sending {message}")
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(2048)
            amount_received += len(data)
            print(f"{data}")
    finally:
        print("closing")
        sock.close()