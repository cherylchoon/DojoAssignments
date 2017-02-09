from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'Peanut'

@app.route('/')
def counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    return render_template('index.html')

@app.route('/plustwo')
def plusTwo():
    session['visits'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
