from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])')
app = Flask (__name__)
app.secret_key = 'banana'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    valid=True

    if len(request.form['email']) == 0:
        flash('Email field cannot be blank!')
        valid=False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Error: Invalid Email Address!")
        valid=False

    if len(request.form['first_name']) == 0:
        flash('First name field cannot be blank!')
        valid=False
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Error: Invalid First Name!")
        valid=False

    if len(request.form['last_name']) == 0:
        flash('Error: Last name field cannot be blank!')
        valid=False
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Error: Invalid Last Name!")
        valid=False

    if len(request.form['password']) == 0:
       flash('Error: Password field cannot be blank!')
       valid=False
    elif len(request.form['password']) < 8:
        flash('Error: Password should be more than 8 characters!')
        valid=False

    if len(request.form['confirm_password']) == 0:
        flash('Error: Confirm password field cannot be blank!')
        valid=False
    elif request.form['password'] != request.form['confirm_password']:
        flash('Error: Password and confirm password does not match!')
        valid=False
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Passwords must contain at least 1 uppercase letter and 1 numeric values.')
        valid=False

    if valid: 
        flash('Thank you for submitting your information!')
        return redirect('/')

    return redirect('/')

app.run(debug=True)
