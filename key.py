import requests
url = 'https://google.com'
x = requests.get(url, params = {'key': 'please'})
print(x.text)