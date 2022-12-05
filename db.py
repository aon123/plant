from pymongo import MongoClient


client = MongoClient("mongodb://plant:plant2022@43.201.136.217:27017/plant",authSource="admin")
db = client.plant
sensorsDB = db.sensors
settingsDB = db.settings
chatbotdb = client.chatbot
chatbotDB = chatbotdb.chatbot
menuDB = chatbotdb.menu
orderDB = chatbotdb.order

