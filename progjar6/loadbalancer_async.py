import socket
import time
import sys
import asyncore

class BalancerHost:
    def __init__(self):
        self.current_host=0
        self.hosts=[('localhost',8887),('localhost',8887)]
    def getserver(self):
        if (self.current_host>=len(self.hosts)):
            self.current_host=0
        return self.hosts[self.current_host]


balancerhost = BalancerHost()


class Proxy(asyncore.dispatcher_with_send):
    def __init__(self):
        self.create_connection(balancerhost.getserver())
    def handle_connect(self):

    def (self,data):

class ProcessTheClient(asyncore.dispatcher_with_send):
	def handle_read(self):
	   data = self.recv(1024)
	   if data:
	        self.sendall("{}" . format(balancer.proses(data)))
	   self.close()

class Server(asyncore.dispatcher):
	def __init__(self):
                asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
                self.set_reuse_addr()
		self.bind(('0.0.0.0',8885))
                self.listen(5)

	def handle_accept(self):
                pair = self.accept()
                if pair is not None:
		        sock, addr = pair
		        print >> sys.stderr, 'connection from', repr(addr)
	                handler = ProcessTheClient(sock)

def main():
	svr = Server()
	asyncore.loop()

if __name__=="__main__":
	main()

