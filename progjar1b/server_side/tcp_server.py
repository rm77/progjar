import sys
import socket
import logging
import json
import os
import ssl

services = dict()


def serving(func):
    def wrapper_serving(*args,**kwargs):
        services[func.__name__]=1
        return func(*args,**kwargs)
    return wrapper_serving


def serialisasi(a):
    serialized =  json.dumps(a)
    logging.warning("serialized data")
    logging.warning(serialized)
    return serialized

def deserialisasi(a):
    deserialized =  json.loads(a)
    logging.warning("deserialized data")
    logging.warning(deserialized)
    return deserialized


def proses_request(request_string):
    """
      the format:

      json:
        - namafungsi : string
        - parameter : json dictionary / object
    """
    try:
        request = deserialisasi(request_string)
        namafungsi = request['namafungsi']
        parameter = request['parameter']
        hasil = locals()[namafungsi](**parameter)
        return serialisasi(hasil)
    except Exception as ee:
        return False


def run_server(server_address,is_secure=False):
    # ------------------------------ SECURE SOCKET INITIALIZATION ----
    if is_secure == True:
        print(os.getcwd())
        cert_location = os.getcwd() + '/certs/'
        socket_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        socket_context.load_cert_chain(
            certfile=cert_location + 'domain.crt',
            keyfile=cert_location + 'domain.key'
        )
    # ---------------------------------

    #--- INISIALISATION ---
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    logging.warning(f"starting up on {server_address}")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1000)


    while True:
        # Wait for a connection
        logging.warning("waiting for a connection")
        koneksi, client_address = sock.accept()
        logging.warning(f"Incoming connection from {client_address}")
        # Receive the data in small chunks and retransmit it

        try:
            if is_secure == True:
                connection = socket_context.wrap_socket(koneksi, server_side=True)
            else:
                connection = koneksi

            selesai=False
            data_received="" #string
            while True:
                data = connection.recv(32)
                logging.warning(f"received {data}")
                if data:
                    data_received += data.decode()
                    if "\r\n\r\n" in data_received:
                        selesai=True

                    if (selesai==True):

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

                        #fungsi proses_request sudah memasukkan pemanggilan serialisasi
                        hasil = proses_request(data_received)
                        logging.warning(f"hasil proses: {hasil}")
                        hasil += "\r\n\r\n"
                        connection.sendall(hasil.encode())
                        selesai = False
                        data_received = ""  # string
                        break

                else:
                   logging.warning(f"no more data from {client_address}")
                   break
            # Clean up the connection
        except ssl.SSLError as error_ssl:
            logging.warning(f"SSL error: {str(error_ssl)}")

