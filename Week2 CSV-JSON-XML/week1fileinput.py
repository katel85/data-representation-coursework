#for files

from xml.dom.minidom import parse
filename= "employees.xml"
#read file in two ways

doc = parse(filename)

#or

with open (filename) as fp:
    doc = parse(fp)

#check it works

print (doc.toprettyxml(), end='') #output to console

