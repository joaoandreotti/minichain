from actors import miner_server
from actors import rendezvous_client
import time
import threading

threads = []

rendezvous = rendezvous_client.RendezvousClient(('localhost', 5555), 5554)
threads.append(rendezvous.client_init())

server = miner_server.MinerServer(5554)
threads.append(server.connection_listener())

def calculate_money():
    money_map = {}
    while True:
        for block in server.block_list:
            for transaction in block.ledger.transaction_list:
                if transaction.source not in money_map:
                    money_map[transaction.source] = 0
                if transaction.destination not in money_map:
                    money_map[transaction.destination] = 0
                money_map[transaction.source] += int(transaction.value)
                money_map[transaction.destination] -= int(transaction.value)
        print(money_map)
        time.sleep(10)

threads.append(threading.Thread(target = calculate_money))
threads[-1].start()

for thread in threads:
    thread.join()
