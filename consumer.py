import os
import requests


def send_image(url_link, text_path):
    info = open(text_path, "rb").read()
    payload = {"text": info}

    response = requests.post(url_link, files=payload).json()

    return response


resp = send_image("http://localhost:4002/process", "./content/text1.txt")
print(resp)