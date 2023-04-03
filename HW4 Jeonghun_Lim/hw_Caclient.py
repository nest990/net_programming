import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 3333))
while True:
    col= input("send op number number(ex + 20 17)")
    if col =='q':
        break
    sock.send(col.encode())
    
    print('Received message:', sock.recv(1024).decode())
sock.close()