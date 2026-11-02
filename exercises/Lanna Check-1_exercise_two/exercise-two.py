from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
# Task-1: GET REQUEST
@app.route("/t1")
def t1():
    return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria", methods = ['POST', 'GET'])
def getSearchCriteria():
    #fill me in :
    #replace the empty space to be url encoded
    base_url = 'https://images-api.nasa.gov/search'
    app.logger.info(request.form["search_query"])
    url_NASA_image = requests.get(base_url, params={'q': request.form["search_query"] , 'media_type': 'image'})
    app.logger.info('https://images-api.nasa.gov'+ 'q=' + request.form["search_query"] + 'media_type=image')
    data = url_NASA_image.json()
    # First element app log
    # app.logger.info(data['collection']['items'][0])
    firstEl = data['collection']['items'][0]
    imgFromNasa = firstEl['links'][0]['href']
    app.logger.info(imgFromNasa)
    description = firstEl['data'][0]['description']
    app.logger.info(description)
    return render_template("t1.html",
                              have_results = True,
                              description=description,
                              imgPath = imgFromNasa
                                           
                           )
    pass

#*************************************************
# #Task-2: GET REQUEST
# @app.route("/t2")
# def t2():
#     return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():
 #fill me in :
#  return render_template("t2.html",images=encodedImageLinks)
    pass
#*************************************************

#run
app.run(debug=True)