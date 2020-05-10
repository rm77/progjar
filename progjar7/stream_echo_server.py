import asyncio
class ServerProtocol(asyncio.Protocol):
    def connection_made(self,transport_socket):
        #dipanggil ketika koneksi baru dibuat
        peername = transport_socket.get_extra_info('peername')
        print('Ada koneksi dari {}' . format(peername))
        self.transport_socket = transport_socket

        #balasan dapat dikirimkan kapan saja, karena pada dasarnya socket telah terbentuk
        balasan = 'ada apa ya ?' . encode() # string -> bytes agar bisa dikirim ke socket
        self.transport_socket.write(balasan)

    def data_received(self, data: bytes):
        #dipanggil ketika ada data masuk ke socket (self.transport_socket)
        message = data.decode()
        print('Data received',message)
        balasan = 'ada apa ?'.encode()
        self.transport_socket.write(balasan)
        self.transport_socket.close()


loop = asyncio.get_event_loop()
coro = loop.create_server(ServerProtocol, '127.0.0.1',10001)
server = loop.run_until_complete(coro)
try:
    #jalankan server, sampai tombol control-C ditekan
    loop.run_forever()
except KeyboardInterrupt:
    pass

#memastikan semua yang hubungannya dengan socket diakhiri
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()