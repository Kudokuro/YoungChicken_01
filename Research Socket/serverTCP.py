import socket
import threading
import asyncio
########################################################
from firewall_login import *
########################################################
namefile = 'erp.efaSsserddapi'
ip = '0.0.0.0'
port = 9999
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(10)
rf = open(namefile[::-1], 'r')
rule  = rf.read()
rf.close()
serv.settimeout(20)
async def checkPredicate(val, rule):
    new = rule.split('\n');
    for i in new:
        if i.find(val) != -1:
            return True
    return False

async def check(ipa, rul):
    predicate = await checkPredicate(ipa, rul)
    return predicate

def handle_client(client_sock, ipa, rul):
    pre = asyncio.run(check(ipa, rul))
    if pre == False:
        client_sock.send(b'You don\'t have access')
        print("NO")
        client_sock.close()
        return
    print('OK')
    req = client_sock.recv(4096)
    print(f"Received {req.decode('utf-8')}")
    client_sock.send(b'OK')
    client_sock.close()

while True:
    c, a = serv.accept()
    print("Accepted connection from %s:%d" % (a[0], a[1]))
    print('Check predicate ..... ',end='');

    cl_ = threading.Thread(target = handle_client, args=(c, a[0], rule))
    cl_.start()
