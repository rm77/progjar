import sys
import socket
import json
import logging
import xmltodict

server_address = ('127.0.0.1', 12000)


def getdatapemain(nomor=0):
    cmd=f"getdatapemain {nomor}"
    hasil = send_command(cmd)
    return hasil


def send_command(command_str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    logging.warning(f"connecting to {server_address}")
    try:
        logging.warning(f"sending message ")
        sock.sendall(command_str.encode())
        # Look for the response, waiting until socket is done (no more data)
        data_received="" #empty string
        while True:
            #socket does not receive all data at once, data comes in part, need to be concatenated at the end of process
            data = sock.recv(16)
            if data:
                #data is not empty, concat with previous content
                data_received += data.decode()
                if "\r\n\r\n" in data_received:
                    break
            else:
                # no more data, stop the process by break
                break
        # at this point, data_received (string) will contain all data coming from the socket
        # to be able to use the data_received as a dict, need to load it using json.loads()
        hasil = json.loads(data_received)
        logging.warning("data received from server:")
        return hasil
    except:
        logging.warning("error during data receiving")
        return False


if __name__=='__main__':
    h = getdatapemain(1)
    print(h['nama'],h['nomor'])
    h = getdatapemain(2)
    print(h['nama'],h['nomor'])
