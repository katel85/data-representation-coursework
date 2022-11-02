import requests
import json


# to get the entire url without modification for the dataset:

#url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"
#
# def getAll():
#   response = requests.get(url)
#   return reponse.json()
#
#if __name__=="__main__":
#    with open("cso.json", "wt") as fp:
#        print(json.dumps(getAll()), file=fp)

# change the url to the beginning and end and take out FP001 from the address and pass this into the gatAll function to only print out this 
#// alt+shift f to get into correct formatting in the json file 
# code :
#urlBeginning= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
#urlEnd = "/JSON-stat/2.0/en"
#def getAll(dataset):
 #   url = urlBeginning + dataset + urlEnd
 #   response = requests.get(url)
 #   return response.json()

# change again to bring in the file from the beginning 

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"

urlEnd = "/JSON-stat/2.0/en"

def getAllasFile(dataset):
    with open("csodataset2.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)
def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedasFile(dataset):
    with open("csoformatted.json", "wt") as fp:
        print(json.dumps(getAllFormatted(dataset)), file=fp)


def getAllFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {} # result into a dict object
    currentDict = result



    for dim0 in range(0, sizes[0]):
        currentId= ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label = dimensions[currentId]["category"]["label"][index]
        currentDict[label]={}
        currentDict = currentDict[label]
        #print(label)
        for dim1 in range(0, sizes[1]):
            currentId= ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label = dimensions[currentId]["category"]["label"][index]
            currentDict[label]={}
            currentDict = currentDict[label]
            #print("\t",label)
            for dim2 in range(0, sizes[2]):
                currentId= ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label = dimensions[currentId]["category"]["label"][index]
                #print("\t\t",label)
                currentDict[label]={}
                currentDict = currentDict[label]
                for dim3 in range(0, sizes[3]):
                    currentId= ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label = dimensions[currentId]["category"]["label"][index]
                    currentDict[label]=values[valuecount]
                    
                    #print("\t\t\t",label,"", values[valuecount])
                    valuecount+=1

    
    #print(result)
    return result
    #for id in ids:
    #    print(id)

if __name__=="__main__":
    # the call can be just for the dataset required here is the FP001
    #getAllasFile("FP001")
    #getAllFormatted("FP001")
    getFormattedasFile("FP001")