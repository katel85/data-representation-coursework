from xml.dom.minidom import parse
import os

filename = "employees.xml"

# read file in two ways
#doc = parse(filename)
# or
with open(filename) as fp:
    doc = parse(fp)

emloyeeNodeList = doc.getElementsByTagName("Employee")
print(len(emloyeeNodeList))
for employeeNode in emloyeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print (firstName)

# https://stackoverflow.com/questions/13482497/no-such-file-or-directory-root-n