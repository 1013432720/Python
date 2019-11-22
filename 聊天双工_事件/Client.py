import socket
import threading
import Chat1
class Client(object):
    sendata = ""
    event = threading.Event()
    def __init__(self,socket,addr,buffsize):
        self.socket=socket
        self.addr=addr
        self.buffsize=buffsize

    def receive(self):
        while True:
            cdata=self.socket.recv(self.buffsize)
            print("from server ",cdata.decode('utf-8'))
            Chat1.win.m_textCtrl2.AppendText('from server: %s\n'%self.sendata)
    def run(self):
        threading.Thread(target=self.receive).start()
        while True:
            self.event.wait()
            Chat1.win.m_textCtrl2.AppendText('client send msg: %s\n'%self.sendata)
            self.socket.send(self.sendata.encode('utf-8'))
            self.event.clear()
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

