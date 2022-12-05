from flask import Flask, jsonify, request
from db import *
import string
import random

app = Flask(__name__)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.get('/')
def index():
    return jsonify({"message": "Welcome to Plant API!"})

@app.get('/settings')
def settings():
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


@app.post('/deactivate/light')
def deactivateLight():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)


@app.post('/deactivate/fan')
def deactivateFan():
    data = request.get_json()
    data['_id'] = id_generator(10)
    x = sensorsDB.find_one({'name': data['name']})
    if x is None:
        sensorsDB.insert_one(data)
    else:
        sensorsDB.update_one({"name": data['name']}, {"$set": {'value': data['value']}})
    return jsonify(data)

@app.post('/deactivate/pump')
def deactivatePump():
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
    x = settingsDB.find({})
    if data['selected'] == True:
        for i in x:
            if i['selected'] == True:
                settingsDB.update_one({"_id": i['_id']}, {"$set": {'selected': False}})
            else:
                continue
    settingsDB.insert_one(data)
    return jsonify({"message": "successfully added!", 
                    "data": data})
    
@app.post('/delete/settings')
def deleteSettings():
    data = request.get_json()
    s = settingsDB.find_one({"_id": data['_id']})
    if s['selected'] == True:
        settingsDB.update_one({"_id": "Y3DYTVQJST"}, {"$set": {'selected': True}})
    settingsDB.delete_one({"_id": data['_id']})
    return jsonify({'message': 'Successfully deleted!', "data": data})

@app.post('/update/settings')
def updateSettings():
    data = request.get_json()
    x = settingsDB.find({})
    if data['selected'] == True:
        for i in x:
            if i['selected'] == True:
                settingsDB.update_one({"_id": i['_id']}, {"$set": {'selected': False}})
            else:
                continue
    settingsDB.update_one({"_id": data['_id']}, {"$set": data})
    return jsonify({"message": "Successfully updated", 'data': data})


@app.get('/get/setting')
def get_setting():
    x = settingsDB.find_one({'selected': True})
    return jsonify(x)

@app.get('/activate/fan')
def activate_fan():
    sensorsDB.update_one({"name": "fan"}, {"$set": {"value": True}})
    return jsonify({"data" : "done"})

@app.get('/activate/pump')
def activate_pump():
    sensorsDB.update_one({"name": "pump"}, {"$set": {"value": True}})
    return jsonify({"data" : "done"})

@app.get('/activate/led')
def activate_led():
    sensorsDB.update_one({"name": "led"}, {"$set": {"value": True}})
    return jsonify({"data" : "done"})


@app.get('/deactivate/fan')
def deactivate_fan():
    sensorsDB.update_one({"name": "fan"}, {"$set": {"value": False}})
    return jsonify({"data" : "done"})

@app.get('/deactivate/pump')
def deactivate_pump():
    sensorsDB.update_one({"name": "pump"}, {"$set": {"value": False}})
    return jsonify({"data" : "done"})

@app.get('/deactivate/led')
def deactivate_led():
    sensorsDB.update_one({"name": "led"}, {"$set": {"value": False}})
    return jsonify({"data" : "done"})


@app.post('/select/setting')
def select_setting():
    data = request.get_json()
    x = settingsDB.find({})
    for i in x:
        if i['_id'] == data["_id"]:
            settingsDB.update_one({"_id": data['_id']},{"$set" : {"selected": True}})
        else:
            settingsDB.update_one({"_id": i['_id']},{"$set" : {"selected": False}})
    d = settingsDB.find_one({"selected": True})
    return jsonify(d)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
