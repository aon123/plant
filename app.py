from flask import Flask, jsonify, request
from db import *
import string
import random

app = Flask(__name__)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.get('/settings')
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

@app.post('/sensor/temp')
def setTemp():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/sensor/humidity')
def setHumid():
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
def getSensorbyName(name):
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


@app.post('/add/settings')
def createSettings():
    data = request.get_json()
    data['_id'] = id_generator(10)
    settingsDB.insert_one(data)
    return jsonify({"message": "successfully added!", 
                    "data": data})
    
@app.post('/delete/settings')
def deleteSettings():
    data = request.get_json()
    settingsDB.delete_one({"_id": data['_id']})
    return jsonify({'message': 'Successfully deleted!', "data": data})

@app.post('/update/settings')
def updateSettings():
    data = request.get_json()
    print(data)
    settingsDB.update_one({"_id": data['_id']}, {"$set": data})
    return jsonify({"message": "Successfully updated", 'data': data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
