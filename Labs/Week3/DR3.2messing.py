import requests

url = "http://www.githup.com"

response = requests.get(url)
print(response.status_code)
#print(response.headers)

