import requests
import json

def set_traffic_light_status(status):
    url = "http://localhost:5000/set_status"
    payload = {"status": status}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

def get_traffic_light_status():
    url = "http://localhost:5000/status"
    response = requests.get(url)
    return response.json()["status"]
