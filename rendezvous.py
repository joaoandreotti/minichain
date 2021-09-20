import socket
import time
import threading

class Rendezvous:
    connections = []
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 5555))
        self.socket.listen(10)

    def __exit__(self):
        self.socket.close()

    def server_listener(self):
        while True:
            (client, address) = self.socket.accept()
            self.client_handler(client, address)

    def client_handler(self, client, address):
        def handler(client, address):
            client_ip = client.getsockname()[0]
            client_port = 0
            try:
                data = client.recv(4096).decode()
                if 'HELLO MINICHAIN' in data:
                    client_port = data.split(' ')[2]
                    self.add_client((client_ip, client_port))
                    while len(data) > 0:
                        data = client.recv(4096)
                        if 'GET PEERS' in data.decode():
                            client.sendall(self.get_ip_list((client_ip, client_port)).encode() + b'\n')
            except Exception as e:
                print(e)
            finally:
                self.remove_client((client_ip, client_port))
        client_thread = threading.Thread(target = handler, args = (client, address,))
        client_thread.start()
        return client_thread

    def add_client(self, client):
        self.connections.append(client)
        print(f'client added: {client}')

    def remove_client(self, client):
        try:
            self.connections.remove(client)
            print(f'client removed: {client}')
        except:
            print(f'{client} not on the list')

    def get_ip_list(self, client_tuple):
        ip_list = ';'.join([':'.join(conn) for conn in self.connections if conn != client_tuple])
        return ip_list

server = Rendezvous()
server.server_listener()
