
import socket


def get_my_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = s.gettimeout()
    print(f"timeout : {timeout}")
    s.settimeout(10)
    timeout = s.gettimeout()
    print(f"timeout : {timeout}")
    koneksi = socket.getaddrinfo('www.its.ac.id',80, proto=socket.IPPROTO_TCP)
    print(koneksi)


def get_my_info():
    hostname = socket.gethostname()
    print(f"hostname : {hostname}")

    ip_address = socket.gethostbyname(hostname)
    print(f"ipaddress: {ip_address}")

def get_remote_info():
    remote_host = 'www.espnfc.cosm'
    try:
        remote_host_ip = socket.gethostbyname(remote_host)
        print(f"ip address dari {remote_host} adalah {remote_host_ip}")
    except Exception as ee:
        print(f"ERROR : {str(ee)}")


if __name__=='__main__':
#    get_my_info()
#    get_remote_info()
    get_my_socket()
