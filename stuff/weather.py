from tkinter import W
import requests
import json



API_KEY = "1826e7cb367d232311c1b6520e518d55"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    with open("json_file.json", "a") as file:
            json.dump(data, file)
    print(data["weather"][0]["description"])                       
else:
    print("An error occured!")