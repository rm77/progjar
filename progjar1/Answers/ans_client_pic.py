import sys
import socket

ip = ['192.168.122.95', '192.168.122.187']

for x in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip[x], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        print(f"Masukkan nama file dengan ekstension, contoh : sea.png")
        fname = input()
        rname = 'renameFromClient' + '_alpine' + str(x+1) + '_' + fname
        f = open(fname, 'rb')
        img = f.read()
        sock.sendall(img)
        print(f"Sending Image {fname}")

        # Look for the response
        amount_received = 0
        amount_expected = len(img)
        with sock, open(rname, 'wb') as file:
            while amount_received < amount_expected:
                data = sock.recv(2048)
                amount_received += len(data)
                if not data:
                    break
                file.write(data);
    finally:
        print(f"Recieving Image {rname}")
        print(f"Image {fname} Send and Receive Sucessfully")
        sock.close()