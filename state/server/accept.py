import threading
from state import *
from connection import *
from hello import *

class Accept(State):
    def run(self):
        print('Accept socket: ' + str(self.connection.socket))
        print('Accept state')
        (client, info) = self.connection.socket.accept()
        print('Transitioning to hello')
        connection = Connection(client, Hello())
        threading.Thread(target = connection.run).start()
        print('Transitioning to accept')
        self.connection.setConnection(Accept())
        self.connection.run()
