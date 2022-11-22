import os
import time

broker_id = os.getpid()
print("Broker: {}".format(os.getpid()))

time.sleep(10)