import socket

UDP_HOST = '127.0.0.1'
UDP_PORT = 12348

def receive_messages(addr, maxsize):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
         msg = s.recvfrom(maxsize)
         yield msg

max_messages = 1024
for msg, addr in receive_messages((UDP_HOST, UDP_PORT), max_messages):
    print('address: {} ::: message: {}'.format(msg, addr))
