import requests
import json


api_url = 'http://api.open-notify.org/astros.json'
response = requests.get(api_url)

if response.status_code == 200:
    json_data = response.json()
    print(f'there are {json_data['number']} people in space right now')
    count = 1
    for person in json_data['people']:
        print(f'{count}- {person['craft']}: {person['name']}')
        count += 1


else:
    print(f'there has been an error: {response.status_code}')