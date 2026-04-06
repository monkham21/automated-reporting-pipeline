import requests

def fetch_data():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    return response.json()