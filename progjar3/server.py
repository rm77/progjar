import sys
import socket
import logging
import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
logging.warning(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
	# Wait for a connection
	logging.warning("opening connection")
	connection, client_address = sock.accept()
	logging.warning(f"connection from {client_address}")
	# Receive the data in small chunks and retransmit it
	while True:
		waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%s")
		data = connection.recv(32)
		logging.warning(f"{waktu} received {data}")
		if data:
			logging.warning("[SERVER] {waktu} sending data back to the client")
			connection.sendall(data)
		else:
			logging.warning(f"[SERVER] {waktu} no more data from {client_address}")
			break
# Clean up the connection
connection.close()
