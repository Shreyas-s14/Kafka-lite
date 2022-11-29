import socket
import threading
import os

ser_host ='10.0.0.2'
ser_port = 4001
print(f"Running server on: {ser_host} and port: {ser_port}")

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
    sck.bind((ser_host,ser_port))
    sck.listen(5)
except Exception as e:
    raise SystemExit(f"we could not bind the server on host:{ser_host} to port:{ser_port}, because {e}")


def on_new_client(client,connection):
    ip = connection[0]
    port = connection[1]
    print(f"New connection from ip:{ip} and port:{port}")
    while True:
        msg = client.recv(1024)
        print(f"The client said:{msg.decode()}")
        client.sendall("hi".encode('utf-8'))
        #temp
        if msg.decode() == "stop":
            break

        #give condition here if it doesn't for send then call allocated leader? and then close that connection and start a new connection

    print(f"disconnected")
    
while True:
    try:
        client,ip=sck.accept()
        threading._start_new_thread(on_new_client,(client,ip))
    except Exception as e:
        print(f"THis is error {e}")

sck.close()