from socket import *
import socket
import time
import sys
import logging
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from http import HttpServer

class BackendList:
	def __init__(self):
		self.servers=[]
		self.servers.append(('10.21.84.254',8000))
		self.servers.append(('10.21.84.254',8001))
		self.servers.append(('10.21.84.254',8002))
#		self.servers.append(('127.0.0.1',9005))
		self.current=0
	def getserver(self):
		s = self.servers[self.current]
		print(s)
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		return s




def ProcessTheClient(connection,address,backend_sock):
		try:
			while True:
				try:
					datafrom_client = connection.recv(1024)
					if datafrom_client:
							backend_sock.sendall(datafrom_client)
					else:
							backend_sock.close()

					datafrom_backend = backend_sock.recv(1024)

					if datafrom_backend:
							connection.sendall(datafrom_backend)
					else:
							connection.close()

				except OSError as e:
					pass
		except Exception as ee:
			logging.warning(f"error {str(ee)}")
		connection.close()
		return



def Server():
	the_clients = []
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	backend = BackendList()

	my_socket.bind(('0.0.0.0', 44444))
	my_socket.listen(1)

	with ProcessPoolExecutor(20) as executor:
		while True:
				connection, client_address = my_socket.accept()
				backend_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				backend_address = backend.getserver()
				logging.warning(f"{client_address} connecting to {backend_address}")
				backend_sock.connect(backend_address)

				#logging.warning("connection from {}".format(client_address))
				p = executor.submit(ProcessTheClient, connection, client_address,backend_sock)
				the_clients.append(p)
				#menampilkan jumlah process yang sedang aktif
				jumlah = ['x' for i in the_clients if i.running()==True]
				#print(jumlah)





def main():
	Server()

if __name__=="__main__":
	main()

