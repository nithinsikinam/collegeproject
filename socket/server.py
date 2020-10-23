import socket                
  
# Create a socket object 
s = socket.socket()     
print("Socket created")     
  
s.bind(('209.151.148.95', 1234))            
  
s.listen(3)
print("waiting for connection")

while True:
    c,addr = s.accept()
    
    name = c.recv(1024).decode()

    print("connection with", addr,name)
    
    c.send(bytes("welcome hasan ali", "utf-8"))

    c.close