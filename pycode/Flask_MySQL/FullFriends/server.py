from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import MySQLConnector

app = Flask (__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    results = mysql.query_db(query)
    return render_template('index.html', all_friends=results)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
            'first_name': request.form['firstname'],
            'last_name': request.form['lastname'],
            'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    query = "SELECT * FROM friends WHERE id=:specific_id"
    data = {'specific_id':id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', one_friend=friends[0])

@app.route('/friends/<id>', methods=['POST'])
def updated(id):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id"
    data = {
            'first_name': request.form['firstname'],
            'last_name': request.form['lastname'],
            'email': request.form['email'],
            'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id=:id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
