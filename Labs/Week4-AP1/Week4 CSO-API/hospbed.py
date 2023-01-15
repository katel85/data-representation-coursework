import requests
import json
import urllib.parse

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/DHA70/JSON-stat/2.0/en"

parameterasDict = { 

    "Download":"false",
    "Format":"json" ,
    "label":"DHA70C02",
    "CategorySelected":"2021" ,
    "Label":"0104",
    #"Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"
}
    

def getall():
    parameters = urllib.parse.urlencode(parameterasDict)
    #print(parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    
    return response.json()


if __name__=="__main__":
    with open ("lengthofstay.json", "wt") as fp:
        print(json.dumps(getall()), file=fp) # to get this into correct format on json file use alt+shift+f