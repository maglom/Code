import json
from flask import Flask, jsonify, request
import requests
from greier import *



app = Flask(__name__)

@app.route('/')
def index():
    return('''
    <a href="http://127.0.0.1:5000/search?=Skjærtorsdag">Skjærtorsdag</a>, 
<a href="http://127.0.0.1:5000/search?=Skjærtorsdag">Langfredag</a>,
<a href="http://127.0.0.1:5000/search?=Kristi himmelfartsdag">Kristi Himmelfartsdag</a>
''')

@app.route('/users')
def boi():
    return jsonify(response.json())

@app.route('/users/<id>')
def ide(id):
    response_json = response.json()
    return response_json[int(id)]

@app.route('/search')
def search():
    response_json = response.json()
    return jsonify(get_facts(get_norwegian_holiday_dates(request.args[''], 3)))
   
if __name__ == '__main__':
    app.run(debug=True)