import socket 
import sys
s=socket.socket();
host=socket.gethostname();
port=12345
s.connect((host,port));

while True:
	d=raw_input()
	s.send(d);
print s.recv(1024)
s.close()
