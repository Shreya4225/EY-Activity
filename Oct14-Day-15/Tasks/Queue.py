import threading
import queue
import time
import random

q = queue.Queue()


def producer():
    for i in range(10):
        item = random.randint(1, 100)
        q.put(item)
        print(f"Producer: {item}")
        time.sleep(1)
    q.put(None)
    print("Producer finished producing")


def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(2)
    q.put(None)
    print("Consumer finished consuming")


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Producer-Consumer thread finished")