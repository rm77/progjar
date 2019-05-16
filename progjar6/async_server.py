import socket
import time
import sys
import asyncore
from http import HttpServer

httpserver = HttpServer()

class ProcessTheClient(asyncore.dispatcher_with_send):
	def handle_read(self):
	   data = self.recv(1024)
	   if data:
	        self.sendall("{}" . format(httpserver.proses(data)))
	   self.close()

class Server(asyncore.dispatcher):
	def __init__(self,portnumber):
                asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
                self.set_reuse_addr()
		self.bind(('',portnumber))
                self.listen(5)
		print "running on port {}" . format(portnumber)

	def handle_accept(self):
                pair = self.accept()
                if pair is not None:
		        sock, addr = pair
		        print >> sys.stderr, 'connection from', repr(addr)
	                handler = ProcessTheClient(sock)

def main():
	portnumber=8887
	try:
	   portnumber=int(sys.argv[1])
	except:
	   pass
	svr = Server(portnumber)
	asyncore.loop()

if __name__=="__main__":
	main()

