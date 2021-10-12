from state import *
import get

class Response(State):
    def run(self):
        print('Response socket: ' + str(self.connection.socket))
        self.connection.socket.sendall('127.0.0.1:5559'.encode())
        self.connection.setConnection(get.Get())
        self.connection.run()
