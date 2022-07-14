from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# This when set to true our all template are autoreloaded!
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# We are creating session as dictionary with key as model and value of model is username
@app.route("/")
def index():
    if not session.get("model"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["model"] = request.form.get("username")
        return redirect("/")
    return render_template("login.html")


# show items purchased!
@app.route('/Showcatlog')
def asd():
    pass

@app.route("/logout",methods=["GET", "POST"])
def logout():
    session["model"] = None
    return redirect("/")


#Items avaialbe to buy
@app.route('/bookscollection', methods=["GET", "POST"])
def show_Books():
    return render_template('books.html')


@app.route('/singup',methods=["GET","POST"])
def shod():
    return render_template('singup.html')




# SHowing buyed products
@app.route('/show', methods=["GET", "POST"])
def show_cart_content():
    return render_template('show.html')


