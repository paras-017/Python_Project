import requests
import json
import os
response = requests.get('https://api.github.com/users')
# print(data.content)       #it is string
data = json.loads(response.content)
print(data[0]['login'])
os.system(f'say {data[0]["login"]}')