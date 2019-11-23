import socket
import threading
class Server(object):
    def __init__(self, socket, addr, conn_socket, buffsize,win):
        self.socket = socket
        self.conn_socket = conn_socket
        self.addr = addr
        self.win=win
        # self.buf_recv=buf_recv
        # self.buf_send=buf_send
        self.buffsize = buffsize

    def send(self,data):
        self.conn_socket.send(data.encode('utf-8'))
    def receive(self):
        while True:
            data = self.conn_socket.recv(self.buffsize)
            self.win.m_textCtrl2.AppendText("from client : %s\n" % (data.decode('utf-8')))
            print("from client ", data.decode('utf-8'))
        self.socket.close()

    