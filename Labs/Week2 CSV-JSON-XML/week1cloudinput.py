#for content from cloud

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
#check it works

#print(doc.toprettyxml()) #output to console-this worked so I used the hashtag for the second section

# if I want to store the xml in a file. You can comment this out later
#with open("trainxml.xml","w") as xmlfp:
#    doc.writexml(xmlfp) - xml file was created and stored on file 

#Modify the program to print out each of the trainscodes. I.e. find the listings and 
#iterate through them to print each traincode out. 
#Comment out the print and modify the program so that it prints out the latitudes-this was done by replacing traincode with train latitude in line three below

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)


# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with open('traintimes.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
            traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
            traincode = traincodenode.firstChild.nodeValue.strip()
            
            
            #dataList = []
            #dataList.append(traincode)
            #train_writer.writerow(dataList)
            #print(dataList)


#At the top of the program make an array called retrieveTags that will 
#store all the names of the tags we want to retrieve.
#Then change the append line to be a for loop that iterates through these
#tag names.

            dataList = []
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())

            train_writer.writerow(dataList)


#As an exercise only store the trains whose traincode starts with a D








