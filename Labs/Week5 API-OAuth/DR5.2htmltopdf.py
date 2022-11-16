import requests
import urllib.parse
# for added security for the api key we do not directly use the key here. This has been set up in the config.py file instead and imported in.
from config import config as cfg
# ref https://html2pdf.app/

import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"

apiKey = cfg ["htmltopdfkey"]
#api = "yourkey"
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("Wikipedia.pdf", "wb") as handler:
    handler.write(result)