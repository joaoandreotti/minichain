from client import *
import time

class PersonClient(Client):
    PERSON_HELLO = 'HELLO PEER'
    PERSON_GET = 'TRANSACTION'

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
        #time.sleep(1)
        pass
        return self.get

    def get_handler(self, data):
        print('Transaction received: ' + data)
