import argparse
from consumer_lib import *
c = consumer()

#Arg parse sets flag,if flag present 'True' else 'False'
flag1=argparse.ArgumentParser()
flag1.add_argument("--from-beginning",help="if present then it will start from beginning",action="store_true")
args=flag1.parse_args()

if args.from_beginning:
    flag=True
else:
    flag=False



topic = str(input("Enter Topic Name to subscribe to or enter xzzx to get out"))
client,offset = c.connection(topic)

print(c.request_topic(client,topic,offset,flag))