import socket

UDP_IP= "10.160.108.101"
UDP_PORT = 5005
MESSAGE="?"
MESSAGE2= "cinema"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data, addr =sock.recvfrom(1024)
print("Message recu :", data.decode())
sock.sendto(MESSAGE2.encode(), (UDP_IP, UDP_PORT))
data = sock.recvfrom(1024)
print("Message recu :", data)
    
