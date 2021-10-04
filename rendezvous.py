import socket
import time
import threading
from server import *

class Rendezvous(Server):
    MINICHAIN_HELLO = 'HELLO MINICHAIN'
    MINICHAIN_GET = 'GET PEERS'

    def __init__(self):
        super(Rendezvous, self).__init__(5555, self.MINICHAIN_HELLO, self.MINICHAIN_GET)

    def start_listener(self):
        self.connection_listener().join()

    def get_ip_list(self, client_string):
        ip_list = ';'.join([conn for conn in self.connections if conn != client_string])
        return ip_list

    def hello_handler(self, ip, data):
        try:
            port = data.split(' ')[2]
            return ip + ':' + port
        except Exception as e:
            print(e)

    def get_handler(self, client_string, data):
        ip_list = self.get_ip_list(client_string)
        return '\n' if len(ip_list) == 0 else ip_list

server = Rendezvous()
server.start_listener()
