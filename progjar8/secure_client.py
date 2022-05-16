import os
import socket
import ssl
import logging

def create_socket(destination_address='localhost',port=10000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (destination_address, port)
    logging.warning(f"connecting to {server_address}")
    sock.connect(server_address)
    return sock

def create_secure_socket(destination_address='localhost',port=10000):
    #get it from https://curl.se/docs/caextract.html

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode=ssl.CERT_OPTIONAL
    context.load_verify_locations(os.getcwd() + '/domain.crt')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (destination_address, port)
    logging.warning(f"connecting to {server_address}")
    sock.connect(server_address)
    secure_socket = context.wrap_socket(sock,server_hostname=destination_address)
    print(secure_socket.getpeercert())
    return secure_socket


def send_server(sock_connection,request_content):
    logging.warning('send request -->')
    sock_connection.sendall(request_content.encode())
    buffer = ""
    while True:
        logging.warning('<--receive content')
        data = sock_connection.recv(32).decode()
        if (data):
            buffer += data
        else:
            break
    return buffer



def run():
    conn = create_secure_socket('localhost',8443)
    http_request_content = "GET / HTTP/1.1\r\n" \
                           "Host: localhost\r\n" \
                           "\r\n" \
                           "\r\n"
    hasil = send_server(sock_connection=conn,
                        request_content=http_request_content)
    print(hasil)


if __name__=='__main__':
    run()