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
        customer_details.write(acc_num + ',' + acc_name + ',' + str(opening_balance) + ',' + acc_type + ',' +
                               acc_email + '\n')
        customer_details.close()
        user_session = open("user_session.txt", "a")
        user_session.write(f"{username} created an account")
        user_session.close()
        print("Account created successfully")
        print("")
        page_2(username)

    elif action2 == "2":
        while True:
            account_no = str(input("Enter account number: "))
            customer_details = open("customer.txt", "r")
            user_session = open("user session.txt", "a+")
            for row in customer_details:
                list1 = row.split(",")
                acc_name = str(list1[0])
                opening_balance = str(list1[1])
                acc_type = str(list1[2])
                acc_email = str(list1[3])
                acc_num = str(list1[4])
                lastchar = len(acc_num) - 1
                acc_number = acc_num[0:lastchar]
                if str(account_no) == acc_number:
                    print(f"Account details are as follows:\n {acc_name}\n "
                          f"{opening_balance}\n {acc_type}\n {acc_email}")
                    customer_details.close()
                    user_session.write(f"{time_stamp} {username} checked account details")
                    user_session.close()
                    break

            else:
                print("Account number incorrect")
            break

    elif action2 == "3":
        os.unlink("user session.txt")
        print("You are now logged out")
        login_page()

    else:
        print("Invalid Selection")


def login_page():
    print("Please enter your details to login")

    unauthorised = True

    while unauthorised:
        username1 = str(input("Enter your username: "))
        password1 = str(input("Enter your password: "))

        login_details = open("staff.txt", "r")
        for row in login_details:
            staff_list = row.split(",")
            username = str(staff_list[0])
            password = str(staff_list[1])

            if username1 == username and password1 == password:
                print("Hello ", staff_list[3])
                user_session = open("user session.txt", "w")
                user_session.write(f"{time_stamp}: {username1} logged in")
                user_session.close()
                unauthorised = False
                print("")
                page_2(username1)

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
