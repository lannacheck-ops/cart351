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
    # Stores the Nasa base search url
    base_url = 'https://images-api.nasa.gov/search'
    app.logger.info(request.form["search_query"])
    # Request the url from the NASA API using the user's input as a query
    url_NASA_image = requests.get(base_url, params={'q': request.form["search_query"] , 'media_type': 'image'})
    app.logger.info('https://images-api.nasa.gov'+ 'q=' + request.form["search_query"] + 'media_type=image')
    # Store data as a JSON file (a python dictionary)
    data = url_NASA_image.json()
    # First element app log
    # app.logger.info(data['collection']['items'][0])
    # Get the first element in the items list
    firstEl = data['collection']['items'][0]
    # Get the first image in the links list
    imgFromNasa = firstEl['links'][0]['href']
    # Replace the empty space to with 20% to follow url syntax
    imgFromNasa.replace(' ', '20%')
    app.logger.info(imgFromNasa)
    # Get the description of the first element in the items list
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
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************

@app.route("/getSearchCriteria_adv", methods = ['POST', 'GET'])
def getSearchCriteria_adv():
 #fill me in :  
    base_url = 'https://images-api.nasa.gov/search'
    url_NASA_image = requests.get(base_url, params={'q': request.form["adv_search_query"] , 'media_type': 'image'})
    data = url_NASA_image.json()
    # Stores the list of all the elements in the items list
    allEl = data['collection']['items']
    # Creates an empty array every time a search is made
    encodedImageLinks = []
    # app.logger.info(firstEl['links'])
    # A for loop that iterates through the items list
    for items in allEl:
      # Gets the first image(href) in the links list for each element in the items list
      singleImage = items['links'][0]['href']
    #   app.logger.info(images['href'])   
      singleImage.replace(' ', '20%')
      # Appends the image to the array
      encodedImageLinks.append(singleImage)
   
    return render_template("t2.html",images=encodedImageLinks)
    pass
#*************************************************

#run
app.run(debug=True)