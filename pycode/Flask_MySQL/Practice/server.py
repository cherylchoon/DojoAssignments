from flask import Flask, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql_db = MySQLConnector(app, 'world')

@app.route('/')
def index():
    result = mysql_db.query_db('select * from cities')
    return render_template('index.html', cities=result)

@app.route('/country/<id>')
def find_by_country_id(id):
    criteria = {'country_id': id}
    result = mysql_db.query_db('select * from cities where country_id = :country_id', criteria)
    return render_template('index.html', cities=result)

@app.route('/country_code/<cc>')
def find_by_country_code(cc):
    criteria = {'code': cc}
    result = mysql_db.query_db('select * from cities where country_code = :code', criteria)
    return render_template('index.html', cities=result)

app.run(debug=True)
