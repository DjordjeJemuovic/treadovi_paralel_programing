import threading
import time


def writhHelo():
    while True:
        print(" hello ")
        time.sleep(5)

treadHelow = threading.Thread(target=writhHelo)
treadHelow.start()


print("prosao petlju")