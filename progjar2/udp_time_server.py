import socket, struct, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 7070))

while True:
    data, addr = sock.recvfrom(1024)
    req_id, client_time = struct.unpack('!Id', data)
    print(f"Received from {addr}: ID {req_id}, Client time {client_time}")
    response = struct.pack('!Id', req_id, time.time())
    sock.sendto(response, addr)

