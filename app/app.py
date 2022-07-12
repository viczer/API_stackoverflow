from flask import Flask, render_template, request, jsonify
import sys
sys.path.append('./scripts/')
from predictions import *


app = Flask(__name__)

@app.route('/')
def index():
    return ""


@app.route('/tags', methods = ['GET'])
def tags():

    question = request.args.get('question')
    predicted_tags = predire(question)
    nombre_tags = len(predicted_tags)
    predicted_tags = ' '.join(predicted_tags)

    return  jsonify({"question":question, "nombre_tags":nombre_tags, "tags":predicted_tags})


if __name__ == "__main__":
    app.run(debug=True)