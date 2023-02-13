import socket

def scan_port(host, port):
    # Port tarama işlemi
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        if result == 0:
            # Port aç
            return True
    # Port kapalı
    return False

def scan_ports(host):
    # Taranacak portlar listesi
    ports = [21, 22, 23, 80, 443, 8080]
    for port in ports:
        if scan_port(host, port):
            print(f'{host}:{port} - Açık')
        else:
            print(f'{host}:{port} - Kapalı')

# Tarama işlemini başlat
scan_ports('google.com')
