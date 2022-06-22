#In this we are storing user data i.e their name and choice of sport selected, if wrongly submitted report them with error message i.e html page

from flask import Flask, render_template, request, redirect
app=Flask(__name__)

# import sqlite3
# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")

#     with open('C:\Users\Kajal\OneDrive\Desktop\Python\CS-50_2021\Flask\Froshver3\app.py', 'r') as sqlite_file:
#         sql_script = sqlite_file.read()

#     cursor.executescript(sql_script)
#     print("SQLite script executed successfully")
#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while executing sqlite script", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection is closed")


import sqlite3

Connecting_flask_db = sqlite3.connect('database-of-registrants.db')
print("Successfully created a database check a new file has created")

# Connecting_flask_db.execute('CREATE TABLE registrants (No. integer, NAME text, SPORTS text )')
Connecting_flask_db.execute('CREATE TABLE registrants (no_of_registratns integer PRIMARY KEY,name text NOT NULL,sports text NOT NULL);')
print("Table is created")
Connecting_flask_db.close()






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
    if request.method =="POST":
        try:
            name=request.form['name']
            sport=request.form['sport']
            
            with sql.connect('database-of-registrants.db') as con:
                cur=con.cursor()
                cur.excute('INSERT INTO registrants (no_of_registratns,name,sports) VALUES (?,?,?)',(a,name,sport))

                con.commit()
                msg="REcord added"
                   except:
                con.rollback()
                msg = "error in insert operation"
      
        finally:
            return render_template("result.html",msg = msg)
            con.close()


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
    return render_template("registrants.html",registrants=REGISTRANTS)

# This to keep count on registrants
# a=len(REGISTRANTS.keys())
# print(f'The value of keys occured or dictionray iterated is{a}')
# print(REGISTRANTS)
# Not working since we are not adding key value to dictionary here

# for i in range(1,1000):
    # find way to run loop when @app.route ("/registrants") is exceuted that time excute loop
    # use if app... excute i+1,

for name in REGISTRANTS:
    print(REGISTRANTS[name])