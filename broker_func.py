import os,sys,requests,re,json, time
from _thread import *
from flask import Flask
# if leader: setup connection between broker-producer and broker-consumer on flask &&
# and send metadata from written file system after update from producer
# metadata format : json


ipc=''

def thread_func():
    yield

def leader_task():
    # filepath=ipc
    
    try:
        with open(ipc,'a') as br_log:
            br_log.write(f"")
    except:
        pass

