from socket import *

s = socket()
s.bind(('',80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    cut = req[0].split(' ')
    req1= cut[1][1:]
    if req1 == 'index.html':
        o = open(req1,'r',encoding = 'utf-8')
        text = 'text/html'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(str('Content-Type: ' + text +'\r\n').encode())
        c.send('\r\n'.encode())
        data = o.read()
        c.send(data.encode('euc-kr'))
    elif req1== 'iot.png':
        o = open(req1,'rb')
        image = 'image/png'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(str('Content-Type: ' + image +'\r\n').encode())
        c.send('\r\n'.encode())
        data = o.read()
        c.send(data)
    elif req1 == 'favicon.ico':
        o = open(req1,'rb')
        icron = 'image/x-icon'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send(str('Content-Type: ' + icron +'\r\n').encode())
        c.send('\r\n'.encode())
        data = o.read()
        c.send(data)
    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())
    c.close()



        
