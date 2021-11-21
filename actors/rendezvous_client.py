from network import client
import time

class RendezvousClient(client.Client):
    connections = []

    RENDEZVOUS_HELLO = 'HELLO MINICHAIN '
    RENDEZVOUS_GET = 'GET PEERS'

    def __init__(self, server_tuple, listener_port):
        self.RENDEZVOUS_HELLO = self.RENDEZVOUS_HELLO + str(listener_port).zfill(5)
        super(RendezvousClient, self).__init__(server_tuple,\
            self.RENDEZVOUS_HELLO, self.RENDEZVOUS_GET)

    def client_init(self):
        return self.connection_handler()

    def client_get(self):
        time.sleep(1)
        return self.get

    def get_handler(self, data):
        print('recv peers: ' + data)
        peer_list = [peer.replace('\n', '') for peer in data.split(';')]
        try:
            self.connections = [(peer.split(':')[0], int(peer.split(':')[1])) for peer in peer_list]
        except:
            pass
