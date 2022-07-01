from flask import Flask, redirect, render_template, request, session
from flask_session import Session
app=Flask(__name__)


app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login",methods=['GET',"POST"])
def login():
    if request.method =="POST":
        first_name=request.form.get('da')
        # first_name is the var created in python and da is a form attribute which is requested means what user type in html form we request here.

        return render_template('login.html',user_name=first_name)
                                # user_name is jingar vairable which we display in html page using jingar and firs is python variable requested by html form
    else:
        return render_template('index.html')


@app.route("/logout",methods=['GET','POST'])
def logout():
    return render_template('logout.html')