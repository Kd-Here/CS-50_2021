from cs50 import SQL
from flask import Flask, render_template, request, redirect

app=Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"] = True

db=SQL("sqlite:///shows.db")


@app.route('/')
def ad():
    return render_template('index.html')

@app.route('/serch',methods=["GET"])
def searching():
    dfa=request.args.get('q')
    print(dfa)
    showing=db.execute("SELECT * FROM shows WHERE title LIKE ?","%" +dfa+ "%")
    return render_template('search.html',shown=showing)