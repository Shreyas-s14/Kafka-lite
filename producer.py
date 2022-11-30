# import os
# import requests


# def send_text(url_link, text_path):
#     info = open(text_path, "rb").read()
#     payload = {"text": info,"id":123}

#     response = requests.post(url_link, files=payload).json()

#     return response


# resp = send_text("http://localhost:5000/process", "./content/text1.txt")
# print(resp)
from producer_lib import *
p = producer()

client = p.connection()



while True:
    topic = str(input("Enter Topic Name or xzzx to get out"))
    if topic == 'xzzx':
        break
    while True:
        mesg = str(input("Enter your message or enter exit to get out"))
        if mesg == 'exit':
            break
        else:
            p.send_message(client,topic,mesg)
    