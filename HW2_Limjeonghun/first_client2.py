import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
send = a = 'jeong hun Lim'
sock.send(a.encode())

msg = sock.recv(1024)

d= int.from_bytes(msg,'big')
print(d)

sock.close()