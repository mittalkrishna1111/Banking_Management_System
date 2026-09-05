import mysql.connector as c
import random
from datetime import datetime
con = c.connect(host='localhost',user='root',passwd='1234')
import time
import sys
import builtins
cursor= con.cursor()

def slow_print(*args, sep=' ', end='\n'):
    text = sep.join(map(str, args)) + end
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)

builtins.print = slow_print

def check(user_input):
    if user_input.strip().lower() == "exit":
        print("\n" + "="*50)
        print("🔒  Exiting the System".center(50))
        print("="*50)
        print("Goodbye! Have a great day ahead 😊".center(50))
        print("="*50 + "\n")
        sys.exit(0)

def Create_requirement():
    a = b = c = d = 0
    cursor.execute("CREATE DATABASE IF NOT EXISTS Global_Bank")
    cursor.execute("USE Global_Bank")
    cursor.execute("show tables")
    data = cursor.fetchall()

    for i in data:
        if i[0].lower() == "accounts":
            a = 1
        elif i[0].lower() == "complaint":
            b = 1
        elif i[0].lower() == "loan":
            c = 1
        elif i[0].lower() == "fixed_deposite":
            d = 1

    print("\n" + "="*60)
    print("🏦  DATABASE TABLE INITIALIZATION".center(60))
    print("="*60)

    if a != 1:
        cursor.execute(
            "create table Accounts(Account_Number int primary key auto_increment , "
            "User_Name varchar(50) not null , Gmail_ID varchar(50) not null , "
            "Password varchar(50) not null , Aadhar_Number bigint not null , "
            "Balance bigint not null)"
        )
        print("✅  Created table: Accounts")
    else:
        print("✔️  Table 'Accounts' already exists")

    if b != 1:
        cursor.execute(
            "create table Complaint(S_No int primary key auto_increment , "
            "Account_Number int not null , Complaint varchar(200) not null)"
        )
        print("✅  Created table: Complaint")
    else:
        print("✔️  Table 'Complaint' already exists")

    if c != 1:
        cursor.execute(
            "create table Loan(Loan_ID int primary key auto_increment , "
            "Account_Number int not null , Loan_Amount int not null , "
            "collateral varchar(50) not null , Date_and_time_of_loan varchar(50) not null , "
            "Duration_of_Loan varchar(50) not null , Last_date_of_repayment_of_loan varchar(50) not null , "
            "Repayable_Amount bigint not null , Repaid_the_loan varchar(50) not null default 'No')"
        )
        print("✅  Created table: Loan")
    else:
        print("✔️  Table 'Loan' already exists")

    if d != 1:
        cursor.execute(
            "create table Fixed_Deposite(FD_ID int primary key auto_increment , "
            "Account_Number int not null , Fixed_Deposite bigint not null , "
            "FD_Maturity_Date varchar(50) not null , Final_Amount int not null)"
        )
        print("✅  Created table: Fixed_Deposite")
    else:
        print("✔️  Table 'Fixed_Deposite' already exists")

    con.commit()

    print("="*60)
    print("🎯  Database setup completed successfully!".center(60))
    print("="*60 + "\n")

def Login():
    print("\n" + "="*60)
    print("🔐  LOGIN PORTAL".center(60))
    print("="*60)
    print("You want to login as :")
    print("  1️⃣  --> Admin")
    print("  2️⃣  --> User")
    print("="*60)
    login=""
    while True:
        choice = input("👉  Enter your choice (1-2): ")
        check(choice)
        choice = int(choice)
        if choice == 1 or choice == 2:
            break
        else:
            print("⚠️  Please enter a valid choice (1 or 2)")
    while(choice == 1):
        passwd = input("\n🔑  Enter the Admin password: ")
        check(passwd)
        if passwd == password:
            print("\n" + "="*60)
            print("✅  Login Successful as ADMIN".center(60))
            print("="*60)
            login = "admin"
            break
        else:
            print("❌  Incorrect password. Please try again.")
            continue
    
    while(choice == 2):
        global acc_no
        acc_no = input("\n💳  Enter your Account Number: ")
        check(acc_no)
        acc_no = int(acc_no)
        query = "select * from Accounts where Account_Number = {}".format(acc_no)
        cursor.execute(query)
        var = cursor.fetchall()
        if cursor.rowcount == 1:
            login = "user"
            print("\n" + "="*60)
            print("✅  Login Successful as USER".center(60))
            print("="*60)
            break
        else:
            print("❌  Account number not found. Please try again.")
            continue

    con.commit()
    return login

def Create_Account():
    print("\n" + "="*60)
    print("🧾  WELCOME TO CREATE ACCOUNT PORTAL".center(60))
    print("="*60 + "\n")


    while True:
        
        user_name = input("👤  Enter your Name: ")
        check(user_name)
    
        while True:
            print("="*60)
            print("📧  Gmail Guidelines:".center(60))
            print("="*60)
            print("• Must have at least 8 characters with at least 1 digit")
            print("• All characters must be lowercase")
            print("• Must end with '@gmail.com'")
            print("• Cannot contain special characters\n")

            Gmail = input("✉️  Enter your Gmail ID: ")
            check(Gmail)
            print()

            Gmail1 = Gmail.split("@")
            if Gmail.endswith("@gmail.com") and len(Gmail1[0]) >= 8 and Gmail.islower():
                digit = alpha = special = 0
                for i in Gmail1[0]:
                    if i.isalpha():
                        alpha += 1
                    elif i.isdigit():
                        digit += 1
                    else:
                        special += 1
                if special == 0 and digit >= 1 and alpha >= 1:
                    break
                else:
                    print("❌  Invalid Gmail ID. Please follow the above instructions.\n")
                    continue
            else:
                print("❌  Invalid Gmail ID. Please follow the above instructions.\n")
                continue

        while True:
            print("="*60)
            print("🔑  Password Guidelines:".center(60))
            print("="*60)
            print("• Must have at least 8 characters")
            print("• Must include at least one alphabet")
            print("• Cannot contain special characters\n")

            password = input("🔒  Enter your Password: ")
            check(password)
            print()
            if len(password) >= 8:
                alnum = special = 0
                for i in Gmail1[0]:
                    if i.isalnum():
                        alnum += 1
                    else:
                        special += 1
                if special == 0 and alnum >= 1:
                    break
                else:
                    print("❌  Invalid Password. Please follow the above instructions.\n")
                    continue
            else:
                print("❌  Invalid Password. Please follow the above instructions.\n")
                continue

        while True:
            print("="*60)
            print("🆔  Aadhar Number Guidelines:".center(60))
            print("="*60)
            print("• Must contain exactly 12 digits")
            print("• Should not contain spaces or special characters\n")

            try:
                aadhar_number = input("📄  Enter your Aadhar Number: ")
                check(aadhar_number)
                aadhar_number = int(aadhar_number)
            except:
                print("⚠️  Invalid Aadhar number. Please enter only digits.\n")
                continue

            if len(str(aadhar_number)) == 12:
                break
            else:
                print("❌  Invalid Aadhar number. Please follow the above instructions.\n")
                continue

        while True:
            try:
                balance = input("💰  Enter Initial Deposit Amount: ")
                check(balance)
                balance = int(balance)
            except:
                print("⚠️  Invalid amount. Please enter only digits.\n")
                continue

            if balance >= 500:
                break
            else:
                print("⚠️  Minimum deposit required: ₹500\n")

        cursor.execute("select * from accounts")
        cursor.fetchall()
        if cursor.rowcount > 0:
            cursor.execute("select Account_Number from accounts order by Account_Number desc limit 1")
            data = cursor.fetchall()
            acc_no = data[0][0] + 1
        else:
            acc_no = 10001

        acc_no1 = str(acc_no)
        query = "insert into Accounts(Account_Number,User_name,Gmail_ID,Password,Aadhar_Number,Balance) values({},'{}','{}','{}',{},{})".format(acc_no, user_name, Gmail, password, aadhar_number, balance)
        cursor.execute(query)

        print("\n" + "="*60)
        print("🎉  Account Created Successfully!".center(60))
        print("="*60)
        print(f"💳  Your New Account Number: {acc_no}".center(60))
        print("="*60 + "\n")

        query1 = "create table A{}(S_No int primary key auto_increment, Amount bigint not null, Transaction_type varchar(50) not null)".format(acc_no1)
        cursor.execute(query1)

        print("Would you like to create another account?")
        choi = input("👉  Press 'y' for Yes or Enter to exit: ")
        if choi.lower() == "y":
            print()
            continue
        else:
            break

    con.commit()

def Deactivate_Account():
    print("\n" + "="*60)
    print("🛑  WELCOME TO DEACTIVATION PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        num = 0
        while True:
            acc_no = input("💳  Enter the Account Number: ")
            check(acc_no)
            acc_no = int(acc_no)
            query = "select * from Accounts where Account_Number = {}".format(acc_no)
            cursor.execute(query)
            cursor.fetchall()
            if cursor.rowcount == 1:
                print()
                break
            else:
                print("⚠️  Enter an existing account number.\n")

        cursor.execute("select * from loan where Account_Number = {} and Repaid_the_loan = 'No'".format(acc_no))
        num = cursor.fetchall()

        if len(num) == 0:
            query = "delete from Accounts where Account_number={}".format(acc_no)
            cursor.execute(query)
            query = "DROP TABLE A{}".format(acc_no)
            cursor.execute(query)
            print("\n" + "="*60)
            print("✅  ACCOUNT DEACTIVATION SUCCESSFUL".center(60))
            print("="*60 + "\n")
        else:
            print("⚠️  Please clear pending loans before deactivating the account.\n")

        print("Do you want to deactivate another account?")
        choi = input("👉  Press 'y' for Yes or Enter to exit: ")
        if choi.lower() == "y":
            print()
            continue
        else:
            break

    con.commit()
    print("\n" + "="*60)
    print("🎯  Deactivation Process Completed".center(60))
    print("="*60 + "\n")

def Deposite_Money(acc_no):
    print("\n" + "="*60)
    print("💵  WELCOME TO DEPOSIT MONEY PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        while True:
            try:
                balance = input("💰  Enter the amount to deposit: ")
                check(balance)
                balance = int(balance)
                break
            except:
                print("⚠️  Invalid amount. Please enter digits only.\n")

        query1 = "select Balance from Accounts where Account_Number = {}".format(acc_no)
        cursor.execute(query1)
        data = cursor.fetchone()
        new_balance = data[0] + balance

        query2 = "update Accounts set Balance={} where Account_Number = {}".format(new_balance, acc_no)
        cursor.execute(query2)

        # Success message
        print("\n" + "="*60)
        print("✅  MONEY DEPOSITED SUCCESSFULLY".center(60))
        print("="*60 + "\n")

        # Ask if user wants to deposit more
        print("Do you want to deposit more money into your account?")
        choi = input("👉  Press 'y' for Yes or Enter to exit: ")
        if choi.lower() == "y":
            print()
            continue
        else:
            break

    con.commit()

def Withdraw_Money(acc_no):

    print("="*65)
    print("\t\tWELCOME TO WITHDRAW MONEY PORTAL")
    print("="*65)
    print()

    while True:
        while True:
            while True :
                try:
                    balance = input("Enter the amount to be withdraw : ")
                    check(balance)
                    balance = int(balance)
                    break
                except:
                    print("invaild amount. Enter only digits")
            
            query1 = 'select Balance from Accounts where Account_Number = {}'.format(acc_no)
            cursor.execute(query1)
            data = cursor.fetchone()
            new_balance = data[0] - balance
            if new_balance < 0 :
                print("your account does not have that much amount of money")
                print(f"your account have only {data[0]}")
            else:
                break
        
        query2 = "update Accounts set Balance={} where Account_Number = {}".format(new_balance,acc_no)
        cursor.execute(query2)

        print("="*65)
        print("\t\tMONEY WITHDRAWAL SUCCESSFULLY")
        print("="*65)
    
        print("Do you want to withdraw more money from your account ?\nIF yes press y otherwise press enter")
        choi = input("enter your choice : ")
        if choi.lower() == "y" :
            continue
        else:
            break

    con.commit()

def Display_Account_Details(acc_no):
    print("\n" + "="*60)
    print("🧾  WELCOME TO DISPLAY ACCOUNT PORTAL".center(60))
    print("="*60 + "\n")

    query = "select * from Accounts where Account_Number = {}".format(acc_no)
    cursor.execute(query)
    data = cursor.fetchone()

    print("📋  ACCOUNT DETAILS".center(60))
    print("="*60)
    print(f"{'Account Number :':<25} {data[0]}")
    print(f"{'User Name :':<25} {data[1]}")
    print(f"{'Gmail ID :':<25} {data[2]}")
    print(f"{'Password :':<25} {data[3]}")
    print(f"{'Aadhar Number :':<25} {data[4]}")
    print(f"{'Balance :':<25} ₹{data[5]}")
    print("="*60)

    con.commit()

    print("\n" + "="*60)
    print("✅  ACCOUNT DETAILS DISPLAYED SUCCESSFULLY".center(60))
    print("="*60 + "\n")

def Display_Accounts():
    print("\n" + "="*60)
    print("📚  WELCOME TO DISPLAY ACCOUNTS PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        print("Select an option:".center(60))
        print("="*60)
        print("1️⃣  Display specific account")
        print("2️⃣  Display first n number of accounts")
        print("3️⃣  Display all accounts")
        print("4️⃣  Exit")
        print("="*60)

        while True:
            choice = input("Enter your choice (1-4): ")
            check(choice)
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("⚠️  Please enter a valid choice (1–4).")

        if choice == 1:
            while True:
                acc_no = input("\nEnter the account number: ")
                check(acc_no)
                acc_no = int(acc_no)
                query = "select * from Accounts where Account_Number = {}".format(acc_no)
                cursor.execute(query)
                cursor.fetchall()
                if cursor.rowcount == 1:
                    print()
                    break
                else:
                    print("⚠️  Account number not found. Please try again.")

            query = "select * from Accounts where Account_Number = {}".format(acc_no)
            cursor.execute(query)
            data = cursor.fetchone()

            print("\n" + "="*60)
            print("📋  ACCOUNT DETAILS".center(60))
            print("="*60)
            print(f"{'Account Number :':<25} {data[0]}")
            print(f"{'User Name :':<25} {data[1]}")
            print(f"{'Gmail ID :':<25} {data[2]}")
            print(f"{'Password :':<25} {data[3]}")
            print(f"{'Aadhar Number :':<25} {data[4]}")
            print(f"{'Balance :':<25} ₹{data[5]}") 
            print("="*60)

        elif choice == 2:
            try:
                num = input("\nEnter how many accounts to display: ")
                check(num)
                num = int(num)
            except:
                print("⚠️  Invalid input. Please enter digits only.")
                continue

            query = "select * from Accounts"
            cursor.execute(query)
            data = cursor.fetchmany(num)

            print("\n" + "📋  ACCOUNT DETAILS".center(60))
            print("="*60)
            n = 1
            for i in data:
                print(f"\n{'Account - ' + str(n):^60}")
                print("="*60)
                print(f"{'Account Number :':<25} {i[0]}")
                print(f"{'User Name :':<25} {i[1]}")
                print(f"{'Gmail ID :':<25} {i[2]}")
                print(f"{'Password :':<25} {i[3]}")
                print(f"{'Aadhar Number :':<25} {i[4]}")
                print(f"{'Balance :':<25} ₹{i[5]}")
                print("="*60)
                n += 1

        elif choice == 3:
            query = "select * from Accounts"
            cursor.execute(query)
            data = cursor.fetchall()

            print("\n" + "📋  ALL ACCOUNT DETAILS".center(60))
            print("="*60)
            n = 1
            for i in data:
                print(f"\n{'Account - ' + str(n):^60}")
                print("="*60)
                print(f"{'Account Number :':<25} {i[0]}")
                print(f"{'User Name :':<25} {i[1]}")
                print(f"{'Gmail ID :':<25} {i[2]}")
                print(f"{'Password :':<25} {i[3]}")
                print(f"{'Aadhar Number :':<25} {i[4]}")
                print(f"{'Balance :':<25} ₹{i[5]}")
                print("="*60)
                n += 1

        else:
            print("\nDo you want to perform another display operation?")
            choi = input("Press 'y' for yes or Enter to exit: ")
            check(choi)
            if choi.lower() == "y":
                continue
            else:
                break

    con.commit()


def Update_Details():
    print("\n" + "="*60)
    print("🛠️  WELCOME TO UPDATE DETAILS PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        while True:
            acc_no = input("Enter the account number to be updated: ")
            check(acc_no)
            acc_no = int(acc_no)
            query = "select * from Accounts where Account_Number = {}".format(acc_no)
            cursor.execute(query)
            cursor.fetchall()
            if cursor.rowcount == 1:
                print()
                break
            else:
                print("⚠️  Account not found. Please enter an existing account number.\n")

        while True:
            print("Select what you want to update:".center(60))
            print("="*60)
            print("1️⃣  Update User Name")
            print("2️⃣  Update Gmail")
            print("3️⃣  Update Password")
            print("4️⃣  Exit")
            print("="*60)

            while True:
                choice = input("Enter your choice (1-4): ")
                check(choice)
                choice = int(choice)
                if choice in [1, 2, 3, 4]:
                    break
                else:
                    print("⚠️  Invalid choice. Please enter a number between 1–4.\n")

            if choice == 1:
                new = input("\nEnter your new User Name: ")
                check(new)
                query = 'update Accounts set User_Name="{}" where Account_Number={}'.format(new, acc_no)
                cursor.execute(query)
                print("\n" + "="*60)
                print("✅  USER NAME UPDATED SUCCESSFULLY".center(60))
                print("="*60 + "\n")

            elif choice == 2:
                while True:
                    print("\n📧  Gmail Guidelines:")
                    print("- Must have at least 8 characters with 1 digit.")
                    print("- All characters should be lowercase.")
                    print("- Must end with '@gmail.com'.")
                    print("- No special characters allowed.\n")

                    Gmail = input("Enter your new Gmail ID: ")
                    check(Gmail)
                    Gmail1 = Gmail.split("@")

                    if Gmail.endswith("@gmail.com") and len(Gmail1[0]) >= 8 and Gmail.islower():
                        digit = alpha = special = 0
                        for i in Gmail1[0]:
                            if i.isalpha():
                                alpha += 1
                            elif i.isdigit():
                                digit += 1
                            else:
                                special += 1
                        if special == 0 and digit >= 1 and alpha >= 1:
                            break
                        else:
                            print("⚠️  Invalid Gmail ID. Please follow the instructions.\n")
                    else:
                        print("⚠️  Invalid Gmail ID. Please follow the instructions.\n")

                query = 'update Accounts set Gmail_ID="{}" where Account_Number={}'.format(Gmail, acc_no)
                cursor.execute(query)
                print("\n" + "="*60)
                print("✅  GMAIL UPDATED SUCCESSFULLY".center(60))
                print("="*60 + "\n")

            elif choice == 3:
                while True:
                    print("\n🔐  Password Guidelines:")
                    print("- Must have at least 8 characters with 1 alphabet.")
                    print("- No special characters allowed.\n")

                    password = input("Enter your new Password: ")
                    check(password)

                    if len(password) >= 8:
                        alnum = special = 0
                        for i in password:
                            if i.isalnum():
                                alnum += 1
                            else:
                                special += 1
                        if special == 0 and alnum >= 1:
                            break
                        else:
                            print("⚠️  Invalid Password. Please follow the instructions.\n")
                    else:
                        print("⚠️  Invalid Password. Must be at least 8 characters.\n")

                query = 'update Accounts set Password="{}" where Account_Number={}'.format(password, acc_no)
                cursor.execute(query)
                print("\n" + "="*60)
                print("✅  PASSWORD UPDATED SUCCESSFULLY".center(60))
                print("="*60 + "\n")

            else:
                print("\nWould you like to perform another update?")
                choi = input("Press 'y' for yes or Enter to exit: ")
                check(choi)
                if choi.lower() == "y":
                    continue
                else:
                    break

        con.commit()
        print("\n💾  Changes saved successfully!\n")

        next_action = input("📋  Update another account? (y/n): ")
        if next_action.lower() != "y":
            break
    
def Transfer_Money(acc_no):
    
    print("💸" + "=" * 60)
    print("🏦\t\tWELCOME TO TRANSFER MONEY PORTAL")
    print("💸" + "=" * 60)
    print()

    while True:
        acc_no1 = acc_no

        # 🔍 Step 1: Receiver Account Validation
        while True:
            acc_no2 = input("🔢 Enter the account number to which you want to deposit money: ")
            check(acc_no2)
            acc_no2 = int(acc_no2)

            query = "select * from Accounts where Account_Number = {}".format(acc_no2)
            cursor.execute(query)
            cursor.fetchall()

            if cursor.rowcount == 1:
                if acc_no1 != acc_no2:
                    print("✅ Account verified successfully!")
                    print()
                    break
                else:
                    print("⚠️ You cannot transfer to your own account. Please enter a different number.")
                    continue
            else:
                print("❌ Invalid account number. Please enter an existing one.")
                continue

        # 💰 Step 2: Perform Transfer Operation
        while True:
            while True:
                try:
                    balance = input("💵 Enter the amount to be withdrawn: ")
                    check(balance)
                    balance = int(balance)
                    break
                except:
                    print("🚫 Invalid input! Please enter digits only.")

            query1 = "select Balance from Accounts where Account_Number = {}".format(acc_no1)
            cursor.execute(query1)
            data = cursor.fetchone()
            new_balance = data[0] - balance

            # ⚠️ Step 3: Check for sufficient balance
            if new_balance < 0:
                print("💣 Insufficient balance!")
                print(f"💰 Your current balance is: ₹{data[0]}")
                print()
                print("🔁 Do you want to try again with a lower amount? (y/n)")
                choice = input("👉 Enter your choice: ")
                check(choice)
                if choice.lower() == "y":
                    continue
                else:
                    break

            else:
                # 💳 Step 4: Deduct from Sender
                query2 = "update Accounts set Balance = {} where Account_Number = {}".format(new_balance, acc_no1)
                cursor.execute(query2)

                acc_no3 = str(acc_no1)
                amount = balance
                Transaction_type = "withdraw"

                cursor.execute("select * from A{}".format(acc_no3))
                cursor.fetchall()
                S_No = 1 + cursor.rowcount

                query3 = "insert into A{} (S_No, Amount, Transaction_type) values ({}, {}, '{}')".format(
                    acc_no3, S_No, amount, Transaction_type
                )
                cursor.execute(query3)

                # 💰 Step 5: Add to Receiver
                query4 = "select Balance from Accounts where Account_Number = {}".format(acc_no2)
                cursor.execute(query4)
                data = cursor.fetchone()
                new_balance = data[0] + balance

                query5 = "update Accounts set Balance = {} where Account_Number = {}".format(new_balance, acc_no2)
                cursor.execute(query5)

                acc_no4 = str(acc_no2)
                amount = balance
                Transaction_type = "deposit"

                cursor.execute("select * from A{}".format(acc_no4))
                cursor.fetchall()
                S_No = 1 + cursor.rowcount

                query6 = "insert into A{} (S_No, Amount, Transaction_type) values ({}, {}, '{}')".format(
                    acc_no4, S_No, amount, Transaction_type
                )
                cursor.execute(query6)

                print("✅" + "=" * 60)
                print("🎉\t\tMONEY TRANSFERRED SUCCESSFULLY!")
                print("✅" + "=" * 60)
                break

        # 🔁 Step 6: Ask for another transaction
        print("🔄 Do you want to perform another transaction?")
        print("If yes, press 'y' 🟢  otherwise press Enter ⏎ to exit.")
        choi = input("👉 Enter your choice: ")

        if choi.lower() == "y":
            continue
        else:
            break

    con.commit()

def Total_Balance_In_bank():

    print("\n" + "="*60)
    print("🏦  WELCOME TO TOTAL BALANCE PORTAL".center(60))
    print("="*60 + "\n")

    total_balance = 0
    query = "select balance from Accounts"
    cursor.execute(query)
    data = cursor.fetchall()

    for i in data:
        total_balance += i[0]

    print("\n" + "="*60)
    print(f"💰  The Total Bank Balance is: ₹{total_balance}".center(60))
    print("="*60 + "\n")

    con.commit()

def Check_Account_Balance(acc_no):

    print("\n" + "="*60)
    print("🏦  WELCOME TO CHECK ACCOUNT BALANCE PORTAL".center(60))
    print("="*60 + "\n")

    query = "select balance from Accounts where Account_Number = {}".format(acc_no)
    cursor.execute(query)
    data = cursor.fetchall()

    print("\n" + "="*60)
    print(f"💰  Your account balance is: ₹{data[0][0]}".center(60))
    print("="*60 + "\n")

    con.commit()

def Transaction_History(acc_no):
    print("\n" + "="*60)
    print("📜  WELCOME TO TRANSACTION HISTORY PORTAL".center(60))
    print("="*60 + "\n")

    query = "select * from A{}".format(acc_no)
    cursor.execute(query)
    data = cursor.fetchall()

    if not data:
        print("\n" + "="*60)
        print("ℹ️  No transactions found for this account.".center(60))
        print("="*60 + "\n")
    else:
        n = 1
        print("\n" + "="*60)
        print("📄  Account Transaction Details".center(60))
        print("="*60 + "\n")

        for i in data:
            print("\n" + "="*50)
            print(f"🔹 Transaction - {n}".center(50))
            print("="*50 + "\n")
            print(f"🆔  S.No           --> {i[0]}")
            print(f"💵  Amount         --> ₹{i[1]}")
            print(f"🔁  Transaction Type --> {i[2]}")
            n += 1
            print("="*50 + "\n")

    con.commit()

def Raise_A_Complaint(acc_no):

    print("\n" + "="*60)
    print("📝  WELCOME TO COMPLAINT PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        complaint = input("✏️  Enter your Complaint: ")
        check(complaint)

        cursor.execute("select * from Complaint")
        cursor.fetchall()
        S_No = 1 + cursor.rowcount

        query = "insert into Complaint(S_No, Account_Number, Complaint) values ({}, {}, '{}')".format(S_No, acc_no, complaint)
        cursor.execute(query)

        print("\n" + "="*60)
        print("✅  COMPLAINT RECORDED SUCCESSFULLY".center(60))
        print("="*60 + "\n")

        print("🔁 Do you want to raise another complaint?")
        print("If yes, press 'y' 🟢  otherwise press Enter ⏎ to exit.")
        choi = input("👉 Enter your choice: ")
        if choi.lower() == "y":
            continue
        else:
            break

    con.commit()

def Check_The_Complaint():
    print("\n" + "="*60)
    print("📋  WELCOME TO CHECK THE COMPLAINT PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        print("1️⃣  Check complaint of a specific account")
        print("2️⃣  Check all complaints")
        print("3️⃣  Exit")
        print()

        while True:
            choice = input("👉 Enter your choice (1-3): ")
            check(choice)
            choice = int(choice)
            if choice in [1, 2, 3]:
                break
            else:
                print("⚠️  Enter a valid choice")

        if choice == 1:
            n = 1
            while True:
                acc_no = input("✏️  Enter the account number: ")
                check(acc_no)
                acc_no = int(acc_no)
                query = "select * from Accounts where Account_Number = {}".format(acc_no)
                cursor.execute(query)
                cursor.fetchall()
                if cursor.rowcount == 1:
                    print()
                    break
                else:
                    print("⚠️  Enter an existing account number")
            query = 'select * from Complaint where Account_Number = {}'.format(acc_no)
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                print("\n" + "="*60)
                print("ℹ️  No complaints found for this account.".center(60))
                print("="*60 + "\n")
            else:
                print("\n" + "="*60)
                print("📄  Complaint Details".center(60))
                print("="*60 + "\n")
                for i in data:
                    print("="*50)
                    print(f"🎯 Complaint - {n}".center(50))
                    print("="*50 + "\n")
                    print(f"🆔  S.No           --> {i[0]}")
                    print(f"💳  Account Number --> {i[1]}")
                    print(f"📝  Complaint      --> {i[2]}")
                    n += 1
                    print("="*50 + "\n")

        elif choice == 2:
            query = 'select * from Complaint'
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                print("\n" + "="*60)
                print("ℹ️  No complaints found in the system.".center(60))
                print("="*60 + "\n")
            else:
                n = 1
                print("\n" + "="*60)
                print("📄  All Complaint Details".center(60))
                print("="*60 + "\n")
                for i in data:
                    print("="*50)
                    print(f"🎯 Complaint - {n}".center(50))
                    print("="*50 + "\n")
                    print(f"🆔  S.No           --> {i[0]}")
                    print(f"💳  Account Number --> {i[1]}")
                    print(f"📝  Complaint      --> {i[2]}")
                    n += 1
                    print("="*50 + "\n")

        else:
            print("🔁 Do you want to do anything else?")
            print("If yes, press 'y' 🟢 otherwise press Enter ⏎ to exit.")
            choi = input("👉 Enter your choice: ")
            check(choi)
            if choi.lower() == "y":
                continue
            else:
                break

    con.commit()

def Loan():

    print("\n" + "="*60)
    print("🏦  WELCOME TO LOAN PORTAL".center(60))
    print("="*60 + "\n")

    while True:
        while True:
            acc_no = input("✏️  Enter the account number: ")
            check(acc_no)
            acc_no = int(acc_no)
            query = "select * from Accounts where Account_Number = {}".format(acc_no)
            cursor.execute(query)
            cursor.fetchall()
            if cursor.rowcount == 1:
                print()
                break
            else:
                print("⚠️  Enter an existing account number")

        query = "select Repaid_the_loan from loan where Account_Number = {}".format(acc_no)
        cursor.execute(query)
        data = cursor.fetchall()
        count = 0
        for i in data:
            if i[0].lower() == "no":
                count += 1

        if count < 3:
            while True:
                print("💰  You can take a loan up to 10 lakhs")
                try:
                    loan_amount = input("✏️  Enter the loan amount: ")
                    check(loan_amount)
                    loan_amount = int(loan_amount)
                    if loan_amount <= 1000000:
                        print()
                        break
                    else:
                        print("⚠️  Enter loan amount within the limit")
                except:
                    print("⚠️  Please enter only digits")

            collateral = input("🏷️  Enter details of collateral: ")
            check(collateral)
            print()

            try:
                duration = input("📅  Enter duration in years: ")
                check(duration)
                duration = int(duration)
            except:
                print("⚠️  Please enter integer values for years")
            duration1 = str(duration) + " YEAR"

            cursor.execute("select * from loan")
            cursor.fetchall()
            if cursor.rowcount > 0:
                cursor.execute("SELECT Loan_ID FROM loan ORDER BY Loan_ID DESC LIMIT 1")
                data = cursor.fetchall()
                loan_id = data[0][0] + 1
            else:
                loan_id = 101

            print("💹  The bank charges 15% interest, compounded annually.")
            choice = input("✅  Confirm loan processing (yes/no): ")
            check(choice)

            if choice.lower() == "yes":
                principal = loan_amount
                annual_rate = 15
                time_years = duration

                r_m = annual_rate / (12 * 100)
                n = time_years * 12

                EMI = principal * (r_m * (1 + r_m)**n) / ((1 + r_m)**n - 1)
                amount = EMI * n

                print(f"Monthly EMI: {EMI:.2f}")
                print(f"Total repayment: {amount:.2f}")

                query1 = "INSERT INTO loan (Loan_ID,Account_Number,Loan_Amount,Collateral,Date_and_time_of_loan,Duration_of_Loan,last_date_of_repayment_of_loan,Repayable_Amount) VALUES ({},{},{},'{}','{}','{}',DATE_ADD(CURDATE(), INTERVAL {} YEAR),{})".format(loan_id, acc_no, loan_amount, collateral, datetime.now(), duration1, duration, amount)
                cursor.execute(query1)

                query2 = 'SELECT Balance FROM Accounts WHERE Account_Number = {}'.format(acc_no)
                cursor.execute(query2)
                data = cursor.fetchone()
                new_balance = data[0] + loan_amount

                query3 = "UPDATE Accounts SET Balance={} WHERE Account_Number={}".format(new_balance, acc_no)
                cursor.execute(query3)
                con.commit()

                print("\n" + "="*60)
                print(f"🆔  Your Loan ID is {loan_id}".center(60))
                print("="*60 + "\n")

        else:
            print(f"⚠️  You currently have {cursor.rowcount} pending loan(s). Clear them first to take a new loan.")

        print("\n" + "="*60)
        print("🏦  LOAN PROCESS COMPLETED SUCCESSFULLY".center(60))
        print("="*60 + "\n")

        choi = input("🔁  Do you want to take another loan? (y/Enter): ")
        check(choi)
        if choi.lower() == "y":
            continue
        else:
            break

    con.commit()

def Repayment_Of_Current_Loan(acc_no):

    print("\n" + "="*70)
    print("💳  WELCOME TO LOAN REPAYMENT PORTAL".center(70))
    print("="*70 + "\n")

    while True:
        query = "SELECT * FROM loan WHERE Account_Number = {} AND Repaid_the_loan = 'No'".format(acc_no)
        cursor.execute(query)
        data = cursor.fetchall()
        num = cursor.rowcount
        print(f"📊  You have {num} pending loan(s)")

        if num == 1:
            print("\n📄  Loan details are given below\n")
            print(f"{'Loan ID :':<35} {data[0][0]}")
            print(f"{'Account Number :':<35} {data[0][1]}")
            print(f"{'Loan Amount :':<35} {data[0][2]}")
            print(f"{'Collateral :':<35} {data[0][3]}")
            print(f"{'Date and time of loan :':<35} {data[0][4]}")
            print(f"{'Duration of loan :':<35} {data[0][5]}")
            print(f"{'Last date of repayment of loan :':<35} {data[0][6]}")
            print(f"{'Repayable amount :':<35} {data[0][7]}")
            print()

        elif num > 1:
            print("\n📄  Loan details are given below\n")
            for n, i in enumerate(data, start=1):
                print(f"Loan - {n}\n")
                print(f"{'Loan ID :':<35} {i[0]}")
                print(f"{'Account Number :':<35} {i[1]}")
                print(f"{'Loan Amount :':<35} {i[2]}")
                print(f"{'Collateral :':<35} {i[3]}")
                print(f"{'Date and time of loan :':<35} {i[4]}")
                print(f"{'Duration of loan :':<35} {i[5]}")
                print(f"{'Last date of repayment of loan :':<35} {i[6]}")
                print(f"{'Repayable amount :':<35} {i[7]}")
                print()

        else:
            break

        choice = input("💰  Do you want to pay any loan listed above? (y/n): ")
        check(choice)
        if choice.lower() == "y":
            while True:
                id = input("✏️  Enter the Loan ID to clear: ")
                check(id)
                id = int(id)
                query = "SELECT * FROM loan WHERE Loan_ID = {} AND Repaid_the_loan = 'No'".format(id)
                cursor.execute(query)
                cursor.fetchall()
                if cursor.rowcount == 1:
                    print()
                    break
                else:
                    print("⚠️  Enter an existing Loan ID")

            cursor.execute("SELECT Repayable_Amount FROM loan WHERE Loan_ID = {}".format(id))
            repayable_amount = cursor.fetchall()

            while True:
                amount = input("💵  Enter the repayable amount: ")
                check(amount)
                amount = int(amount)
                if amount == repayable_amount[0][0]:
                    query1 = 'SELECT Balance FROM Accounts WHERE Account_Number = {}'.format(acc_no)
                    cursor.execute(query1)
                    data1 = cursor.fetchone()
                    new_balance = data1[0] - amount
                    if new_balance < 0:
                        print(f"⚠️  Your account balance is insufficient. Available balance: {data1[0]}")
                    else:
                        query2 = "UPDATE Accounts SET Balance={} WHERE Account_Number={}".format(new_balance, acc_no)
                        cursor.execute(query2)

                        query3 = "UPDATE loan SET Repaid_the_loan='yes' WHERE Loan_ID={}".format(id)
                        cursor.execute(query3)

                        print("\n" + "="*55)
                        print("✅  LOAN REPAYED SUCCESSFULLY".center(55))
                        print("="*55 + "\n")
                        break

        choi = input("🔁  Do you want to pay another loan? (y/Enter): ")
        check(choi)
        if choi.lower() != "y":
            break

    con.commit()

def Fixed_Deposite():
    
    print("\n" + "="*65)
    print("🏦  WELCOME TO FIXED DEPOSIT PORTAL".center(65))
    print("="*65 + "\n")

    while True:
        while True: 
            acc_no = input("🆔  Enter the Bank account number: ")
            check(acc_no)
            acc_no = int(acc_no)
            query = "SELECT * FROM Accounts WHERE Account_Number = {}".format(acc_no)
            cursor.execute(query)
            cursor.fetchall()
            if cursor.rowcount == 1:
                break
            else:
                print("⚠️  Please enter an existing Bank account number")

        while True:
            fixed_deposite = input("💰  Enter initial fixed deposit amount: ")
            check(fixed_deposite)
            fixed_deposite = int(fixed_deposite)
            if fixed_deposite >= 500:
                break
            else:
                print("⚠️  Deposit minimum amount of 500 Rs")

        try:
            fd_maturity_date = input("📆  Enter for how many years you want the FD: ")
            check(fd_maturity_date)
            fd_maturity_date = int(fd_maturity_date)
        except:
            print("⚠️  Please enter only integer values for years")
        fd_maturity_date1 = str(fd_maturity_date) + " YEAR"

        cursor.execute("SELECT * FROM Fixed_Deposite")
        cursor.fetchall()
        if cursor.rowcount > 0:
            cursor.execute("SELECT FD_ID FROM Fixed_Deposite ORDER BY FD_ID DESC LIMIT 1")
            data = cursor.fetchall()
            fd_id = data[0][0] + 1
        else:
            fd_id = 101

        print("💹  The bank will apply 5% interest compounded annually")
        choice = input("✅  Please confirm creation of FD by typing yes/no: ")
        check(choice)

        if choice.lower() == "yes":
            principle = fixed_deposite
            time = fd_maturity_date
            rate = 5
            amount = principle * (1 + (rate/100)) ** time

            print(f"💵  You will get Rs. {amount} after {fd_maturity_date} year(s)")

            while True:
                query1 = 'SELECT Balance FROM Accounts WHERE Account_Number = {}'.format(acc_no)
                cursor.execute(query1)
                data = cursor.fetchone()
                new_balance = data[0] - fixed_deposite
                if new_balance < 0:
                    print(f"⚠️  Your account does not have that much amount. Available: {data[0]}")
                    break
                else:
                    query2 = "UPDATE Accounts SET Balance={} WHERE Account_Number={}".format(new_balance, acc_no)
                    cursor.execute(query2)

                    query3 = "INSERT INTO Fixed_Deposite(FD_ID,Account_Number,Fixed_Deposite,FD_Maturity_Date,Final_Amount) VALUES ({},{},{},date_add(curdate(), interval {}),{})".format(fd_id, acc_no, fixed_deposite, fd_maturity_date1, amount)
                    cursor.execute(query3)

                    print(f"📝  Your Fixed Deposit ID is {fd_id}")

                    print("\n" + "="*55)
                    print("✅  FD CREATED SUCCESSFULLY".center(55))
                    print("="*55 + "\n")
                    con.commit()
                    break
                
        print("🔁 Do you want to make another FD?")
        print("If yes, press 'y' 🟢  otherwise press Enter ⏎ to exit.")
        choi = input()
        if choi.lower() != "y":
            break

    con.commit()

def Details_of_FD(acc_no):

    print("="*70)
    print("\t\tWELCOME TO FIXED DEPOSITE DETAILS PORTAL")
    print("="*70)
    print()
    query = "select * from fixed_Deposite where Account_Number = {}".format(acc_no)
    cursor.execute(query)
    data = cursor.fetchall()
    if cursor.rowcount == 0 :
        print("There is no FD details for this account number")
    else:
        n = 1
        print("FD details are given below")
        print()
        for i in data:
            print("FD - {}".format(n))
            print()
            print(f"{'FD ID :':<25} {i[0]}")
            print(f"{'Account Number :':<25} {i[1]}")
            print(f"{'Fixed Deposite :':<25} {i[2]}")
            print(f"{'FD Maturity Date :':<25} {i[3]}")
            print(f"{'Final Amount :':<25} {i[4]}")
            n += 1
            print()

    con.commit()

while True:
    print("OTP Verification")
    num = random.randint(100000, 999999)
    print("\n🎲  Please enter the number shown below to proceed:")
    print("\t\t🔢", num)
    
    chek = input("✏️  Enter the above shown OTP: ")
    chek = int(chek)
    
    if chek == num:
        print("\n" + "="*60)
        print("✅  You have successfully entered the correct OTP!".center(60))
        print("="*60 + "\n")
        break
    else:
        print("⚠️  Incorrect number entered. Please try again.\n")

print("\n⚠️  DISCLAIMER: If you want to exit the bank system anywhere in the project, type 'exit'.\n")
Create_requirement()
password = "krishna2025"

print("="*60)
print("🏦  WELCOME TO".center(60))
print("💰  GLOBAL TRUST BANK 🌍  💰".center(60))
print("Your Trusted Partner in Secure Banking".center(60))
print("="*60)
print()

while True:
    login=Login()
    # Admin operations
    while login == "admin":
        print("\n🛠️  CHOOSE AN OPERATOR (ADMIN)\n")
        print("1️⃣  Create Account")
        print("2️⃣  Deactivate Account")
        print("3️⃣  Display Accounts")
        print("4️⃣  Update Details")
        print("5️⃣  Total Balance in Bank")
        print("6️⃣  Check The Complaint")
        print("7️⃣  Loan")
        print("8️⃣  Fixed Deposit")
        print("9️⃣  Exit from Admin\n")

        choice = input("Enter a choice: ")
        check(choice)
        choice = int(choice)

        if choice == 1:
            Create_Account()
        elif choice == 2:
            Deactivate_Account()
        elif choice == 3:
            Display_Accounts()
        elif choice == 4:
            Update_Details()
        elif choice == 5:
            Total_Balance_In_bank()
        elif choice == 6:
            Check_The_Complaint()
        elif choice == 7:
            Loan()
        elif choice == 8:
            Fixed_Deposite()
        elif choice == 9:
            print("\n🔒 Exiting Admin Portal...\n")
            break

    # User operations
    while login == "user":
        query = f"SELECT password FROM Accounts WHERE Account_Number = {acc_no}"
        cursor.execute(query)
        data = cursor.fetchall()

        print("🔑  Enter the password of your account:")
        passd = input()
        check(passd)

        if passd == data[0][0]:
            print("✅ Verification Successful\n")
            print("🛠️  CHOOSE AN OPERATOR (USER)\n")
            print("1️⃣  Deposit Money")
            print("2️⃣  Withdraw Money")
            print("3️⃣  Display Account Details")
            print("4️⃣  Check Account Balance")
            print("5️⃣  Transfer Money")
            print("6️⃣  Transaction History")
            print("7️⃣  Raise a Complaint")
            print("8️⃣  Repayment of Current Loan")
            print("9️⃣  Details of FD")
            print("🔟  Exit from User\n")

            choice = input("Enter a choice: ")
            check(choice)
            choice = int(choice)

            if choice == 1:
                Deposite_Money(acc_no)
            elif choice == 2:
                Withdraw_Money(acc_no)
            elif choice == 3:
                Display_Account_Details(acc_no)
            elif choice == 4:
                Check_Account_Balance(acc_no)
            elif choice == 5:
                Transfer_Money(acc_no)
            elif choice == 6:
                Transaction_History(acc_no)
            elif choice == 7:
                Raise_A_Complaint(acc_no)
            elif choice == 8:
                Repayment_Of_Current_Loan(acc_no)
            elif choice == 9:
                Details_of_FD(acc_no)
            elif choice == 10:
                print("\n🔒 Exiting User Portal...\n")
                break

        else:
            print("❌ ERROR: Incorrect password. Please try again.\n")
    
    # Ask to login again
    print("🔄 Do you want to login as another user/admin? Press 'y' for yes, or Enter to exit.")
    choi = input("Enter your choice: ")
    check(choi)
    if choi.lower() == "y":
        continue
    else:
        print("\n🏦 Exiting Bank System... Have a great day! 💖\n")
        break
