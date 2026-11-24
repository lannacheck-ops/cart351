from flask import Flask,render_template,request,redirect, url_for,session 
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo
from dotenv import load_dotenv
#import datetime
from datetime import datetime 

import os

format_string = "%Y-%m-%d"
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
app.secret_key = 'BAD_SECRET_KEY'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/insertTestPage')
def insertTest():
    session.pop('ids', default=None)
    return render_template("testInsert.html")

# a route
@app.route('/insertMany')
def insertMany():
  
    data = [
{'owner_name': 'Sarah',
'plant_name': 'Snake Plant',
'birthDate':datetime.strptime("2002-06-12", format_string),
'geoLoc': 'Montreal',
'descript': 'Description for the plant',
'imagePath': 'images/one.png'
},
{
'owner_name': 'Sarah',
'plant_name':'Cactus',
'birthDate':datetime.strptime("2005-06-13", format_string),
'geoLoc':'Toronto',
'descript':'Description for the plant',
'imagePath': 'images/seven.png'
},
 
 {
'owner_name': 'Sarah',
'plant_name': 'Agapanthus',
'birthDate': datetime.strptime("2003-03-19", format_string),
'geoLoc': 'Halifax',
'descript': 'Description for the plant',
'imagePath': 'images/seventeen.png'
},
 {
'owner_name': 'Stephen',
'plant_name': 'Baby Rubber Plant',
'birthDate ': datetime.strptime("1997-07-18", format_string),
'geoLoc': 'Edinborough',
'descript':'Description for the plant',
'imagePath': 'images/ten.png'
},
 
{
'owner_name': 'Stephen',
'plant_name': 'Dahlia',
'birthDate':datetime.strptime("2000-05-06", format_string),
'geoLoc':'London',
'descript':'Description for the plant',
'imagePath': 'images/thirteen.png'
},
 
{
'owner_name': 'Harold',
'plant_name': 'Daphne',
'birthDate': datetime.strptime("2012-10-21", format_string),
'geoLoc':'New York',
'descript':'Description for the plant',
'imagePath': 'images/three.png'
},
{
'owner_name' : 'Martha',
'plant_name' : 'Daylily',
'birthDate':datetime.strptime("2017-08-21", format_string),
'geoLoc':'Paris',
'descript':'Description for the plant',
'imagePath': 'images/nine.png'
}
]
    try:
        # insert many works :)
        result = mongo.db.plantRepo.insert_many(data)
        session['ids'] = result.inserted_ids
        return redirect(url_for('testIds'))
    except Exception as e:
        print(e)

@app.route('/testIds')
def testIds():
    print(session['ids'])
    return render_template("testIds.html")

# a route
@app.route('/viewResults')
def viewResults():
    # #  All results
    # result = mongo.db.plantRepo.find()
    startTime = datetime.strptime("2003-01-12", format_string)
    # #  All results with birthdate greater than startTime
    # result= mongo.db.plantRepo.find({'birthDate':{'$gt':startTime}})
    endTime = datetime.strptime("2010-01-12", format_string)
     # Results btwn startTime and endTime
    # result = mongo.db.plantRepo.find(
    #     {'$and':[{'birthDate':{'$gt':startTime}},{'birthDate':{'$lt':endTime}} ]})
    # Results with ownernaem sarah or martha
    # result = mongo.db.plantRepo.find(
    #     {'$or':[{'owner_name':'Sarah'},{'owner_name':'Martha'} ]})
    # # Here - we are sorting by creation date smaller-larger ... if we change to -1, then it would be the opposite direction.
    # result = mongo.db.plantRepo.find(
    #     {'$or':[{'owner_name':'Sarah'},{'owner_name':'Martha'}]}).sort("birthDate",1)
    #  Sort and limit the number of results
    result = mongo.db.plantRepo.find(
        {'$or':[{'owner_name':'Sarah'},{'owner_name':'Martha'}]}).sort("birthDate",-1).limit(2)


    print(result)
    return render_template("viewResults.html",result=result)

@app.route('/updateOne')
def updateOne():
     try:
        updatedRepoItem= mongo.db.plantRepo.find_one_and_update(
            {'plant_name' :'Agapanthus'},
            {'$set':{'descript':'a more precise description'}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)


@app.route('/updatePoints')
def updatePoints():
     try:
        updatedRepoItem= mongo.db.plantRepo.find_one_and_update(
            {'user' :'maria'},
            {'$inc':{'points':2}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)

@app.route('/updateOneRepeat')
def updateOneRepeat():
     try:
        updatedRepoItem= mongo.db.plantRepo.find_one_and_update(
            {'owner_name' :'Sarah'},
            {'$set':{'descript':'a more precise description for all sarahs','title':'test123'}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
 
        print(e)

@app.route('/updateMany')
def updateMany():
     try:
        updatedRepoItem= mongo.db.plantRepo.update_many(
            {'owner_name' :'Sarah'},
            {'$set':{'descript':'a more precise description for all sarahs','title':'testALL'}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)

app.run(debug = True)

