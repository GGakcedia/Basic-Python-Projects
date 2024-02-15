from os import system as command

class Customer():
    def __init__(self, ID, PASSWORD, NAME):
        self.name = NAME
        self.password = PASSWORD
        self.id = ID
        self.balance = 0

class Bank():
    def __init__(self):
        self.customers = []

    def being_customer(self, ID, PASSWORD, NAME):
        self.customers.append(Customer(ID, PASSWORD, NAME))
        print("!! Thank you for registering with our bank !!")

def main():
    bank = Bank()
    while True:
        command("cls")
        print("""
        [1] I am a bank customer
        [2] I want to be a bank customer
        """)
        
        choose = input("Your Choose: ")

        if choose == "1":
            ids = [i.id for i in bank.customers]
            ID = input("ID: ")
            if ID in ids:
                for customer in bank.customers:
                    if ID == customer.id:
                        print("Welcome {}".format(customer.name))
                        password = input("Your Password: ")
                        if password == customer.password:
                            print("!Approved!")
                            while True:
                                command("cls")
                                print("""
                                [1] Balance İnquiry
                                [2] Deposit Money (To own account )
                                [3] Deposit Money(To someone else's account)
                                [4] Withdraw Money
                                [Q] Quit                        
                                    """)
                                choose2 = input("Your Transaction")
                                if choose2 == "1":
                                    print("Your Balance:{}".format(customer.balance))
                                    input("...Process Completed...!!__Press enter to return to the main menu__!!")
                                elif choose2 == "2":
                                    amount = int(input("Amount: "))
                                    approved = input("Do you approve the deposit of ${} into your own account? :y/n \n".format(amount))
                                    if approved =="Y" or approved == "y":
                                        customer.balance += amount
                                        print("!Your money has been deposited!")
                                        input("!!__Press enter to return to the main menu__!!")

                                    elif approved == "N" or approved == "n":
                                        print("--!Transaction canceled!--")
                                        input("!!__Press enter to return to the main menu__!!")

                                    else:
                                        print("!Entered incorrectly, transaction canceled!")
                                        input("!!__Press enter to return to the main menu__!!")    
                                elif choose2 == "3":
                                    searchID = input("Customer ID: ") 
                                    if searchID in ids:
                                        for othercustomer in bank.customers:
                                            if searchID == othercustomer.id:
                                                amount = int(input("Amount: "))
                                                if amount <= customer.balance:
                                                    approved = input("Do you approve the deposit of ${} to our customer named {}?: y/n \n".format(amount,othercustomer.name))
                                                    if approved == "y" or approved == "Y":
                                                        othercustomer.balance += amount
                                                        customer.balance -= amount 
                                                        print("====>Money transferred<====")
                                                        input("!!__Press enter to return to the main menu__!!")
                                                    elif approved == "n" or approved == "N":
                                                        print(".....Transaction canceled....")
                                                        input("!!__Press enter to return to the main menu__!!")
                                                    else:
                                                        print("!Entered incorrectly, transaction canceled!")       
                                                        input("!!__Press enter to return to the main menu__!!")
                                                else:
                                                    print("!!Your balance is insufficient!!")        
                                        else:
                                            print("!!--Customer not found--!!")
                                            input("!!__Press enter to return to the main menu__!!")        
                                elif choose2 == "4":
                                    amount = int(input("Amount: "))
                                    if amount <= customer.balance:
                                        customer.balance -= amount
                                        print("!!Transation completed.Please take your money!!")
                                        input("!!__Press enter to return to the main menu__!!")  
                                    else:
                                        print("!!Your balance is insufficient!!") 
                                        input("!!__Press enter to return to the main menu__!!")  
                                elif choose2 == "q" or choose2 == "Q":
                                    break
        elif choose == "2":
            ID = input("ID:")
            NAME = input("Your Name: ")
            PASSWORD = input("Your Password: ")
            bank.being_customer(ID,PASSWORD,NAME)                            

if __name__ ==  "__main__":
    main()
