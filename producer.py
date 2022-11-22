import os
import time

producer_id = os.getpid()

print("Producer: {}".format(os.getpid()))
time.sleep(10)