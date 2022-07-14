from flask import Flask, redirect,render_template,request
from cs50 import SQL



app= Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

# This is class of cs50 which is from sql alchemy for sqltie
db=SQL('sqlite:///stroing_info.db')


@app.route("/")
def padf():
    return render_template('index.html')

@app.route("/register",methods=["POST"])
def registered():
    # TO get data from user which submits by form 
    req=request.form.get('nam')
    db.execute('INSERT INTO first (name) VALUES (?)',req)
    return redirect('/sub')

@app.route('/sub')
def showdata():
    showin=db.execute('SELECT * FROM first')
    return render_template('show.html',registered=showin)
