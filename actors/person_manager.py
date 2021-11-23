import time
import threading
from actors import person_client

class PersonManager:
    persons = []

    def __init__(self, connections):
      self.connections = connections

    def clients_init(self):
        def connection_loop():
            while True:
                for connection in self.connections:
                    try:
                        if connection not in self.persons:
                            client = person_client.PersonClient(connection)
                            self.persons.append(client)
                    except Exception as e:
                        print(e)
                for person in self.persons:
                    try:
                        person.client_init()
                    except Exception as e:
                        print(e)
                time.sleep(1)
        thread = threading.Thread(target = connection_loop)
        thread.start()
        return thread

