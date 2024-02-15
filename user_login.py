users = { "user" : "kilicozgur",
          "password": "12345"}

names = users.keys()

user_name = input("==> Enter Username <==")
if  user_name in names :
    print("!!Welcome!! {}".format(user_name))
    password = input("Your Password: ")
    if password == users[user_name]:
        print("!!!!!!Your passwords is correct!!!!!!")
    else:
        print("!!!!!Your passwords is incorrect!!!!!")
        print("Please try again")

else:
    (".......There is no such user.......")