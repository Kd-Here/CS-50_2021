from cs50 import SQL
from flask import Flask, render_template, request, redirect
db = SQL("sqlite:///Froshver3.db")


app=Flask(__name__)

REGISTRANTS ={}
#This is empty dictionary key value pair.

SPORTS ={   
    "Football",
    "Volleyball",
    "Baseball",
    "Bat-ball"
}
s=list(SPORTS)
s.sort()

@app.route("/")
def index():
    return render_template("index.html", sports=s)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # Remember registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    # Confirm registration
    return redirect("/registrants")


#If user wants to delete 
@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")
    # redirect is used to 
    #why not render_Template
    # return render_template("registrants.html")




@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)