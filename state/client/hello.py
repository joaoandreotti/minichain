from state import *
from get import *

class Hello(State):
    def run(self):
        print('Hello socket: ' + str(self.connection.socket))
        self.connection.socket.sendall(self.connection.hello.encode())
        self.connection.setConnection(Get())
        self.connection.run()
