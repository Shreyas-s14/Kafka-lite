import os

topic_name = "BossVarma"
data = "Hello this is Boss Varma.Nice to meet you."

dirnames = [name for name in os.listdir("./topics")]
print(dirnames)

if topic_name not in dirnames:
        os.chdir('./topics')
        os.mkdir(topic_name)

        path = './topic/{topicName}/{fileName}'.format(topicName = topic_name,fileName = topic_name+'.txt')
        with open(path,'w') as f:
            f.write(data)
            f.close()
else:
    path = './topic/{topicName}/{fileName}'.format(topicName = topic_name,fileName = topic_name+'.txt')
    with open(path,'w') as f:
        f.write(data)
        f.close()

