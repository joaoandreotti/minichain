from state import *
from connection import *
from hello import *
import socket
import threading

class Connect(State):
    def run(self):
        print('Connect socket: ' + str(self.connection.socket))
        self.connection.socket.connect(self.connection.server_tuple)
        print('Transitioning to hello')
        self.connection.setConnection(Hello())
        self.connection.run()
