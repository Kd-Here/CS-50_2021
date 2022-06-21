#In this we are storing user data i.e their name and choice of sport selected, if wrongly submitted report them with error message i.e html page

from flask import Flask, render_template, request, redirect
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


    #Valditating name
    name=request.form.get("name")
    if not name: #simply remember if not as jar nsel tar
        return render_template("error.html", message="Missing Name")
        # if not explained https://www.jquery-az.com/4-demos-python-if-not-and-not-in-operator/#:~:text=The%20'not'%20is%20a%20Logical,used%20in%20the%20if%20statements.&text=If%20x%20is%20True%2C%20then,as%20false%2C%20otherwise%2C%20True.


    #Validating sport
    sport = request.form.get("sport")
    if not s: #simply means if sport is not filled
        return render_template("error.html", message="Missing Sport")
    
    if sport not in s: #simply means sport nsel s madhey tarch
        return render_template("error.html", message="Invalid Sport")


    #Storing User name
    REGISTRANTS[name]=sport
     
    #Confirm registration
    return redirect("/registrants")



@app.route("/registrants")
def regost():
    return render_template("registrants.html",registrants=REGISTRANTS,ad=i)

# This to keep count on registrants
# a=len(REGISTRANTS.keys())
# print(f'The value of keys occured or dictionray iterated is{a}')
# print(REGISTRANTS)
# Not working since we are not adding key value to dictionary here

# for i in range(1,1000):
    # find way to run loop when @app.route ("/registrants") is exceuted that time excute loop
    # use if app... excute i+1,
