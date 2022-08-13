from flask import Flask,jsonify
import db1
import requests

app = Flask(__name__)

root = '''Welcome to the root page
<p><a href="/get_youngest_oscar_winner">get_youngest_oscar_winner</a></p>
<p><a href="/multiple_oscar_winners/">Multiple Winners</a></p>'''

@app.route('/')
def root_page():
    return root


@app.route('/get_youngest_oscar_winner')
def get():
    return jsonify(db1.get_youngest_oscar_winner())

@app.route('/multiple_oscar_winners/<num_oscar>')
def get_oscar(num_oscar):
    return db1.multiple_oscar_winners(num_oscar)


app.run(debug=True)


