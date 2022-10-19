#for content from cloud

from regex import D
import requests
import csv

from xml.dom.minidom import parseString
url = 'http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'

page = requests.get(url)
doc = parseString(page.content)

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    
    
    traincode = traincodenode.firstChild.nodeValue.strip()
    
    
    print (traincode)

