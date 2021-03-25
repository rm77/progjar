import sys
import socket

ipserver = ['192.168.122.72', '192.168.122.171']

for i in range(2):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = (ipserver[i], 10000)
	print(f"connecting to {server_address}")
	sock.connect(server_address)


	try:
		# Send data
		send_filename = 'sendimage.jpg'
		recv_filename = 'recvimage.jpg'
		size_img = 0;
		with open(send_filename, 'rb') as file:
		    sendfile = file.read() 
		sock.sendall(sendfile)
		print(f"sending {send_filename}")
		# Look for the response
		amount_received = 0
		amount_expected = len(sendfile)
		with sock,open(recv_filename,'wb') as file:
		    while amount_received < amount_expected:
		        data = sock.recv(16)
		        amount_received += len(data)
		        if not data:
		            break
		        file.write(data);
	finally:
		print(f"{recv_filename} done")
		sock.close()
