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
		self.servers.append(('127.0.0.1',8000))
		self.servers.append(('127.0.0.1',8001))
		self.servers.append(('127.0.0.1',8002))
#		self.servers.append(('127.0.0.1',9005))
		self.current=0
	def getserver(self):
		s = self.servers[self.current]
		print(s)
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		return s




def ProcessTheClient(connection,address,backend_sock,mode='toupstream'):
		try:
			while True:
				try:
					if (mode=='toupstream'):
						datafrom_client = connection.recv(32)
						if datafrom_client:
								backend_sock.sendall(datafrom_client)
						else:
								backend_sock.close()
								break
					elif (mode=='toclient'):
						datafrom_backend = backend_sock.recv(32)

						if datafrom_backend:
								connection.sendall(datafrom_backend)
						else:
								connection.close()
								break

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
				backend_sock.settimeout(1)
				backend_address = backend.getserver()
				logging.warning(f"{client_address} connecting to {backend_address}")
				try:
					backend_sock.connect(backend_address)

					#logging.warning("connection from {}".format(client_address))
					toupstream = executor.submit(ProcessTheClient, connection, client_address,backend_sock,'toupstream')
					#the_clients.append(toupstream)
					toclient = executor.submit(ProcessTheClient, connection, client_address,backend_sock,'toclient')
					#the_clients.append(toclient)

					#menampilkan jumlah process yang sedang aktif
					jumlah = ['x' for i in the_clients if i.running()==True]
					#print(jumlah)
				except Exception as err:
					logging.error(err)
					pass





def main():
	Server()

if __name__=="__main__":
	main()

