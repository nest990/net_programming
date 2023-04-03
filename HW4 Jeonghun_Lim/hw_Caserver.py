import socket
def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mulply(a,b):
    return a*b
def division(a,b):
    return a/b
cat = {'+':add, '-':sub, '*':mulply,'/':division}




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',3333))
s.listen(5)
print('wating.....')
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data=client.recv(1024).decode()
        if not data:
            break
        try:
            rsp=cat[data.split(' ')[0]](float(data.split(' ')[1]),float(data.split(' ')[2]))
            rsp=str(rsp)
        except:
            client.send(b'Try again')
        else:
            client.send(rsp.encode())
  
    client.close()