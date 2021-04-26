import socket                                         
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = 'localhost'                        

port = 5000                                          

s.bind((host, port))                                  

s.listen(5)                                           
clientsocket,addr = s.accept()
size = clientsocket.recv(5).decode('utf-8')
time.sleep(0.4)
for x in range(int(size)):
    msg = clientsocket.recv(100)
    time.sleep(0.4)
    clientsocket.send(bytes(msg.decode('utf-8').upper(),'utf-8'))
    time.sleep(0.4)
print('done')
