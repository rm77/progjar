from socket import *
import socket
import time
import sys
import logging
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import asyncio
from http import HttpServer

httpserver = HttpServer()

class ProcessTheClient(asyncio.Protocol):
		def connection_made(self, transport):
			peername = transport.get_extra_info('peername')
			print('Connection from {}'.format(peername))
			self.transport = transport
			self.rcv = ""
		def data_received(self, data: bytes) -> None:
			try:
				d = data.decode()
				self.rcv=self.rcv+d
				if self.rcv[-2:]=='\r\n':
					hasil = httpserver.proses(self.rcv)
					hasil=hasil+"\r\n\r\n".encode()
					self.transport.write(hasil)
					self.transport.close()
					self.rcv=""
			except OSError as e:
				pass



async def Server():
	loop = asyncio.get_running_loop()

	server = await loop.create_server(
		lambda: ProcessTheClient(),
		'0.0.0.0', 8886)

	async with server:
		await server.serve_forever()

if __name__=="__main__":
	asyncio.run(Server())

