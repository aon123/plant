from flask import Flask, jsonify, request
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

@app.post('/sensor/light')
def setLight():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)


@app.post('/sensor/moisture')
def setMoisture():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/sensor/temp/humidity')
def setTempHumid():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/sensor/pump')
def setPump():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/sensor/fan')
def setFan():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/sensor/led')
def setLed():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.get('/sensor/<string:name>')
def getMoisture(name):
    if name != "":
        x = sensorsDB.find_one({'name': name})
        if x is not None:
            return jsonify(x)
        else:
            return jsonify({"message": f"{name} not existing in DB"})
    else:
        return jsonify({'message': "Error! Enter sensor name"})
    

@app.get('/sensors')
def getSensors():
    x = sensorsDB.find({})
    data = [i for i in x]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)