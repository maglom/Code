import requests 
import json 
import datetime
import time
import plotly.express as px

tidls = []
verdi = []


url = f'''https://api2.binance.com/api/v3/ticker/24hr'''
 
while True: 
    response = requests.get(url) 

    # test if the respons was ok 
    assert response.status_code==200  

    dic = (json.dumps(response.json()))

    x = json.loads(dic)

    tid = datetime.datetime.now()

    tiden = tid.strftime('%Y-%m-%d %H:%M:%S')

    verdi.append(x[11]['lastPrice'])

    tidls.append(tiden)
    
    print(f'{tiden} BTC kurs: {verdi[-1]}')

    fig = px.line(x=tidls,y=verdi)
    

    time.sleep(1)






fig.show()