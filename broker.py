import socket
import threading
import os

#client part (zookeeper-broker)
client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client1.connect(('10.0.2.15',5000))

# {
#     topic1:{
#         part1:off1,
#         part2:off2,
#         part3:off3
#     },
#     topic2:{
#         part1:off1
#     }

# }

# topic1:{
#     part1::0
#     part2:0
#     part3:0
# }
# topic1:{
#         part1:off1,
#         part2:off2,
#         part3:off3
#     }

# server part
ser_host='10.0.2.15'
ser_port = 5001
print(f"Running server on: {ser_host} and port: {ser_port}")

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

try:
    sck.bind((ser_host,ser_port))
    sck.listen(5)
except Exception as e:
    raise SystemExit(f"We could not bind the server on host:{ser_host} to port: {ser_port},because {e}")

def on_new_client(client,connection):
    ip = connection[0]
    port = connection[1]
    print(f"new connection from ip:{ip} and port: {port}")
    while True:
        client1.send("Give ip_port".encode('utf-8'))
        l = client1.recv(1024).decode()

        msg = client.recv(1024)
        print(f"The client said:{msg.decode()}")
        if msg.decode()=='p_update':
            # client.send(l.encode('utf-8'))

        client.send("hi".encode("utf-8"))
        if msg.decode() == "stop":
            break
    client.close()  

while True:
    try:
        client,ip = sck.accept()
        threading._start_new_thread(on_new_client,(client,ip))
    except Exception as e:
        print(f"This is error {e}")

sck.close()