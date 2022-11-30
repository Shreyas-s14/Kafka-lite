import socket
import threading
import os
import sys
import json
import random

ip_port = [('10.0.2.15',5001),('10.0.2.15',5002),('10.0.2.15',5003)]
# connect_port = 0
# connect_ip = 0


def helper_connect(client,i) -> bool:
    # client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect(ip_port[i])
        return True
    except Exception as e:
        print(e) 
        # ip_.pop(ind)
        return False

class producer:
    

    def __init__(self):
        pass


    def connection(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        global connect_port 
        global connect_ip
        ind = random.randint(0,2)
        if helper_connect(client,ind):
            
            client.send("p_update".encode('utf-8'))
            # up_list = client.recv(1024).decode('utf-8')
            # print(up_list)
            
            connect_port = ip_port[ind][1]
            
            connect_ip =  ip_port[ind][0]


        elif helper_connect(client,((ind+1)%3)):
            client.send("p_update".encode('utf-8'))
            # up_list = client.recv(1024).decode('utf-8')
            # print(up_list)
            # global connect_port 
            connect_port = ip_port[(ind+1)%3][1]
            # global connect_ip
            connect_ip =  ip_port[(ind+1)%3][0]

        elif helper_connect(client,((ind+2)%3)):
            client.send("p_update".encode('utf-8'))
            # up_list = client.recv(1024).decode('utf-8')
            # print(up_list)
            # global connect_port 
            connect_port = ip_port[(ind+2)%3][1]
            # global connect_ip
            connect_ip =  ip_port[(ind+2)%3][0]
        else:
            print("none is working")
        return client

    def send_message(self,client,topic,message):
        self.topic = topic
        self.message = message
        final_message = {topic:message}
        j_message = json.dumps(final_message)
        client.send(j_message.encode('utf-8'))
        ack_mesg = client.recv(1024).decode('utf-8')


if __name__ == '__main__':
    pass