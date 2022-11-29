from flask import Flask
import threading
import sys,time
from _thread import *
import socket
import socketserver



class Zookeeper:
    # global file path to be appended by every instance
    filepath=""
    connection_list=[] # list of all the connection ports(client side)

    def __init__(self,host,port): # host:ip address, port:port number
        self.host = host
        self.port = port

    def connection_setup(self):
        self.server = socketserver.ThreadingTCPServer((self.host,self.port),socketserver.BaseRequestHandler)
        self.server.serve_forever()

        while True:
            self.server.handle_request()
            self.connection_list.append(self.request)
            
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            self.request.sendall(self.data.upper())

            
    def run(self):
        self.connection_setup()

        self.handle()


    
    def heartbeat(self): #send a message to the connected client every 5 seconds and if the client doesn't respond in 10 seconds, close the connection

        while True:
            time.sleep(5)
            self.request.sendall("heartbeat".encode())
            time.sleep(10)
            if self.request.recv(1024).strip() != "heartbeat".encode():
                #remove the connection from the list
                self.connection_list.remove(self.request)
                self.request.close()
                break    

if __name__=="__main__":
    #call instance of zookeeper with necessary ports
    #run broker( the socket part of it atleast to test out connections)
    #TODO 
    pass
