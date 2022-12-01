import socket
import threading
import os
import logging

queue = []
leader=0

ser_host ='10.0.2.15'
ser_port = 5000
print(f"Running server on: {ser_host} and port: {ser_port}")

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
    sck.bind((ser_host,ser_port))
    sck.listen(5)
except Exception as e:
    raise SystemExit(f"we could not bind the server on host:{ser_host} to port:{ser_port}, because {e}")


def on_new_client(client,connection):
    global leader
    ip = connection[0]
    port = connection[1]
    print(f"New connection from ip:{ip} and port:{port}")
    queue.append(port);leader=queue[0]
    print(queue)
    while True:
        try:
            msg = client.recv(1024)
            print(f"The client said:{msg.decode()}")
            client.send("hi".encode('utf-8'))
            #temp
            if port==leader:
               client.send("True".encode('utf-8'))
            if msg.decode() == "stop":
                break
        except Exception as e:
            break
        
        #give condition here if it doesn't for send then call allocated leader? and then close that connection and start a new connection
    queue.pop(0); leader=queue[0] # leader gets updated here. Basically round robin election??
    print(queue)
    client.send("True".encode('utf-8'))
    print(f"disconnected")
    
while True:
    try:
        client,ip=sck.accept()
        threading._start_new_thread(on_new_client,(client,ip))
    except Exception as e:
        print(f"THis is error {e}")

sck.close()