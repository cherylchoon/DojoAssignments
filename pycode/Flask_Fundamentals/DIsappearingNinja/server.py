from flask import Flask, render_template, redirect, request

app = Flask (__name__)
app.secret_key = 'banana'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    valid = False
    if color != 'blue' or color != 'red' or color != 'orange' or color != 'purple':
        valid = True
    return render_template('ninja.html', color=color, valid=valid)

app.run(debug=True)
