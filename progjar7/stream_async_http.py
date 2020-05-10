import asyncio

#menggunakan library http
from http import HttpServer

httpserver = HttpServer()

class ServerProtocol(asyncio.Protocol):
    def connection_made(self,transport_socket):
        #dipanggil ketika koneksi baru dibuat
        peername = transport_socket.get_extra_info('peername')
        print('Ada koneksi dari {}' . format(peername))
        #self.transport_socket adalah socket yang bisa dikirimi dan dibaca
        self.transport_socket = transport_socket


    def data_received(self, data: bytes):
        #dipanggil ketika ada data masuk ke socket (self.transport_socket)
        message = data.decode()
        #data stream sudah dikelola oleh library, kita hanya tinggal mengambil dari variabel message
        hasil = httpserver.proses(message)
        #proses, hasil langsung dideliver ke socket yang merequest
        #hasil, sudah berupa bytes, jika menggunakan string, encode lah terlebih dahulu
        self.transport_socket.write(hasil)
        self.transport_socket.close()


loop = asyncio.get_event_loop()
coro = loop.create_server(ServerProtocol, '127.0.0.1',10002)
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