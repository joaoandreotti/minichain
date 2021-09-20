import hashlib
from ledger import *
from transaction import *

class Block:
    def __init__(self, number, previous_hash, transactions_hash, ledger):
        self.number = number
        self.previous_hash = previous_hash
        self.transactions_hash = transactions_hash
        self.ledger = ledger
        self.proof_of_work = 0

    def __str__(self):
        return str(self.number) + ';' + self.previous_hash + ';' + \
                self.transactions_hash + ';' + str(self.proof_of_work)

    def __repr__(self):
        return hashlib.sha256(str(self).encode()).hexdigest()

    def generate_valid_block(self):
        while not self.valid_block():
            self.proof_of_work += 1

    def valid_block(self):
        difficult = 6
        if repr(self)[:difficult] == '0'*difficult:
            return True
        return False
