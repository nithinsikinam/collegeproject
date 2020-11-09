import socket                
  
print("hellokp")
c = socket.socket()          
  

c.connect(("209.151.148.95", 9999)) 

name = input("enter your name")
c.send(bytes(name,'utf-8'))

 
print (c.recv(1024).decode()) 
 
