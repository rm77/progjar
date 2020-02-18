import socket
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
angka = 0
while True:
    angka = angka+1
    msg = " ini angka {} " . format(angka)
    print(msg)
    sock.sendto(msg.encode(), (TARGET_IP, TARGET_PORT))
    time.sleep(1)

