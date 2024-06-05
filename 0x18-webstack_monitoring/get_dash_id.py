import requests

# Replace with your Datadog API key and application key
API_KEY = ''
APP_KEY = ''

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

