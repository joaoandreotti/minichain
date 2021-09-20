import hashlib

class Transaction:
    def __init__(self, source, destination, value):
        self.source = source
        self.destination = destination
        self.value = value

    def __str__(self):
        return self.source + ';' + self.destination + ';' + str(self.value)

    def __repr__(self):
        return hashlib.sha256(str(self).encode()).hexdigest()
