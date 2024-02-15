import sqlite3
 
db = sqlite3.connect("books.sqlite")
cursor = db.cursor()

menu = """
[1] Search Book
[2] Search Author
"""
print(menu)

process = input("Your Process: ")
if process == "1":
    name = input("Book Name: ")
    query = "SELECT * FROM 'bookcase' WHERE book= '{}'".format(name)
    cursor.execute(query)
    databases = cursor.fetchall()
    for i in databases:
        print(i)
  

db.close()