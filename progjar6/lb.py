import socket
import time
import sys
import asyncore


class BackendList:
	def __init__(self):
		self.servers=[]
		self.servers.append(('127.0.0.1',9001))
		self.servers.append(('127.0.0.1',9002))
		self.servers.append(('127.0.0.1',9003))
		self.servers.append(('127.0.0.1',9004))
		self.servers.append(('127.0.0.1',9005))
		self.current=0
	def getserver(self):
		s = self.servers[self.current]
		self.current=self.current+1
		if (self.current>=len(self.servers)):
			self.current=0
		return s

class Backend(asyncore.dispatcher_with_send):
	def __init__(self,targetaddress):
	    asyncore.dispatcher_with_send.__init__(self)
	    self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
	    self.connect(targetaddress)
	    self.connection = self
	def handle_read(self):
	    try:
	    	self.client_socket.sendall(self.recv(8192))
	    except:
 		pass
	def handle_close(self):
	    try:
	    	self.close()
	    	self.client_socket.close()
	    except:
		pass

class ProcessTheClient(asyncore.dispatcher):
	def handle_read(self):
	   data = self.recv(8192)
	   if data:
		self.backend.client_socket = self
		self.backend.sendall(data)
	def handle_close(self):
	    self.close()

class Server(asyncore.dispatcher):
	def __init__(self):
                asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
                self.set_reuse_addr()
		self.bind(('0.0.0.0',8885))
                self.listen(5)
		self.bservers = BackendList()

	def handle_accept(self):
                pair = self.accept()
                if pair is not None:
		        sock, addr = pair
		        print >> sys.stderr, 'connection from', repr(addr)
			backend = Backend(self.bservers.getserver())
	                handler = ProcessTheClient(sock)
			handler.backend = backend



def main():
	svr = Server()
	asyncore.loop()

if __name__=="__main__":
	main()

