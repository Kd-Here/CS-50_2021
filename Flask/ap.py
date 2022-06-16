
from flask import Flask, render_template, request

app=Flask(__name__)
#__name__ reffers to name of current which simply guiding flask that turn this file whatever is name into flask application


@app.route("/") #This is    know as decorator in python 
#This @app.route is just saying when the index function will be called. 




def index(): 
    #yourname=request.args.get("nav")#This is taking a argument from user which user put afters /?nav=
    #return render_template("index.html",nam=yourname) #This is code if there is argument and we pass it through return commnad.
    return render_template("index.html") #This is code if there is no argument
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


@app.route("/form")
def form():
    return render_template("fo.html")

@app.route("/greet")
def gre():
    tname=request.args.get("username")    
    return render_template("greeting.html",na=tname)


@app.route("/ext")
def lay():
    return render_template("child_layout.html")

@app.route("/greeta")
def greeta():
    tname=request.args.get("username")    
    return render_template("child_greet.html",na=tname)

#WE can also have post method for route app
# @app.route("/greeta", methods=["POST"])
# def greeta():
#     return render_template("child_greet.html")
#Don't forget to make form method post.





