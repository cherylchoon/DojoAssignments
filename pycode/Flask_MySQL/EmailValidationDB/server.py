from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask (__name__)
app.secret_key = 'banana'
mysql = MySQLConnector(app, 'email')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validation', methods=['POST'])
def valid():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
        data = {
                'email': request.form['email']
        }
        mysql.query_db(query, data)
        session['user'] = request.form['email']
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    email = mysql.query_db(query)
    return render_template('success.html', all_emails=email)

@app.route('/delete_email', methods=['POST'])
def delete():
    email_id = int(request.form['emailid'])
    query = "DELETE FROM emails WHERE id=:id"
    data = {'id': email_id}
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
