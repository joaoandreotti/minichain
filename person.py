import socket
import time
import threading
import sys
from server import *
from rendezvous_client import *
from person_client import *

class Person(Server):
    PEER_HELLO = 'HELLO PEER'
    PEER_GET = ''
    persons = []

    def __init__(self, listener_port):
        super(Person, self).__init__(listener_port, self.PEER_HELLO, self.PEER_GET)
        self.listener_port = listener_port

    def start_listener(self):
        self.connection_listener().join()

    def rendezvous_init(self):
        self.rendezvous = RendezvousClient(('localhost', 5555), self.listener_port)
        self.rendezvous.client_init()

    def clients_init(self):
        def connection_loop():
            while True:
                for connection in self.rendezvous.connections:
                    try:
                        if connection not in self.persons:
                            client = PersonClient(connection)
                            self.persons.append(client)
                    except Exception as e:
                        print(e)
                for person in self.persons:
                    try:
                        if person.client_init() is not None:
                            print('connected to ' + str(person))
                    except Exception as e:
                        print(e)
                time.sleep(1)
        thread = threading.Thread(target = connection_loop)
        thread.start()
        return thread

    def peer_send_command(self, peer_socket):
        command = b'JAMES'
        try:
            peer_socket.sendall(command)
            return True
        except:
            return False

print('INITIALIZING')
client = Person(int(sys.argv[1]))
print('RENDEZVOUS CONNECTION')
client.rendezvous_init()
print('CONNECTING TO PEERS')
client.clients_init()
print('LISTENING TO PEERS')
client.start_listener()
