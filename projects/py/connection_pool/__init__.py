from pymongo import MongoClient
import threading
from time import sleep


class Pool:
    def __init__(self):
        self.conns = [MongoClient() for _ in range(10)]

    def get(self):
        while True:
            if self.conns:
                return self.conns.pop()
            sleep(1)
            print("Nothing to return")

    def add(self, conn):
        self.conns.append(conn)


def target(connection, pool, i):
    sleep(5)
    connection["benq"]["users"].find_one({})
    pool.add(connection)


def find():
    pool = Pool()
    threads = []
    for i in range(50):
        print(i)
        connection = pool.get()
        t = threading.Thread(target=target, args=(connection, pool, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
