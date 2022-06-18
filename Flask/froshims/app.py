from flask import Flask,  render_template, request
#Flask is the function which kick start everything, render_template is used to print or serve template, request is used to get user request or input
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def formfilled():
    tname=request.args.get("name")
    fgame=request.args.get("game")
    formupdate=request.args.get("update")
    return render_template("register.html",yourname=tname,yourgame=fgame,updation=formupdate)