import hashlib

class Ledger:
    def __init__(self):
        self.transaction_list = list()

    def __str__(self):
        return str(len(self.transaction_list)) + ';' + str(self.transaction_list)

    def __repr__(self):
        return hashlib.sha256(str(self).encode()).hexdigest()

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
