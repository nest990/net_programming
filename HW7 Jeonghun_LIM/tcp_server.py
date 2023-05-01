import socket
import threading
import time
clients = []

def sendTask(sock,addr):
    while True:
        data = sock.recv(1024)
        if sock not in clients:
            print('new client',addr)
            clients.append(sock)
        
        print(time.asctime() + str(addr) + ':' + data.decode())
        
        for client in clients:
            if client != sock:
                client.send(data)
                    
        
        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',2500))
s.listen(10)
print('Server Started')
while True:
    conn, addr = s.accept()
    
    th = (threading.Thread(target=sendTask, args=(conn,addr,)))
    th.start()
