import threading


def gfg():
    count = 1
    print("Hub\n", count+1)


timer = threading.Timer(5.0, gfg)
timer.start()
