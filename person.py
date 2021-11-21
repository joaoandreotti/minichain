import time
import threading
import sys
from actors import rendezvous_client
from actors import person_client 
from actors import person_server

class Person:
    PEER_HELLO = 'HELLO PEER'
    PEER_GET = ''
    persons = []

    def __init__(self, listener_port):
        self.listener_port = listener_port

    def start_listener(self):
        self.server = person_server.PersonServer(self.listener_port)
        self.server.connection_listener()

    def rendezvous_init(self):
        self.rendezvous = rendezvous_client.RendezvousClient(('localhost', 5555), self.listener_port)
        self.rendezvous.client_init()

    def clients_init(self):
        def connection_loop():
            while True:
                for connection in self.rendezvous.connections:
                    try:
                        if connection not in self.persons:
                            client = person_client.PersonClient(connection)
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

print('INITIALIZING')
client = Person(int(sys.argv[1]))
print('RENDEZVOUS CONNECTION')
client.rendezvous_init()
print('CONNECTING TO PEERS')
client.clients_init()
print('LISTENING TO PEERS')
client.start_listener()
