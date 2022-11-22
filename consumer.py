import os
import time

consumer_id = os.getpid()
    

print("Consumer: {}".format(os.getpid()))

time.sleep(10)