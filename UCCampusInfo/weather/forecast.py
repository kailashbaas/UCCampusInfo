import json
import requests

def get_hourly_forecast(state, city):
    request_url = "http://api.wunderground.com/api/108ec38ddacd6b6d/" \
                  + "hourly/q/" + state + "/" + city + ".json"
    response = requests.get(request_url)
    json_data = response.json() # json_data is a dict
    return json_data['hourly_forecast']
