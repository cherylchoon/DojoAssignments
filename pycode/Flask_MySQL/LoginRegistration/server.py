from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask (__name__)
app.secret_key = 'banana'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/authentication', methods=['POST'])
def authentication():
    if request.method == 'POST':
        username = request.form['login_username']
        password = request.form['login_password']
        pw_hash = bcrypt.generate_password_hash(password)
        user_query = "SELECT * FROM users WHERE users.email = :email"
        query_data = { 'email': username, 'password': password}
        user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['password'], password) and len(password) > 1:
        session['userid'] = user[0]['id']
        session['username'] = user[0]['first_name']
        return redirect('/wall')
    else:
        flash("ERROR: Invalid username/password!")
    return redirect('/login')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')

@app.route('/wall')
def message_wall():
    query_user_message = "SELECT messages.id as id, DATE_FORMAT(messages.created_at, '%M %D %Y %l:%i %p') as date, first_name, last_name, message FROM messages JOIN users ON users.id = user_id ORDER BY date DESC"
    all_messages = mysql.query_db(query_user_message)

    query_user_comment = "SELECT comments.id, comment, DATE_FORMAT(comments.created_at, '%M %D %Y %l:%i %p') as date, message_id, user_id, first_name, last_name FROM comments JOIN users ON users.id = user_id"
    all_comments = mysql.query_db(query_user_comment)

    # create a dictionary
    # key = message_id
    # value = [comments]
    # {1: [{comment 1.1}, {comment 1.2}, {comment 1.3}],
    #  2: [{comment 2.1}, {comment 2.2}, {comment 2.3}],
    #  3: [{comment 3.1}, {comment 3.2}, {comment 3.3}]}

    return render_template('wall.html', messages=all_messages, comments=all_comments)

@app.route('/post_message', methods=['POST'])
def create_message():
    message = request.form['message']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
            'user_id': session['userid'],
            'message': message
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/post_comment/<id>', methods=['POST'])
def create_comment(id):
    comment = request.form['commentbox']
    valid = False
    if len(comment) > 0:
        valid = True
    if valid:
        query = "INSERT INTO comments (comment, created_at, user_id, message_id) VALUES (:comment, NOW(), :user_id, :message_id)"
        data = {
                'comment': comment,
                'user_id': session['userid'],
                'message_id': id
                }
        mysql.query_db(query, data)
    if not valid:
        flash("ERROR: Comment field cannot be empty!")
    return redirect('/wall')

@app.route('/delete_comment/<id>', methods=['POST'])
def delete_comment(id):
    query = "DELETE FROM comments WHERE id=:comment_id"
    data = {'comment_id': id}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/register', methods=['POST'])
def create_user():
    valid = True
    if len(request.form['firstname']) < 2 or not NAME_REGEX.match(request.form['firstname']):
        flash("ERROR: First Name is invalid!")
        valid = False
    if len(request.form['lastname']) < 2 or not NAME_REGEX.match(request.form['lastname']):
        flash("ERROR: Last Name is invalid!")
        valid = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("ERROR: Email is invalid!")
        valid = False
    if len(request.form['password']) < 8 or not PASSWORD_REGEX.match(request.form['password']):
        flash("ERROR: Password has to be at least 8 characters & contain at least one uppercase letter and number!")
        valid = False
    if request.form['password'] != request.form['confirm']:
        flash("ERROR: Password and Confirm Password are different!")
        valid = False
    if valid:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
        data = {
                'first_name': request.form['firstname'],
                'last_name': request.form['lastname'],
                'email': request.form['email'],
                'password': bcrypt.generate_password_hash(request.form['password'])
        }
        user = mysql.query_db(query, data)
        session['userid'] = user
        session['username'] = request.form['firstname']
        flash("Thank you for your registration!")
        return redirect('/wall')
    return redirect('/')


app.run(debug=True)
