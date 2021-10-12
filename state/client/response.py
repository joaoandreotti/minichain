from state import *
import get
import time

class Response(State):
    def run(self):
        print('Response socket: ' + str(self.connection.socket))
        response = self.connection.socket.recv(4096).decode()
        self.handler(response)
        self.connection.setConnection(get.Get())
        self.connection.run()

    def handler(self, response):
        print('response: ' + response)
        time.sleep(1)
