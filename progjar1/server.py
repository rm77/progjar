import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(32)
        print(f"received {data}")
        if data:
            print("sending back data")
            connection.sendall(data)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client_address}")
           break
    # Clean up the connection
    connection.close()
