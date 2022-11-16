import requests
import json

filename = "kate-public.json"

#url = 'https://github.com/katel85/aprivateone-'
url = 'https://api.github.com/repos/katel85/data-representation-coursework/contents'

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)