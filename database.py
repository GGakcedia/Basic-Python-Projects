import sqlite3 

databases = [
("J.R.R. Tolkien", "Silmarilion"),
("Ömer Çıtak","Ethical Hacking"),
("Paulo Coelho","Simyacı"),
("Paulo Coelho","Simyacı")]

db = sqlite3.connect("books.sqlite")

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS 'bookcase table  ' (author,book)")

for data in databases:
    cursor.execute("INSERT INTO 'bookcase table' VALUES (?,?)",data)

db.commit()
db.close()