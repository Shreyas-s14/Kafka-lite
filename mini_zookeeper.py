import socket
from _thread import *
import threading
import sys
import os
import time


'''
Required functions:
1) setup and connection
2) heartbeat on the same socket for all the brokers
3) leader_election
4) metadata
5) configuration of topics from broker : by taking response from broker , which previously, received info from producer  (RESEARCH MORE ON THIS!!)
'''


####################################################################################################
global_metadata=dict() # update metadata received from the brokers
global_threads=[] # to keep count of threads (zookeeper side only)
####################################################################################################


print_lock=threading.Lock()
def threaded(client) -> None:
    while True:

       # Data is received from the client
        data = client.recv(1001)
        if not data:
           print('No connection, Bye')
          
           # Releasing lock on exit
           print_lock.release()
           break

       # Reverse the given string from the client
        data =data[::-1]

       # Send back reversed string to the client
        client.send(data)


# the function to be called inside the thread instance created
# arg: client socket...
def handle_client(client_socket):
    #print out what the client sends
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request.decode('utf-8'))
    #send back a packet
    client_socket.send("ACK!".encode('utf-8'))
    #client_socket.close()

def enter_client(): # temporary soltion for getting ip and port from all the 3 brokers... fix later
    client1=[]
    client2=[]
    client3=[]
    client1.append(input("Enter client1 ip: "))
    client1.append(int(input("Enter client1 port: ")))
    client2.append(input("Enter client2 ip: "))
    client2.append(int(input("Enter client2 port: ")))
    client3.append(input("Enter client3 ip: "))
    client3.append(int(input("Enter client3 port: ")))
    return client1,client2,client3

def heartbeat():
    pass

def leader_election():
    pass

def metadata_update():
    pass

def main():
    host = "127.0.0.1" # fix later
    port = 1025
    c1,c2,c3=enter_client()  # for now, manually enter
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    while True:
        client1, addr1 = server.accept()
        client2, addr2 = server.accept()
        client3, addr3 = server.accept()
        client_handler1= threading.Thread(target=handle_client, args=(client1,)) # argument is a socket
        client_handler2= threading.Thread(target=handle_client, args=(client2,))
        client_handler3= threading.Thread(target=handle_client, args=(client3,))

        # start the threads to receive 
        client_handler1.start()
        #client_handler1.join()
        client_handler2.start()
        #client_handler2.join()
        client_handler3.start()

main()

