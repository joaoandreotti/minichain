from network import client
import time

class PersonClient(client.Client):
    PERSON_HELLO = 'HELLO PEER 00000'
    PERSON_GET = 'SEND SOURCE DESTIN 00010'

    def __init__(self, server_tuple):
        super(PersonClient, self).__init__(server_tuple, self.PERSON_HELLO, self.PERSON_GET)
        self.initialized = False
        self.server_tuple = server_tuple

    def __eq__(self, other):
        return self.server_tuple == other

    def client_init(self):
        if not self.initialized:
            self.initialized = True
            return self.connection_handler()

    def client_get(self):
        time.sleep(5)
        return self.get
