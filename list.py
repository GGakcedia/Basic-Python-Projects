booklist = ["A Tale of Two Cities", "The Lord of the Rings", "Le Petit Prince"]

for i in booklist:
    print("Book Name: {}".format(i))

adding = input("Book Name: ")

booklist += [adding]

print(booklist)
