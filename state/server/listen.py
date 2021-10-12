from state import *
from accept import *

class Listen(State):
    def run(self) -> None:
        print('Listener state')
        self.connection.socket.listen(5)
        print('Transitioning to accept')
        self.connection.setConnection(Accept())
        self.connection.run()
