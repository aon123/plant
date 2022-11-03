from flask import Flask, jsonify
from db import *
import string
import random

app = Flask(__name__)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.get('/')
def hello_world():
    d = settingsDB.find({})
    data = [i for i in d]
    return jsonify(data)

if __name__ == "__main__":
    app.run()