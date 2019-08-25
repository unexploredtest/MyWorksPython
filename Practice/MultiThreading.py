from threading import *
from time import sleep

class lol(Thread):

    def run(self):
        for i in range(8):
            print("lol")
            sleep(1)

class noob(Thread):

    def run(self):
        for i in range(5):
            print("noob")
            sleep(1)
w1 = lol()
w2 = noob()

w1.start()
sleep(0.2)
w2.start()

w1.join()
w2.join()

print("loler than noober")
