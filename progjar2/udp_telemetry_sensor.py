import socket, struct, random, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('127.0.0.1', 50000)

sensor_id = 42

while True:
    temp = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    packed = struct.pack('!Iff', sensor_id, temp, humidity)
    sock.sendto(packed, server)
    time.sleep(2)

