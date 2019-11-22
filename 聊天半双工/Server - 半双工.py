import socket
import threading
import Chat
event=threading.Event() 
class Server(object):
    sendata=""
    def __init__(self,socket,addr,conn_socket,buffsize):
        self.socket=socket
        self.conn_socket=conn_socket
        self.addr=addr
        #self.buf_recv=buf_recv
        #self.buf_send=buf_send
        self.buffsize=buffsize
    def run(self):
        while True:
            #conn,addr=self.socket.accept()
            while True:
                data = self.conn_socket.recv(self.buffsize)
                Chat.win.m_textCtrl2.AppendText("from client : %s\n" %(data.decode('utf-8')))
                print("from client ",data.decode('utf-8'))
                Chat.win.m_textCtrl2.AppendText('server reply msg:')
                event.wait()
                self.conn_socket.send(self.sendata.encode('utf-8'))
                event.clear()
        self.socket.close()

def main():
    host ='127.0.0.1'
    port = 8888
    addr = (host,port)
    buffsize = 1024
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    #while True:
    conn,addr=sock.accept()
    server=Server(sock,addr,conn,buffsize)
    server.run()
if __name__ == '__main__':
    main()