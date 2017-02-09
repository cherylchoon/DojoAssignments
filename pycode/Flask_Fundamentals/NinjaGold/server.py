import random
from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
app.secret_key = 'samurai'

@app.route('/')
def index():
    if 'activities' not in session:
        session['activities'] = []
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/processmoney', methods=['POST'])
def amtGold():
    session['places'] = request.form['building']
    if session['places'] == "farm":
        session['gold'] = random.randrange(10,21)
    elif session['places'] == "cave":
        session['gold'] = random.randrange(5,11)
    elif session['places'] == "house":
        session['gold'] = random.randrange(2,6)
    elif session['places'] == "casino":
        session['gold'] = random.randrange(-50,51)

    if session['gold'] > 0:
        session['activities'].insert(0,"Earned " + str(session['gold']) + " golds from the " + session['places'])
    else:
        session['activities'].insert(0,"Entered a casino and lost " + str(-session['gold']) + " golds... Ouch...")

    session['counter'] += session['gold']
    return redirect('/')
app.run(debug=True)
