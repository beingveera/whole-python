from socket import *
#f=socket(AF_INET,SOCK_STREAM)
f=socket(AF_INET,SOCK_STREAM)
#print(f)
f.connect(("www.google.com",80))
f.send("GET /index.html HTTP/1.0\n\n") 
data = s.recv(10000) 
f.close()

