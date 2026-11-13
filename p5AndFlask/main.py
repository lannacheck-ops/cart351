 
from flask import Flask,render_template,request
import os
import json

app = Flask(__name__)
# a route
@app.route('/')
def index():
    return render_template("index.html")


# another route
@app.route('/p5BreakOut')
def runpP5():
    return render_template("p5_BreakOut.html")



# for the get from p5
@app.route('/getDataFromP5')
def getDataFromP5():
    #give back request.args
    app.logger.info(request.args["id"])
    app.logger.info(request.args["score"])
   # Check if the file exists (can be a file or directory)
    filePath="filesForP5/p5Data.json"
    if os.path.exists(filePath):
        jsonFile = ""
        app.logger.info("file exists")
        jsonFile = open(filePath, "r")
        theList = []
        theList = json.load(jsonFile)
        # check if id is in the list
        nameExists = False
        oldData = ""
        print(theList)
        for el in theList:
            if el["id"].upper() ==  request.args["id"].upper():
                print(el["id"])
                nameExists = True
                oldData = el["score"]
                el["score"] = request.args["score"]
                break # This exits the loop entirely
        #clear the file
        #jsonFile.truncate(0)
        jsonFile.close()
        jsonFile_write = open(filePath, "w")
        if nameExists ==True: 
            print(request.args)
            json.dump(theList,  jsonFile_write, indent =4)
            jsonFile_write.close()
            return({"inFile":"true","score":oldData})
        else:
            print("newName")
            theList.append(request.args)
            json.dump(theList, jsonFile_write, indent =4)
            jsonFile_write.close()
        return({"inFile":"false"})
    # # file not existing
    else:
        app.logger.info("file not exists")
        #open file for writing
        jsonFile = open(filePath, "w")
        list_m = [request.args]
        json.dump(list_m, jsonFile, indent =4)
        jsonFile.close()

    return({"inFile":"false"}) 

app.run(debug = True)