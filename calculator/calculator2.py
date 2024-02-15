print("""

 ----------------------------
 [1] Collection   
 [2] Extraction       
 [3] Division        
 [4] Multiplication
 [5] Exponentiation
 [Q] Quit
 ----------------------------     1

      """)

entry = input("!Choose!")
if entry == "1":
    x = input("First Number: ")
    x = float(x)
    y = input("Second Number: ")
    y = float(y)

    print("==========================")
    print("Transaction Result: ", x+y)
    print("==========================")

elif entry == "2":
    x = input("First Number: ")
    x = float(x)
    y = input("Second Number: ")
    y = float(y)

    print("==========================")
    print("Transaction Result: ", x-y)
    print("==========================")

elif entry == "3":
    x = input("First Number: ")
    x = float(x)
    y = input("Second Number: ")
    y = float(y)

    print("==========================")
    print("Transaction Result: ", x/y)
    print("==========================")

elif entry == "4":
    x = input("First Number: ")
    x = float(x)
    y = input("Second Number: ")
    y = float(y)

    print("==========================")
    print("Transaction Result: ", x*y) 
    print("==========================")

elif entry == "5":
    x = input("Base: ")
    x = float(x)
    y = input("Exponent: ")
    y = int(y)

    print("==========================")
    print("Transaction Result: ", x**y)
    print("==========================")

elif entry == "q" or entry == "Q":
    print("!Exiting!")
    quit()
else:
    print("!You entered incorrectly!")
    quit()