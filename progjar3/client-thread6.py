import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('a', (TARGET_IP, TARGET_PORT))
while True:
	data,addr = sock.recvfrom(1024)
	print data

