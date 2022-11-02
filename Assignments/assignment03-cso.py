import requests
import json

#url= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

#def getAll():
#  response = requests.get(url)
#  return response.json()

#if __name__=="__main__":
    #print(getAll())
#   with open("cso.json", "wt") as fp:
#        print(json.dumps(getAll()), file=fp)

#Alternative way to get dataset specifically FIQO2
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("Ass03dataset.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()


if __name__=="__main__":
    # the call can be just for the dataset required here is the FP001
    getAllAsFile("FIQ02")


