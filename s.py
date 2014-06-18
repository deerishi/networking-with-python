import socket;
s=socket.socket() ;
host=socket.gethostname();
port=12345;
print 'host is ',host
s.bind((host,port));
s.listen(10)
while True :
	(c,add)=s.accept();
	print 'the received address is ',add
	while True:
		print  c.recv(1024)
	c.send('thank you for sending');
	






