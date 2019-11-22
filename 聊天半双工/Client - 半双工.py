import socket

class Client(object):
    def __init__(self,socket,addr,buffsize):
        self.socket=socket
        self.addr=addr
        self.buffsize=buffsize
    def run(self):
        while True:
            sendata = input("client send msg:")
            self.socket.send(sendata.encode('utf-8'))
            cdata=self.socket.recv(self.buffsize)
            print("from server ",cdata.decode('utf-8'))
        self.socket.close()


def main():
    host = '127.0.0.1'
    port = 8888
    addr = (host,port)
    buffsize = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    client=Client(sock,addr,buffsize)
    client.run()


if __name__ == "__main__":
    main()

