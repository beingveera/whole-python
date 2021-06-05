import socket,sys,threading
print('\n> Python3 Port Scanner\n  '+'='*20+'\n')
if len(sys.argv) > 1:
	target = socket.gethostbyname(sys.argv[1])
else: 
	 target = socket.gethostbyname(input('> Enter target: '))
# Scan ports - arguments: target + port
def scanPort(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c = s.connect_ex((target, port))
    if c == 0: 
    	print('  ' + target + ' ~ Port %d \t[open]' % (port,))
    s.close()
# Here we define range of ports to scan
for i in range(1, 1024):
    scan=threading.Thread(target=scanPort, args=(target, i))
    scan.start()