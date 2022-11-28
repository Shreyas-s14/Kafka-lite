import io
from flask import Flask, request, jsonify
from PIL import Image


app = Flask(__name__)
port = 4002

@app.route('/', methods=["GET"])
def message():
    message = "Flask server running on port {}...".format(port)
    
    return message

@app.route("/process", methods=["POST"])
def predict():
    if request.method == "POST":
        if request.files.get("text"):
            # read the image in PIL format
            text = "Wassup bwoi!!"

    # return a JSON response
    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(port=port,
            debug=True)