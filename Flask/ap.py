
from flask import Flask, render_template, request

app=Flask(__name__)
#__name__ reffers to name of current which simply guiding flask that turn this file whatever is name into flask application


@app.route("/") #This is know as decorator in python 
#This @app.route is just saying when the index function will be called. 




def index(): 
    name=request.args.get("name")#This is taking a argument from user which user put afters /?name=
    return render_template("index.html",nam=name)
#So far we created a fucniton index when user call this function it's simply 
# render i.e prints the index.html file to user screen 


@app.route("/bf")
def user():
    return render_template("bf.html")

@app.route("/sea")
def asd():
    return render_template("/gg/ggo.html")

@app.route("/hello")
def hel():
    return render_template("/hello.html")