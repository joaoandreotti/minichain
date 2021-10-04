import socket
import threading

class Client:
    def __init__(self, server_tuple, hello, get):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(server_tuple)
        self.hello = hello
        self.get = get

    def __exit__(self):
        self.client.close()

    def __del__(self):
        self.client.close()

    def connection_handler(self):
        def handler(client):
            try:
                print('sending: ' + self.hello)
                client.sendall(self.hello.encode())
                print('hello sent')
                while True:
                    self.client_get()
                    print('sending: ' + self.get)
                    client.send(self.get.encode())
                    print('get sent')
                    data = client.recv(4096).decode()
                    self.get_handler(data)
            except Exception as e:
                print(e)
        thread = threading.Thread(target = handler, args = (self.client,))
        thread.start()
        return thread

    def client_get(self):
        return self.get

    def get_handler(self, data):
        pass
