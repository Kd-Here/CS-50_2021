# https://pythonbasics.org/flask-sqlite/

import sqlite3
import sqlite3 as sql

coa=sqlite3.connect('info.db')
coa.execute('CREATE TABLE students (nav TEXT, addd TEXT, cito TEXT, pinto TEXT)')
coa.close()

from flask import Flask, render_template, request
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def login():
    return render_template('index.html')


@app.route('/su')
def stu():
    return render_template('student.html')

@app.route("/storeinfo" ,methods=['POST','GET'])
def are():
    if request.method =="POST":
        try:
            nav=request.form['nav']
            addd=request.form['pata']
            cito=request.form['city']
            pinto=request.form['pin']
        

            with sql.connect('info.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO students (nav,addr,city,pin) VALUES (?,?,?,?)",(nav,addd,cito,pinto))

                con.commit()
                msg="recorded successfully added!"
        except:
            con.rollback()
            msg="erro in insertion"

        finally:
            return render_template('result.html',mgg=msg)
            con.close()

@app.route('/list')
def list():
   con = sql.connect("info.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

@app.route('/')
def home():
   return render_template('index.html')
