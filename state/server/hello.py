from state import *
from get import *

class Hello(State):
    def run(self):
        print('Hello socket: ' + str(self.connection.socket))
        hello = self.connection.socket.recv(4096).decode()
        if self.connection.hello in hello:
            self.handler(hello)
            self.connection.setConnection(Get())
            self.connection.run()

    def handler(self, hello):
        print('Hello MSG: ' + hello)
