import os
tables = dict()
for i in range(10):
    tables[i]= 0

def add():
    table_no = int(input("Table No: "))
    valid = tables[table_no]
    will_add = float(input("Fee to be added: "))
    total = valid + will_add
    tables[table_no] = total 

def remove():
    table_no = int(input("Table No: "))
    valid = tables[table_no]
    will_decrease = float(input("Fee to be deacrease: "))
    total = valid - will_decrease
    if total < 0:
        print("!!Transaction is incorrect!! ----Please check this----")
    else:    
        tables[table_no] = total 

def accound_check(folder_name):
    try:
        folder = open(folder_name)
        data = folder.read()
        data = data.split("\n")
        data.pop()
        folder.close()
        flag = True
    except FileNotFoundError:
        folder = open(folder_name,"w")
        folder.close()
        print("!Run for the first time! --Log file created--")
        flag = False

    if flag:
        for i in enumerate(data):
            tables[i[0]] = float(i[1])
    else:
        pass

def log_update():
     folder = open("log.txt","w")
     for i in range(10):
         valid = tables[i]
         valid = str(valid)
         folder.write(valid +"\n")
     folder.close()    

def main():
 accound_check("log.txt")
 while True:
     os.system("cls")
    
     print("""
     [1] View Tables
     [2] Add Bill
     [3] Remove Bill     
     [Q] Quit      
     """)
    
     choice = input("Your choice: ")   

     if choice == "1":
         for i in range(10):
             print("Bill for table {}: {}".format(i,tables[i]))
         print("...Process Completed...!!__Press enter to return to the main menu__!!")
         input()

     elif choice == "2":
         add()
         print("...Process Completed...!!__Press enter to return to the main menu__!!")
         input()

     elif choice == "3":
         remove()
         print("...Process Completed...!!__Press enter to return to the main menu__!!")
         input()

     elif choice == "q" or choice == "Q":
         print("!!!Exiting!!!!")
         quit()

main()         