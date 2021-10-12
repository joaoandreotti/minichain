from state import *
from response import *

class Get(State):
    def run(self):
        print('Get socket: ' + str(self.connection.socket))
        self.connection.socket.sendall(self.connection.get.encode())
        self.connection.setConnection(Response())
        self.connection.run()
