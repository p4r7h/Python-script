import requests
url = 'http://ptl-e1cf1322-eb626166.libcurl.so/pentesterlab'
x = requests.get(url, cookies = {'key': 'please'})
print(x.text)