import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg= sock.recv(1024)
print(msg.decode())
sock.send(b'jeong hun Lim')
msg2=sock.recv(1024)
print(int.from_bytes(msg2,'big'))
sock.close()