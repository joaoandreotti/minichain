from state import *

class Connection:
    _state = None
    hello = 'HELLO MINICHAIN'
    get = 'GET PEERS'

    def __init__(self, socket, state: State) -> None:
        self.setConnection(state)
        self.socket = socket

    def setConnection(self, state: State):
        self._state = state
        self._state._connection = self

    def run(self):
        self._state.run()
