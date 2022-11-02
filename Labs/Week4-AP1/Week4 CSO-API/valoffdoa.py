# looking how many clubhouses are in the cavan . Searched for leisure in Cavan County Council
import requests
import json
import urllib.parse

url = "https://api.valoff.ie/api/Property/GetProperties"

parameterasDict = { 

    "Download":"false",
    "Format":"json" ,
    "CategorySelected":"LEISURE" ,
    "LocalAuthority":"MEATH COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"
}
    

def getall():
    parameters = urllib.parse.urlencode(parameterasDict)
    #print(parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    
    return response.json()


if __name__=="__main__":
    with open ("valoff.json", "wt") as fp:
        print(json.dumps(getall()), file=fp) # to get this into correct format on json file use alt+shift+f



