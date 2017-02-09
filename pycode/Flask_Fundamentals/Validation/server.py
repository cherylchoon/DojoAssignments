from flask import Flask, render_template, request, redirect, session, flash

app = Flask (__name__)
app.secret_key = 'banana'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(request.form['name']) == 0:
        flash("Error: Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) == 1:
        flash("Error: Comment cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Error: Comment is too long!")
        return redirect('/')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)
