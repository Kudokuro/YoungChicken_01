import socket
import argparse
#########################################################################
args = argparse.ArgumentParser(description="send data into network");
#Add argument assign host
args.add_argument( 
        "--host", 
        "-f",
        "--HOST",
        "-F",
        dest="host", 
        type = str,
        default=socket.gethostbyname(socket.gethostname()))
#Add argument assign port
args.add_argument(
        "-p",
        "--port",
        "-P",
        "--PORT",
        dest="port",
        type = int,
        default = 5858,
        )
#Add argument assign data
args.add_argument(
        "-d",
        "-D",
        "--DATA",
        "--data",
        dest = "data",
        default = "hello",
        )
#Add argument assign protocol:
args.add_argument(
        '-pro',
        '-PRO',
        '--protocol',
        '--PROTOCOL',
        dest = 'prtcl',
        default = 'TCP'
        )
#Add argument assign user:
args.add_argument(
        '-u',
        '--user',
        '-U',
        '--USER',
        dest = 'user',
        default = 'admin'
        )
#Add argument assign pass
args.add_argument(
        '-pwd',
        '-PWD',
        '--PASSWD',
        '--passwd',
        dest = 'pwd',
        default = 'admin'
        )
_input = args.parse_args()
###########################################################################
def RawDataInputToUpper(value):
    return value.upper() if type(value) is str else value

def sendData_UDP(host, port, data, user, passw):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto((data + "$" + user + "$" + passw).encode(), (host, port))
    data, addr = client.recvfrom(4096)
    if type(data) is str:
        pass
    else:
        data = data.decode('utf-8')

    if "OK" in data:
        return True
    else:
        return False


def sendData_TCP(host, port, data, user, passw):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send((data + "$" + user + "$" + passw).encode())
    data = client.recv(4096)
    if type(data) is str:
        pass
    else:
        data = data.decode('utf-8')

    if "OK" in data:
        return True, data
    else:
        return False, data


def main():
    global _input
    _input.prtcl = RawDataInputToUpper(_input.prtcl)
    _input.host = socket.gethostbyname(_input.host)
    if _input.prtcl == "UDP":
        re, _ = sendData_UDP(
                _input.host, 
                _input.port, 
                _input.data, 
                _input.user, 
                _input.pwd)
        if re:
            print("Yeah it run")
            return 0
        else:
            print(_)
            return -1
    elif _input.prtcl == "TCP":
        re, _ = sendData_TCP(
                _input.host, 
                _input.port, 
                _input.data,
                _input.user,
                _input.pwd)
        if re:
            print("Yeah it run")
            return 0
        else:
            print(_)
            return -1
if __name__ == "__main__":
    main()
