from pymongo import MongoClient
import threading
from time import sleep
from queue import Queue


class Pool:
    def __init__(self):
        self.conns = Queue(10)
        for _ in range(10):
            self.conns.put(MongoClient())

    def get(self):
        return self.conns.get()

    def add(self, conn):
        self.conns.put(conn)


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


# find()
