from network import server
from ledger import block
from ledger import ledger
from ledger import transaction

class MinerServer(server.Server):
    PEER_HELLO = 'HELLO PEER 00000'
    PEER_GET = 'SEND SOURCE DESTIN 00000'
    transaction_queue = 0
    current_ledger = []
    block_list = []

    def __init__(self, listener_port):
        super(MinerServer, self).__init__(listener_port, self.PEER_HELLO, self.PEER_GET)
        self.listener_port = listener_port
        self.current_ledger = ledger.Ledger()

    def start_listener(self):
        self.connection_listener().join()

    def hello_handler(self, connection, data):
        try:
            ip = connection.getsockname()[0]
            port = str(connection.getsockname()[1])
            return ip + ':' + port
        except Exception as e:
            print(e)

    def get_handler(self, client_string, data):
        self.transaction_queue += 1
        data = data.split(' ')
        current_transaction = transaction.Transaction(data[1], data[2], data[3].zfill(5))
        self.current_ledger.add_transaction(current_transaction)
        if self.transaction_queue == 1:
            new_block = block.Block(len(self.block_list),\
                repr(self.block_list[-1]),\
                repr(self.current_ledger), self.current_ledger)
            new_block.generate_valid_block()
            self.block_list.append(new_block)
            self.transaction_queue = 0
            self.current_ledger = ledger.Ledger()
        return '\n'
