import requests

# Replace with your Datadog API key and application key
API_KEY = '624602f8010c4bad80af300f3df81704'
APP_KEY = '095f7939d1b7dc02654e280a97d86c96f7ae14ec'

headers = {
    'DD-API-KEY': API_KEY,
    'DD-APPLICATION-KEY': APP_KEY
}

url = 'https://api.datadoghq.com/api/v1/dashboard'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    dashboards = response.json()
    for dashboard in dashboards['dashboards']:
        print(f"Title: {dashboard['title']}, ID: {dashboard['id']}")
else:
    print(f"Failed to retrieve dashboards: {response.status_code}")

