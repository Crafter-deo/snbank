import random
import datetime
import os

time_stamp = datetime.datetime.now()


def page_2(username):
    print("1 Create new bank account\n2 Check Account Details\n3 Logout")
    action2 = input("")
    if action2 == "1":
        print("Please fill in the following")
        acc_name = input("Enter account name: ")
        opening_balance = int(input("Enter opening balance: "))
        acc_type = input("Enter account type: ")
        acc_email = input("Enter account email: ")
        acc_num = "".join(str(random.randint(0, 9))
                          for i in range(10))
        print(acc_num)
        customer_details = open("customer.txt", "a")
        customer_details.write(acc_name, opening_balance, acc_type, acc_email, acc_num)
        user_session = open("user_session.txt", "a")
        user_session.write(f"{username} created an account")
        user_session.close()
        print("Account created successfully")
        print("")
        page_2()

    elif action2 == "2":
        input("Enter your account number: ")
        customer_details = open("customer.txt", "a+")
        customer_details.write(f"{time_stamp} {username} checked account details")

    elif action2 == "3":
        os.remove("user session.txt")
        login_page()

    else:
        print("Invalid Selection")


def login_page():
    print("Please enter your details to login")
    username1 = input("Enter your username: ")
    password1 = input("Enter your password: ")

    login_details = open("staff.txt", "r")
    found_details = False

    while not found_details:
        staff_list = login_details.read()
        new_list = staff_list.strip('\n')
        new_list2 = new_list.split(',')
        if username1 == new_list2[0] and password1 == new_list2[1]:
            found_details = True
            print("Hello ", new_list2[3])
            user_session = open("user session.txt", "w")
            user_session.write(f"{time_stamp}: {username1} logged in")
            user_session.close()
            print("")
            page_2()

        else:
            print("Incorrect details. Please try again")
            username1 = input("Enter your username: ")
            password1 = input("Enter your password: ")


menu_list = ["1 Staff Login", "2 Close App"]
for item in menu_list:
    print(item)
action1 = input("Pick an action\n")
if action1 == "1":
    login_page()

elif action1 == "2":
    exit(0)

else:
    print("Invalid selection")
