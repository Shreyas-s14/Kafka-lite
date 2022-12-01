import socket
import threading
import os
import json

#client part (zookeeper-broker)
client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client1.connect(('10.0.2.15',5000))

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
        # client1.send("Give ip_port".encode('utf-8'))
        # l = client1.recv(1024).decode()

        msg = client.recv(1024)
        here = msg.decode()
        print(f"The client said:{msg.decode()}")
        if msg.decode()=='p_update':
            # client.send(l.encode('utf-8'))
            while True:
                with open("./zookeeper/offset_metadata.txt","r") as f1:
                    meta = json.loads(f1.read())
                i = 0;prev=''
                while(i<3):

                    msg = client.recv(1024).decode()
                    msg = json.loads(msg)
                    topic = list(msg.keys())[0]
                    print(topic)
                    if topic not in meta:
                        meta[topic]={"off1":0,"off2":0,"off3":0}
                        off1=0;off2=0;off3=0
                        print(meta)
                    else:
                        d = meta[topic]
                        print(d)
                        off1 = d["off1"];off2= d["off2"];off3 = d["off3"]
                    
                    if prev=='':
                        prev=topic
                    dirnames = [name for name in os.listdir("./broker1")]
                    if topic not in dirnames:
                        os.chdir('./broker1')
                        os.mkdir(topic)
                        with  open('./topic/{topicName}/partition1.txt'.format(topicName = topic),'w+') as f:
                            f.write("--")
                        
                        with open('./topic/{topicName}/partition2.txt'.format(topicName = topic),'w+') as f:
                            f.write("--")
                        
                        with open('./topic/{topicName}/partition3.txt'.format(topicName = topic),'w+') as f:
                            f.write("--")
                        
                    if prev!=topic:
                        i=0
                        prev=topic
                    if i==0:
                        with  open(f'./broker1/{topic}/partition1.txt','a+') as f:
                            f.write(f"{off1+1}: {list(msg.values())[0]}\n")
                            meta[topic]["off1"]=meta[topic]["off1"]+1
                            f.close()
                    elif i==1:
                        with open(f'./broker1/{topic}/partition2.txt','a+') as f:
                            f.write(f"{off2+1}: {list(msg.values())[0]}\n")
                            meta[topic]["off2"]=meta[topic]["off2"]+1
                            f.close()
                    else:
                        with open(f'./broker1/{topic}/partition3.txt','a+') as f:
                            f.write(f"{off3+1}: {list(msg.values())[0]}\n")
                            meta[topic]["off3"]=meta[topic]["off3"]+1
                            f.close()
                    i+=1
                with open("./zookeeper/offset_metadata.txt", 'w') as json_file:
                    json_file.write(json.dumps(meta,indent=4))

        if here=='c_offset':
            msg = client.recv(1024).decode('utf-8')
            # msg = json.load(msg)
            topic = msg
            print(topic)
            dirnames = [name for name in os.listdir("./broker1")]
            with open("./zookeeper/offset_metadata.txt","r") as f1:
                    meta = json.loads(f1.read())
            if topic not in dirnames:
                os.chdir('./broker1')
                os.mkdir(topic)
                with  open('./topic/{topicName}/partition1.txt'.format(topicName = topic),'w+') as f:
                    f.write("--")
                
                with open('./topic/{topicName}/partition2.txt'.format(topicName = topic),'w+') as f:
                    f.write("--")
                
                with open('./topic/{topicName}/partition3.txt'.format(topicName = topic),'w+') as f:
                    f.write("--")
                off1 = 0;off2=0;off3=0
            else:
                off1 = meta[topic]["off1"];off2 = meta[topic]["off2"];off3 = meta[topic]["off3"]
            client.send(meta[topic].encode('utf-8'))
            d=client.recv(1024).decode('utf-8')
            offset=client.recv(1024).decode('utf-8')
            d=json.loads(d)
            offset = json.loads(offset)
            topic=list(d.keys())[0]
            flag = d[topic][0]
            if flag==True:
                with  open('./topic/{topicName}/partition1.txt'.format(topicName = topic),'r') as f:
                    v = f.readlines()
                    h = [i[2:] for i in v]
                    print(v)
                    client.send(h.encode('utf-8'))                
                with open('./topic/{topicName}/partition2.txt'.format(topicName = topic),'r') as f:
                    v = f.readlines()
                    h = [i[2:] for i in v]
                    print(v)
                    client.send(h.encode('utf-8'))  
                with open('./topic/{topicName}/partition3.txt'.format(topicName = topic),'r') as f:
                    v = f.readlines()
                    h = [i[2:] for i in v]
                    print(v)
                    client.send(h.encode('utf-8')) 
            else:
                with open("./zookeeper/offset_metadata.txt","r") as f1:
                    meta = json.loads(f1.read())
                if meta[topic]["off1"]-offset["off1"]:
                    with  open('./topic/{topicName}/partition1.txt'.format(topicName = topic),'r') as f:
                        v = f.readlines()
                        h = [i[2:] for i in v]
                        print(v)
                        client.send(h[offset["off1"]].encode('utf-8'))
                        offset["off1"] = meta[topic]["off1"]
                elif meta[topic]["off2"]-offset["off2"]:
                    with  open('./topic/{topicName}/partition2.txt'.format(topicName = topic),'r') as f:
                        v = f.readlines()
                        h = [i[2:] for i in v]
                        print(v)
                        client.send(h[offset["off2"]].encode('utf-8'))
                        offset["off2"] = meta[topic]["off2"]
                elif meta[topic]["off3"]-offset["off3"]:
                    with  open('./topic/{topicName}/partition3.txt'.format(topicName = topic),'r') as f:
                        v = f.readlines()
                        h = [i[2:] for i in v]
                        print(v)
                        client.send(h[offset["off3"]].encode('utf-8'))
                        offset["off3"] = meta[topic]["off3"]
        
        
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