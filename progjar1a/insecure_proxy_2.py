import socket
import os
import logging
from threading import Thread

def make_realserver_socket(server_address):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.warning(f"connecting to {server_address}")
        sock.connect(server_address)
        return sock
    except Exception as ee:
        logging.warning(f"error {str(ee)}")


def from_client_torealserver(realserver_connection,client_connection):
    while True:
        data = client_connection.recv(32)
        logging.warning(f"received data from client {data}")
        if data:
            logging.warning(f"sending to realserver {data}")
            realserver_connection.sendall(data)
        else:
            logging.warning(f"no more data")
            break

def from_realserver_to_client(realserver_connection,client_connection):
    while True:
        data = realserver_connection.recv(32)
        logging.warning(f"received data from realserver {data}")
        if data:
            logging.warning(f"sending to client {data}")
            client_connection.sendall(data)
        else:
            logging.warning(f"no more data")
            break


def run_proxy_server(proxy_address,realserver_address):
    #--- SERVER INISIALISATION ---
    proxysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    logging.warning(f"starting up on {realserver_address}")
    proxysock.bind(proxy_address)
    # Listen for incoming connections
    proxysock.listen(1)
    while True:
        # Wait for a connection
        logging.warning("waiting for a connection")
        client_connection, client_address = proxysock.accept()
        logging.warning(f"Incoming connection from {client_address}")
        realserver_connection = make_realserver_socket(realserver_address)
        Thread(target=from_client_torealserver,args=(realserver_connection,client_connection)).start()
        Thread(target=from_realserver_to_client,args=(realserver_connection,client_connection)).start()

if __name__=='__main__':
    try:
        proxy_address = ('0.0.0.0',16000)
        realserver_address = ('172.16.16.103',15000)
        run_proxy_server(proxy_address,realserver_address)
    except KeyboardInterrupt:
        logging.warning("Control-C: Program berhenti")
        exit(0)
    finally:
        logging.warning("seelsai")