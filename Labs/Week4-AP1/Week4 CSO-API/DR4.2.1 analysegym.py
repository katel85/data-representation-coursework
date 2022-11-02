from valoffdoa import getall


data = getall()
totalarea = 0
for entry in data:
    #print(entry)
    valuationreports = entry["ValuationReport"]
    #print(valuationreports)
    for valuationreport in valuationreports:
        #print(valuationreport)
        if valuationreport['FloorUse'] =='GYMNASIUM':
            totalarea += valuationreport['Area']

print(totalarea)