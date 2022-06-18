from flask import Flask,  render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def greet(): 
    #validate submission
    if not request.form.get("name") or request.form.get("sport") not in ["Football", "Baseball", "Volleyball"]:
        return render_template("Failure.html")
    
    #Confirm Regristration
    return render_template("success.html")