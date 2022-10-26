from sympy import O
from bookapi import getallbooks

books = getallbooks()
total = 0
count = 0
for book in books:
    #print(book)
    total += book["Price"]
    count += 1 

print("Average of ",count, "book is", total/count)

