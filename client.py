from util import load_file, write_file
import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = 'localhost' 

port = 5000

s.connect((host, port))                    

result = load_file("data.txt").copy()

s.send(str(len(result)).encode('utf-8'))
time.sleep(0.4)
f = open('result.txt','w')
f.truncate()
for x in result:
    s.send(bytes(str(x),('utf-8')))
    time.sleep(0.4)
    msg = s.recv(100)
    time.sleep(0.4)
    message = msg.decode('utf-8')
    write_file("result.txt", message)
print('done')

