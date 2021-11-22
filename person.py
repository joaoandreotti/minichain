import sys
import time
from actors import rendezvous_client
from actors import person_server
from actors import person_manager

listener_port = int(sys.argv[1])

print('RENDEZVOUS CLIENT INIT')
rendezvous = rendezvous_client.RendezvousClient(('localhost', 5555), listener_port)
rendezvous.client_init()

print('PERSON CLIENT MANAGER INIT')
person_client_manager = person_manager.PersonManager(rendezvous.connections)
person_client_manager.clients_init()

print('PERSON SERVER INIT')
server = person_server.PersonServer(listener_port)
server.connection_listener()

while True:
    person_client_manager.connections = rendezvous.connections
    time.sleep(1)
