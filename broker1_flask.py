import io
from flask import Flask, request, jsonify

app = Flask(__name__)
port = 5000

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
# while True:
#     print("hello world")
if __name__ == "__main__":
    #connect to zookeeper
    app.run(port=port,
            debug=True)