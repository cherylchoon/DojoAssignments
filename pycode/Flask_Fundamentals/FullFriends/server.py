from flask import Flask, render_template, request, session, redirect, flash
from connection import MySQLConnector

app = Flask (__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    results = mysql.query_db(query)
    return render_template('index.html', all_friends=results)

app.run(debug=True)
