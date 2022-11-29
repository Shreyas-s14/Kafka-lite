import subprocess
import os
from subprocess import Popen,PIPE

number_of_producers = int(input("Enter number of producers: "))
number_of_consumers = int(input("Enter number of consumers: "))
number_of_brokers = 3

commands = []

commands.append("python3 broker1.py")
commands.append("python3 broker2.py")
commands.append("python3 broker3.py")

for i in range(number_of_consumers):
    commands.append("python3 consumer.py")

for i in range(number_of_producers):
    commands.append("python3 producer.py")

#commands.append("python mini_zookeeper.py")

print(len(commands))

procs = [ Popen(i) for i in commands ]

for p in procs:
   p.wait()

'''
def create_brokers():
    for i in range(number_of_brokers):
        program_broker = "broker.py"
        Popen(program_broker)
        print("created broker: {}").format(i)

def create_consumers():
    for i in range(number_of_consumers):
        program_consumer = "producer.py"
        Popen(program_consumer)
        print("created consumer: {}").format(i)

def create_producers():
    for i in range(number_of_producers):
        program_producer = "consumer.py"
        Popen(program_producer)
        print("created producer: {}").format(i)


create_brokers()
create_consumers()
create_producers()
'''