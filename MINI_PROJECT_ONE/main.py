from flask import Flask,render_template,request,url_for,redirect,session
import requests
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/objectives')
def objectives():
    return render_template('objectives.html')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    stars = []
    base_url = "https://spacecatalog.org/api/v1/objects"
    response = requests.get(base_url, params={"limit": 10, "category": "planet"})
    data = response.json()
    for items in data['objects']:
        star = items['name']
        stars.append(star)
    app.logger.info(type(data['objects']))
    app.logger.info(data)
    planet = request.args.get('object')
    
    return render_template('research.html', planet=planet)

app.run(debug=True)