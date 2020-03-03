import threading
import glob
import time
import socket

all_files = {}

class FileReaderThread(threading.Thread):
	def __init__(self):
        	threading.Thread.__init__(self)
        	self.daemon=True
	def run(self):
		while True:
			files = glob.glob('*.py')
           		for x in files:
				fp = open(x,'rb')
				all_files[x]=fp.read()
			time.sleep(1)
	
class UdpServer(threading.Thread):
	def __init__(self):
		self.address = '127.0.0.1'
		self.port = 8888
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((self.address,self.port))
        	threading.Thread.__init__(self)
        	self.daemon=True
	def run(self):
		while True:
			data,addr = self.sock.recvfrom(1024)
			for k in all_files:
				self.sock.sendto(all_files[k],addr)
				print("kirim nama file",k," ke ",addr)



def main():
   frt = FileReaderThread()
   frt.start()
   
   udpserver = UdpServer()
   udpserver.start()
   


if __name__ == "__main__":
    try:
      main()
      while True:
        pass
    except KeyboardInterrupt:
      print(" Program Stop ..")
