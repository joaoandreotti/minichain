from network import server

class PersonServer(server.Server):
    PEER_HELLO = 'HELLO PEER 00000'
    PEER_GET = 'SEND SOURCE DESTIN 00000'

    def __init__(self, listener_port):
        super(PersonServer, self).__init__(listener_port, self.PEER_HELLO, self.PEER_GET)
        self.listener_port = listener_port

    def start_listener(self):
        self.connection_listener().join()

    def hello_handler(self, connection, data):
        try:
            ip = connection.getsockname()[0]
            port = str(connection.getsockname()[1])
            return ip + ':' + port
        except Exception as e:
            print(e)

    def get_handler(self, client_string, data):
        return '\n'
