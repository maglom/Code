from flask import Flask, request, jsonify
import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
response = response.text



app = Flask(__name__)

@app.route('/')
def index():
    #return response
    if request.args:
        return 'HALLA'   
    return 'BALLA'

app.run(debug=True)