import socket
import threading

ip = '0.0.0.0'
port = 9999
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(10)
serv.settimeout(20)

def handle_client(client_sock):
    req = client_sock.recv(4096)
    print(f"Received {req}")
    client_sock.send(b'OK')
    client_sock.close()

while True:
    c, a = serv.accept()
    print("Accepted connection from %s:%d" % (a[0], a[1]))
    cl_ = threading.Thread(target = handle_client, args=(c,))
    cl_.start()
serv.settimeout(None)
