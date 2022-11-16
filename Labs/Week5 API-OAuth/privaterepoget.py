import requests
import json
from config import config as cfg

filename = "kate-private.json"

url = 'https://api.github.com/repos/katel85/aprivateone'

#apikey = "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"
# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)
#apikey = "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"
apikey = cfg ["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)