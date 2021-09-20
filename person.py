import socket
import time
import threading
import sys

class Person:
    connections = []

    def __init__(self, listener_port):
        self.listener_port = listener_port
        self.rendezvous_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rendezvous_socket.connect(('localhost', 5555))
        self.peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peer_socket.bind(('', self.listener_port))
        self.peer_socket.listen(10)

    def __exit__(self):
        self.peer_socket.close()
        self.rendezvous_socket.close()

    def rendezvous_init(self):
        if self.rendezvous_hello() and self.rendezvous_get_peers():
            return True
        return False

    def rendezvous_hello(self):
        try:
            self.rendezvous_socket.sendall(b'HELLO MINICHAIN ' + str(self.listener_port).encode())
            return True
        except:
            return False

    def rendezvous_get_peers(self):
        try:
            time.sleep(1)
            self.rendezvous_socket.sendall(b'GET PEERS')
            data = self.rendezvous_socket.recv(4096)
            self.peer_list = [peer.replace('\n', '') for peer in data.decode().split(';')]
            return True
        except:
            return False

    def peer_connect_to_list(self):
        print(self.peer_list)
        for peer in self.peer_list:
            try:
                peer = peer.split(':')
                peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peer_socket.connect((peer[0], int(peer[1])))
                self.peer_hello()
                self.peer_send_command(peer_socket)
            except:
                continue
        return True

    def peer_hello(self):
        try:
            self.rendezvous_socket.sendall(b'HELLO PEER')
            return True
        except:
            return False

    def peer_send_command(self, peer_socket, command):
        try:
            peer_socket.sendall(command)
            return True
        except:
            return False

    def peer_listener(self):
        while True:
            (peer, address) = self.peer_socket.accept()
            self.peer_handler(peer, address)

    def peer_handler(self, peer, address):
        def handler(peer, address):
            self.add_peer(peer)
            try:
                data = peer.recv(4096)
                print(data)
                if 'HELLO PEER' in data.decode():
                    print('a')
                    while True:
                        data = peer.recv(4096)
                        print(data)
            except Exception as e:
                print(e)
            finally:
                self.remove_peer(peer)
        peer_thread = threading.Thread(target = handler, args = (peer, address,))
        peer_thread.start()
        return peer_thread

    def add_peer(self, peer):
        print(f'peer add: {peer}')
        self.connections.append(peer)

    def remove_peer(self, peer):
        print(f'peer removed: {peer}')
        self.connections.remove(peer)

client = Person(int(sys.argv[1]))
print('INITIALIZING')
if client.rendezvous_init() and client.peer_connect_to_list():
    print('LISTENING TO PEERS')
    client.peer_listener()
