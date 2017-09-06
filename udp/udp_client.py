import socket
import uuid

UDP_HOST = '127.0.0.1'
UDP_PORT = 12348


class UDPClient(object):

    def __init__(self, host, port, tag=None, msg=None):
        self.host = host
        self.port = port
        self.tag = tag if tag else uuid.uuid1()
        self.msg = msg if msg is not None else 'message from {}'.format(self.tag)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def send(self, n_messages):
        self.sock.connect((self.host, self.port))
        print('{} is connected to {}:{}'.format(self, self.host, self.port))
        for i in range(n_messages):
            yield self.sock.send(str.encode(self.msg))
            # data, addr = self.sock.recvfrom(1024)
        self.sock.close()
        print('{} is disconnected from {}:{}'.format(self, self.host, self.port))

    def __repr__(self):
        return 'UDPClient: {}'.format(self.tag)

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    client = UDPClient(UDP_HOST, UDP_PORT)
    res = [sent for sent in client.send(1000)]

