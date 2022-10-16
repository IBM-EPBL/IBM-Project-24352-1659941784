from site import USER_BASE
from flask import Flask, render_template, url_for, request, redirect
import sqlite3 assql

 
app=Flask(__name__)
app.secret_key ='shreesathyam'

@app.route('/')
defhome():
    con =sql.connect('user_base.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select *from user')

    users= cur.fetchall()
    con.close()
    returnrender_template('index.html',users=users)

@app.route('/about')
defabout():
    returnrender_template('about.html')
@app.route('/signin')
defsignin():
    returnrender_template('signin.html')
@app.route('/signup')
defsingup():
