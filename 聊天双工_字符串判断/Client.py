import socket
import threading
class Client(object):
    def __init__(self,socket,addr,buffsize,win):
        self.socket=socket
        self.addr=addr
        self.buffsize=buffsize
        self.win=win
    def receive(self):
        while True:
            cdata=self.socket.recv(self.buffsize).decode('utf-8')
            print("from server: %s"%cdata)
            self.win.m_textCtrl2.AppendText('from server: %s\n'%cdata)
        self.socket.close()
    def send(self,data):
        self.socket.send(data.encode('utf-8'))
        
