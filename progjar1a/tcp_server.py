import sys
import socket
import logging
import json
import dicttoxml

alldata = dict()
alldata['1']=dict(nomor=1, nama="dean henderson", posisi="kiper")
alldata['2']=dict(nomor=2, nama="luke shaw", posisi="bek kiri")
alldata['3']=dict(nomor=3, nama="aaron wan-bissaka", posisi="bek kanan")
alldata['4']=dict(nomor=4, nama="victor lindelof", posisi="bek tengah kanan")


def proses_request(request_string):
    #format request
    # NAMACOMMAND spasi PARAMETER
    cstring = request_string.split(" ")
    hasil = None
    try:
        command = cstring[0].strip()
        if (command == 'getdatapemain'):
            # getdata spasi parameter1
            # parameter1 harus berupa nomor pemain
            logging.warning("getdata")
            nomorpemain = cstring[1].strip()
            try:
                logging.warning(f"data {nomorpemain} ketemu")
                hasil = alldata[nomorpemain]
            except:
                hasil = None
    except:
        hasil = None
    return hasil


def serialisasi(a):
    #print(a)
    #serialized = str(dicttoxml.dicttoxml(a))
    serialized =  json.dumps(a)
    logging.warning("serialized data")
    logging.warning(serialized)
    return serialized

def run_server(server_address):
    #--- INISIALISATION ---
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    print(f"starting up on {server_address}")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)


    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        print(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print(f"received {data}")
            if data:
                hasil = proses_request(data.decode())
                print(hasil)
                #hasil bisa berupa tipe dictionary
                #harus diserialisasi dulu sebelum dikirim via network
                # Send data
                # some data structure may have complex structure
                # how to send such data structure through the network ?
                # use serialization
                #  example : json, xml

                # complex structure, nested dict
                # all data that will be sent through network has to be encoded into bytes type"
                # in this case, the message (type: string) will be encoded to bytes by calling encode

                hasil = serialisasi(hasil)
                hasil += "\r\n\r\n"
                connection.sendall(hasil.encode())
            else:
               print(f"no more data from {client_address}")
               break
        # Clean up the connection
        connection.close()


if __name__=='__main__':
    run_server(('127.0.0.1', 12000))