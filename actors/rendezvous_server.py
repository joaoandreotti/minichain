from network import server

class RendezvousServer(server.Server):
    MINICHAIN_HELLO = 'HELLO MINICHAIN 00000'
    MINICHAIN_GET = 'GET PEERS'

    def __init__(self):
        super(RendezvousServer, self).__init__(5555, self.MINICHAIN_HELLO, self.MINICHAIN_GET)

    def start_listener(self):
        self.connection_listener().join()

    def hello_handler(self, connection, data):
        try:
            ip = connection.getsockname()[0]
            port = data.split(' ')[2]
            return ip + ':' + port
        except Exception as e:
            print(e)

    def get_handler(self, client_string, data):
        ip_list = self.get_ip_list(client_string)
        return '\n' if len(ip_list) == 0 else ip_list
