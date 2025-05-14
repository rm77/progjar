import struct

magic = b'MAGC'         # 4 bytes
version = 1             # 1 byte
length = 128            # 2 bytes (unsigned short)
flags = 0b01010101      # 1 byte

packet = struct.pack('!4sBHB', magic, version, length, flags)
print(packet)

