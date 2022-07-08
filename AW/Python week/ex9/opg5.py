import requests 
import json 

 


url = f'''https://api2.binance.com/api/v3/ticker/24hr'''
 
response = requests.get(url) 
 
# test if the respons was ok 
assert response.status_code==200  
 
dic = (json.dumps(response.json()))

x = json.loads(dic)

x[0]['symbol']


