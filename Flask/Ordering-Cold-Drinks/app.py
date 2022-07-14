# Learn how to add session and create a db to store user name and password and verfied users should login

from cs50 import SQL 
from flask import Flask, request, redirect,render_template

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


