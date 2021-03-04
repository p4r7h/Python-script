import requests
url = 'google.com'
x = requests.get(url, headers = {'Content-Type': 'key/please'})
print(x.text)
