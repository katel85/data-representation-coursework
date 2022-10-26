import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):

    #book= {'Author': 'Kate Leddy', 'Price': 450, 'Title': 'Python Expert', 'id': 147 }
    #response = requests.post(url,json=json.dumps(book))- this doesn't work internal server error
    headers = { "Content-type": "application/json"}
    #response = requests.post(url, data = book, headers=headers)-bad request with just using book instead of json.book. Need json string
    response = requests.post(url, data = json.dumps(book), headers=headers)
    return response.json()

    

def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)     ##can change this to deleteurl instead of geturl
    response = requests.put(updateurl, json=bookdiff)  ##can change this to deleteurl instead of geturl
    return response.json()
    
    

def deleteBook(id):
    geturl = url + "/" + str(id)     ##can change this to deleteurl instead of geturl
    response = requests.delete(geturl)  ##can change this to deleteurl instead of geturl
    return response.json()
    

    

if __name__=="__main__":
    book= {'Author': 'Kate Leddy', 'Price': 450, 'Title': 'Python Expert', 'id': 147 } # moved from above for function to work.
    bookdiff= {'Price': 250 }
    #print(getBookById(123))
    print (deleteBook(162))
    #print(getallbooks())
    #print(createBook(book))
    #print(updateBook(2,bookdiff))