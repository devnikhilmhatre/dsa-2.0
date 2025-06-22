from pymongo import MongoClient
import threading
from time import sleep
from queue import Queue

sem = threading.Semaphore(10)


class Pool:
    # def __init__(self):
    #     self.conns = Queue(10)
    #     for _ in range(10):
    #         self.conns.put()

    def get(self):
        return MongoClient()

    # def add(self, conn):
    #     self.conns.put(conn)


def target(connection, pool, i):
    if sem:
        sleep(5)
        connection["benq"]["users"].find_one({})
        print("-" * 5, i)
        # pool.add(connection)


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
