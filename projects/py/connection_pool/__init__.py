from pymongo import MongoClient
import asyncio
from time import sleep
from queue import Queue

sem = asyncio.Semaphore(10)


class Pool:
    def get(self):
        return MongoClient()


async def target(connection, i):
    if sem:
        await asyncio.sleep(5)
        connection["benq"]["users"].find_one({})
        print("-" * 5, i)
        # pool.add(connection)


async def find():
    pool = Pool()
    threads = []
    for i in range(50):
        print(i)
        connection = pool.get()
        threads.append(target(connection, i))

    await asyncio.gather(*threads)


asyncio.get_event_loop().run_until_complete(find())
