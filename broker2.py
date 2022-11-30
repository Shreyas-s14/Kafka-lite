import io
import os

from flask import Flask, request, jsonify

app = Flask(__name__)
port = 4002

@app.route('/', methods=["GET"])
def message():
    message = "Flask server running on port {}...".format(port)
    
    return message

@app.route("/process", methods=["POST"])
def response():
    if request.method == "POST":
        if request.files.get("text"):
            text = "Wassup bwoi!!"

    return jsonify({"text": text})

def topic_creation(topic_name,data):
    dirnames = [name for name in os.listdir("./topics") if os.path.isdir(name)]
    if topic_name not in dirnames:
        os.chdir('./topics')
        os.mkdir(topic_name)
        path = './topic/{topicName}/{topicName}.txt'.format(topicName = topic_name)
        with open(path,'w') as f:
            f.write(data)
    path = './topic/{topicName}/{topicName}.txt'.format(topicName = topic_name)
    with open(path,'w') as f:
        f.write(data)



if __name__ == "__main__":
    app.run(port=port,
            debug=True)