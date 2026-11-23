from flask import Flask,render_template,request,redirect, url_for,session 
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo
from dotenv import load_dotenv

import os

load_dotenv()  # Load variables from .env and .flaskenv
db_name = os.getenv('DATABASE_NAME')
db_user = os.getenv('MONGODB_USERNAME')
db_pass = os.getenv('MONGODB_PASSWORD')
# print(db_user)


uri = os.getenv("MONGODB_URI")
uri = uri + f"/{db_name}?retryWrites=true&w=majority"

print(uri)
app = Flask(__name__)

# set a config var
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
# try:
#     #get details of the client
#     print (mongo.cx)
#     print("You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
try:
    #get details of the client
    print (mongo.cx)
    #get db
    print (mongo.db)
    #get collection
    print (mongo.db.plantRepo)
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)

result = mongo.db.plantRepo.insert_one({"testKeyMon":"testValueMon"})
print(result)

