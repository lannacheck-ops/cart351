from flask import Flask
app = Flask(__name__)

#@app.route("/") and index go together so the @app.route("/")always goes on top. It basically means when the user puts a "/" in the url it runs the index function
@app.route("/")
def index():
    return ' Hello CART 351!'

@app.route("/about")
def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>'

#The variable name in th app route and in the function argument must be exactly the same so as to not run into errors
@app.route("/user/<name>")
def user_profile(name):
    # we will use templates sooN!
    return f"<h2> This is <span style = 'color:orange'>{name}'s</span> profile page" 

@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    # we will use templates sooN!
    return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"

@app.route("/cat/<catname>")
def cat_route(catname):
    if catname[-1] != 'y':
        catname = catname[:-2] + 'y'
    else:
        catname = catname[:-2] + 'iful'
    return f"<h2>{catname}</h2>"

#Keep app.run() at the bottom
app.run()