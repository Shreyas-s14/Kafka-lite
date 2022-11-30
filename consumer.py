from consumer_lib import *
c = consumer()

#Arg parse sets flag,if flag present 'True' else 'False'
flag = False

topic = str(input("Enter Topic Name to subscribe to or enter xzzx to get out"))
client,offset = c.connection(topic)

print(c.request_topic(client,topic,offset,flag))