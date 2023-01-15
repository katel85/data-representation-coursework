import requests
import json
import urllib.parse

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/G0322/JSON-stat/2.0/en"

parameterasDict = { 

    "Download":"false",
    "Format":"json" ,
    #"CategorySelected":"LEISURE" ,
    #"LocalAuthority":"MEATH COUNTY COUNCIL",
    #"Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"
}
    

def getall():
    parameters = urllib.parse.urlencode(parameterasDict)
    #print(parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    
    return response.json()


if __name__=="__main__":
    with open ("medical.json", "wt") as fp:
        print(json.dumps(getall()), file=fp) # to get this into correct format on json file use alt+shift+f


