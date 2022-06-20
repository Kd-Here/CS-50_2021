from flask import Flask,  render_template, request
app=Flask(__name__)



#Every time you see copy paste or equivalent to it rememeber you can do better
#So not in ["Foo..."] we are making global
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
    return render_template("index.html",sports=s)
 
@app.route("/register", methods=["POST"])
def greet(): 
    #validate submission
    if not request.form.get("name") or request.form.get("sport") not in s:
        return render_template("Failure.html")
    
    #Confirm Regristration
    return render_template("success.html")