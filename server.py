import socket
import threading

class Server:
    connections = []

    def __init__(self, listener_port, hello, get):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connection_socket.bind(('', listener_port))
        self.connection_socket.listen(5)
        self.hello = hello
        self.get = get

    def __exit__(self):
        self.connection_socket.close()

    def connection_listener(self):
        def listener():
            while True:
                print('waiting for connection')
                (connection, address) = self.connection_socket.accept()
                print('received connection' + str(address))
                self.connection_handler(connection, address)
        thread = threading.Thread(target = listener)
        thread.start()
        return thread

    def connection_handler(self, connection, address):
        def handler(connection, address):
            client_string = ''
            try:
                data = connection.recv(4096).decode()
                if self.hello in data:
                    client_string = self.hello_handler(connection.getsockname()[0], data)
                    self.connections.append(client_string)
                    while True:
                        data = connection.recv(4096).decode()
                        if len(data) == 0:
                            break
                        if self.get in data:
                            message = self.get_handler(client_string, data)
                            connection.sendall(message.encode())
            except Exception as e:
                print(e)
            finally:
                self.remove_connection(client_string)
        thread = threading.Thread(target = handler, args = (connection, address,))
        thread.start()
        return thread

    def add_connection(self, connection):
        print(f'connection add: {connection}')
        self.connections.append(connection)

    def remove_connection(self, connection):
        print(f'connection removed: {connection}')
        self.connections.remove(connection)

    def hello_handler(self, ip, data):
        return 'DEFAULT'

    def get_handler(self, client_string, data):
        return 'DEFAULT'
