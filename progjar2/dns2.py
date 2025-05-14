import socket
import random
import struct

def create_query(domain):
    # Header: [Transaction ID][Flags][Questions][Answer RRs][Authority RRs][Additional RRs]
    tid = random.randint(0, 65535)
    flags = 0x0100  # standard query
    qdcount = 1
    header = struct.pack(">HHHHHH", tid, flags, qdcount, 0, 0, 0)

    def encode_domain(domain):
        parts = domain.split(".")
        result = b''.join([bytes([len(part)]) + part.encode() for part in parts]) + b'\x00'
        return result

    qname = encode_domain(domain)
    qtype = 1    # A
    qclass = 1   # IN
    question = qname + struct.pack(">HH", qtype, qclass)

    return tid, header + question

def parse_response(data):
    tid, flags, qdcount, ancount, _, _ = struct.unpack(">HHHHHH", data[:12])
    offset = 12
    for _ in range(qdcount):
        while data[offset] != 0:
            offset += data[offset] + 1
        offset += 5  # null byte + qtype (2) + qclass (2)

    # Parse answers
    answers = []
    for _ in range(ancount):
        offset += 2  # name (compressed)
        rtype, rclass, ttl, rdlength = struct.unpack(">HHIH", data[offset:offset+10])
        offset += 10
        rdata = data[offset:offset+rdlength]
        offset += rdlength
        if rtype == 1 and rclass == 1:  # A, IN
            ip = ".".join(str(b) for b in rdata)
            answers.append(ip)
    return answers

def dns_query(domain, dns_server='8.8.8.8'):
    tid, query = create_query(domain)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    sock.sendto(query, (dns_server, 53))
    try:
        data, _ = sock.recvfrom(512)
        ips = parse_response(data)
        print(f"[+] {domain} resolved to: {ips}")
    except socket.timeout:
        print("[!] DNS query timed out")
    finally:
        sock.close()

if __name__ == "__main__":
    dns_query("www.its.ac.id",dns_server='8.8.8.8')

