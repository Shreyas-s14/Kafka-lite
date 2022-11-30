import socket
import threading
import os
import sys
import json
import random

ip_port = [('10.0.2.15',5001),('10.0.2.15',5002),('10.0.2.15',5003)]

def helper_connect(client,i) -> bool:
    try:
        client.connect(ip_port[i])
        return True
    except Exception as e:
        print(e) 
        return False

class consumer:
    

    def __init__(self):
        pass


    def connection(self,topic):
        self.topic = topic
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        global connect_port 
        global connect_ip
        ind = random.randint(0,2)
        if helper_connect(client,ind):
            client.send("c_offset".encode('utf-8'))
            client.send(f"{topic}".encode('utf-8'))
            meta = client.recv(2048).decode('utf-8')
            connect_port = ip_port[ind][1]
            connect_ip =  ip_port[ind][0]

        elif helper_connect(client,((ind+1)%3)):
            client.send("c_offset".encode('utf-8'))
            client.send(f"{topic}".encode('utf-8'))
            meta = client.recv(2048).decode('utf-8')
            connect_port = ip_port[(ind+1)%3][1]
            connect_ip =  ip_port[(ind+1)%3][0]

        elif helper_connect(client,((ind+2)%3)):
            client.send("c_offset".encode('utf-8')) 
            client.send(f"{topic}".encode('utf-8'))
            meta = client.recv(2048).decode('utf-8')
            connect_port = ip_port[(ind+2)%3][1]
            connect_ip =  ip_port[(ind+2)%3][0]
        else:
            print("none is working")
        return client,meta

    def request_topic(self,client,topic,offset,flag):
        self.topic = topic
        self.offset = offset
        self.flag = flag
        final_request = {topic:(flag,offset)}
        request_message = json.dumps(final_request)
        client.send(request_message.encode('utf-8'))
        while True:
            data = client.recv(2048).decode('utf-8')
            yield data

if __name__ == '__main__':
    pass