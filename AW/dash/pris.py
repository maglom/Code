# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import datetime
import json
import time
from decimal import ROUND_UP
from math import ceil

import pandas as pd
import plotly.express as px
import requests

import dash
from dash import Dash, dcc, dependencies, html


def get_price(antall, coin=11):
    tidls = []
    verdils = []
    kurs = {}
    for i in range(antall):
        url = r'''https://api2.binance.com/api/v3/ticker/24hr'''
        response = requests.get(url)
        # test if the respons was ok
        assert response.status_code == 200
        dic_ = (json.dumps(response.json()))
        x = json.loads(dic_)
        tid = datetime.datetime.now()
        tiden = tid.strftime('%H:%M:%S')
        tidls.append(tiden)
        verdils.append(float(x[coin]['lastPrice']))
        print(tidls[-1], verdils[-1])
        time.sleep(1)
    kurs['tid'] = tidls
    kurs['verdi'] = verdils
    return(kurs, x[coin]['symbol'])


dic = get_price(10, 11)

app = Dash(__name__)

header = html.H1(f'{dic[1]} Kurs')

info = html.Div(f'''
        Her kan du se kursutviklingen i {dic[1]} den siste tiden!
    ''')

data = dic[0]
fig = px.line(data, x='tid', y='verdi')

graph = dcc.Graph(id='kurs', figure=fig)

app.layout = html.Div([header, info, graph])
if __name__ == '__main__':
    app.run_server(debug=False)
