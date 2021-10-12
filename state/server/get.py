from state import *
from response import *

class Get(State):
    def run(self):
        print('Get socket: ' + str(self.connection.socket))
        get = self.connection.socket.recv(4096).decode()
        if self.connection.get in get:
            self.handler(get)
            self.connection.setConnection(Response())
            self.connection.run()

    def handler(self, get):
        print('Get MSG: ' + get)
