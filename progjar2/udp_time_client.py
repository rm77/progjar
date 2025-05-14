import socket, struct, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('127.0.0.1', 7070)

req_id = 1
timestamp = time.time()
msg = struct.pack('!Id', req_id, timestamp)
sock.sendto(msg, server)

data, _ = sock.recvfrom(1024)
resp_id, server_time = struct.unpack('!Id', data)

print(f"Response ID: {resp_id}, Server time: {server_time}")


