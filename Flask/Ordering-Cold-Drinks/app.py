# Learn how to add session and create a db to store user name and password and verfied users should login

from cs50 import SQL 
from flask import Flask, render_template_string, request, redirect,render_template,session
from flask_session import Session


app=Flask(__name__)




#Creating a storage i.e db for user order!
storage=SQL('sqlite:///pepsi_store.db')

# Tabele config:-
#  CREATE TABLE cart(        
#    ...> user_id INTEGER PRIMARY KEY,
#    ...> order_name TEXT NOT NULL);


# Creating a list of all Pepsi
All_Pepsi=[
    "NITRO PEPSI",
    "DIET PEPSI",
    "BLACK PEPSI",
    "NITRO VANILLA",
    "DARK MANGO PEPSI",
    "DIET WILD CHERRY",
    "MANGO ADDED SUGAR"
]


# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)





app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bookscollection',methods=["GET", "POST"])
def show_Books():
    return render_template('books.html',showing_ba=All_Pepsi)

@app.route('/sf',methods=["GET", "POST"])
def ad():
    prd=request.form.get('product')
    storage.execute('INSERT INTO cart (order_name) VALUES (?)', prd)
    return redirect('/bookscollection')


@app.route('/login',methods=['POST',"GET"])
def login():
    if not session.get('name'):
        return render_template('login.html')
    return redirect('/logged')

@app.route('/logged',methods=['POST',"GET"])
def logg():
    if request.method == "POST":
        session['name']=request.form.get('username')
        return redirect('/Showcatlog')
    return render_template('login.html')

@app.route('/logout',methods=['POST',"GET"])    
def lgo():
    session["name"] = None
    storage.execute('DELETE FROM cart')
    return redirect("/")
    



@app.route('/MyCart',methods=['POST',"GET"])
def faag():
    return redirect('/show')

@app.route('/show', methods=["POST","GET"])
def show_cart_content():
    showin=storage.execute('SELECT * FROM cart')
    return render_template('show.html',injing=showin)

@app.route('/remove',methods=['POST','GET'])
def afFA():
    storage.execute('DELETE FROM cart')
    return render_template('show.html')


@app.route('/Showcatlog' ,methods=['POST','GET'])
def nodha():
    return render_template('catlog.html')


# VIA products :-
@app.route('/productdd', methods=['POST','GET'])
def afdaf():
    prda=request.form.get('submit_button')
    storage.execute('INSERT INTO cart (order_name) VALUES (?)', prda)
    return render_template('catlog.html')


