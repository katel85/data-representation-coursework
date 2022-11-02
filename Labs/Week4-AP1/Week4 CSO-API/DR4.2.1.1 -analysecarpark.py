from valoffdoa import getall
# how many premises are on the meath county list by listing the number of carparks

data = getall()
total = 0
count = 0
#for entry in data:
    #print(entry)
    #carparks = entry["CarPark"]
    #print(carparks)
    #total += entry["CarPark"]
    #count += 1 

#print(count)


for entry in data:
    #print(entry)
    premises = entry["PropertyNumber"]
    #print(carparks)
    total += entry["PropertyNumber"]
    count += 1 

print(count)

# both ran correctly and gave the number as 75.