



from flask import Flask
from flask_mail import Mail, Message
from cs50 import SQL
from flask import Flask, render_template, request, redirect
db = SQL("sqlite:///Froshver3.db")


   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

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

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'waitingforyou9899@gmail.com'
app.config['MAIL_PASSWORD'] = 'qflhewmbvikuyjhj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/mail", methods=["POST"])
def sendmail():
   registrants = db.execute("SELECT * FROM registrants")
   for registrant in registrants:      
         msg = Message(
                     'Hello',
                     sender ='waitingforyou9899@gmail.com',
                     recipients = ['fqkwgihiuafsghxzve@kvhrr.com']
                     )
         msg.body = 'Hello the person registered for our sport program are:-\n  Flask message sent from Flask-Mail . The person submitted the data  '+registrant['name']+" Selected this sport " +registrant['sport']
         mail.send(msg)
   return render_template("mail.html")



# Just to check the registered players with sports.
# a=[]
# b=[]
# registrants = db.execute("SELECT * FROM registrants")
# for anad in registrants:
#    a.append(anad['name'])
#    b.append(anad['sport'])

# print(a)
# print(b)

