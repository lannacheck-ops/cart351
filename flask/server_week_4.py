from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pineapples.html")

@app.route('/favfruit')
def favfruit():
    return render_template("pineapple2.html")

app.run(debug = True)