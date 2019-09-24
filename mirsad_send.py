#!/usr/bin/python3
import socket, time
# checking for socket functions

print([i for i in dir(socket) if 'socket' in i])

# now creating UDP socket
# IPv4 Socket - IPv4 + 2 Byte port
# IPv6 socket - IPv6 + 2 bute port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #for ipv4 udp socket
# socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for IPv4 TCP socket.

'''
for receiver:
s.bind(("", 8889))
# bind will accept tuple format of IP and port
'''

# For sender - Enter message
while True:
    msg = input("Enter data tp send :")
    #converting data into byte-like string format
    newmsg = msg.encode('ascii')
    # lets send data to target
    s.sendto(newmsg, ("127.0.0.1", 8899))
    data = s.recvfrom(1000)
    print(data)
s.close()


'''for receiver:
    bind will accept tuple format of ip and port
data = s.recvfrom(1000)   --> this is buffer size
print(data)
'''


