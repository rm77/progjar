import sys
import socket
import json
import logging
import ssl
import os

server_address = ('www.its.ac.id', 443)
server_address = ('www.ietf.org',443)


def make_socket(destination_address='localhost', port=12000):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (destination_address, port)
        logging.warning(f"connecting to {server_address}")
        sock.connect(server_address)
        return sock
    except Exception as ee:
        logging.warning(f"error {str(ee)}")


def make_secure_socket(destination_address='localhost', port=10000):
    try:
        # get it from https://curl.se/docs/caextract.html

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        context.load_verify_locations(os.getcwd() + '/domain.crt')

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (destination_address, port)
        logging.warning(f"connecting to {server_address}")
        sock.connect(server_address)
        secure_socket = context.wrap_socket(sock, server_hostname=destination_address)
        logging.warning(secure_socket.getpeercert())
        return secure_socket
    except Exception as ee:
        logging.warning(f"error {str(ee)}")



def send_command(command_str, is_secure=False):
    alamat_server = server_address[0]
    port_server = server_address[1]
    #    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # gunakan fungsi diatas
    if is_secure == True:
        sock = make_secure_socket(alamat_server, port_server)
    else:
        sock = make_socket(alamat_server, port_server)

    logging.warning(f"connecting to {server_address}")
    try:
        logging.warning(f"sending message ")
        sock.sendall(command_str.encode())
        logging.warning(command_str)
        # Look for the response, waiting until socket is done (no more data)
        data_received = ""  # empty string
        while True:
            # socket does not receive all data at once, data comes in part, need to be concatenated at the end of process
            data = sock.recv(2048)
            if data:
                # data is not empty, concat with previous content
                data_received += data.decode()
                if "\r\n\r\n" in data_received:
                    break
            else:
                # no more data, stop the process by break
                break
        # at this point, data_received (string) will contain all data coming from the socket
        # to be able to use the data_received as a dict, need to load it using json.loads()
        hasil = data_received
        logging.warning("data received from server:")
        return hasil
    except Exception as ee:
        logging.warning(f"error during data receiving {str(ee)}")
        return False

#> GET / HTTP/1.1
#> Host: www.its.ac.id
#> User-Agent: curl/8.7.1
#> Accept: */*
#>

if __name__ == '__main__':
    cmd = f"""GET /rfc/rfc2616.txt HTTP/1.1
Host: www.ietf.org
User-Agent: myclient/1.1
Accept: */*

"""
    hasil = send_command(cmd, is_secure=True)
    print(hasil)
