import threading
import time
from atpbar import flush, atpbar
import random

# def gfg():
#     count = 1
#     print("Hub\n", count+1)


# timer = threading.Timer(5.0, gfg)
# print(timer.start())
# timer.start()

def run_with_threading():
    nthreads = 1

    def task(n, name):
        for i in atpbar(range(n), name=name):
            time.sleep(0.0001)
    threads = []
    for i in range(nthreads):
        name = 'thread {}'.format(i)
        n = random.randint(5, 100)
        t = threading.Thread(target=task, args=(n, name))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    flush()


run_with_threading()
