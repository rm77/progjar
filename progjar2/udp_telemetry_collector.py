import socket, struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 50000))

while True:
    data, addr = sock.recvfrom(1024)
    sensor_id, temp, hum = struct.unpack('!Iff', data)
    print(f"Sensor {sensor_id} @ {addr} | Temp: {temp:.1f}°C | Humidity: {hum:.1f}%")

