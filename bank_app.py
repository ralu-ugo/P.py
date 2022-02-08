import random
from re import S


# print(a)



data = {

    "2051038492" : {
         "name": "Ralu",
         "dob" : "01-07-03",
         "bvn" : "00000000",
         "pin" : "2003",
         "bal": 5000,
         "account": "2051038492"
    }
}

print("Welcome to the AstroBank App")
print("Enter s to sign up or l to login:")
choice = input('>').lower()


def logIn():
    acc_num = (input("Enter your account number: \n>"))
    pin = input("Enter your pin: \n>")

    user = data.get(acc_num)

    if user is not None and user['pin'] == pin:
        print("You have successfully logged in!") 
    else:
        print("Login Failed")

    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}. \n Your account balance is {user['bal']} ")
        actions(user)
    else: print("Invalid Login")


a = random.randint(2051111111, 2059999999)


def signUp():
    name = input("Enter your name: \n>")
    dob = input("Enter your date of birth: \n>")
    bvn = input("Enter your bvn: \n>")
    pin = input("Enter your pin: \n>")
    # balance = int(input("Enter your account balance: \n>"))


    details = [('name', name), ('dob', dob), ('bvn', bvn), ('pin', pin), ('bal', 0), ('account', (a))]

    data[a] = dict(details)

    

    # new = {(a) : {
    #      "name": (name),
    #      "dob" : (dob),
    #      "bvn" : (bvn),
    #      "pin" : (pin),
    #      "bal": (balance)
    # }}

    # data.update(new)  
    print(data)

    print(f"{a} is your new Account Number")

    print(f"Welcome {name}. \n Your account balance is {data[a]['bal']} ")
    actions(data[a])

def actions(user_data):
    # print(f"user_data = {user_data['bal']}")
    actions = input("Would you like to do something else: Y/N \n>")
    if actions.lower() == 'y':
        prompt = int(input("Actions: \n1. Withdraw \n2. Deposit \n3. Transfer \n4. Check Balance \n5. Cancel\n>"))
        if prompt == 1:
            withdrawal(user_data)
        elif prompt == 2:
            deposit(user_data)
        elif prompt == 3:
            transfer(user_data)
        elif prompt == 4:
            balance(user_data)
        elif prompt == 5:
            print("Thank you for your patronage!")
        else: print("Invalid Input")
    elif actions.lower() == 'n':
        print("Thank you for your patronage!")
    else:
        print("Invalid input")

        


def withdrawal(user_data):
    user_bal = int(user_data["bal"])
    amount = int(input("Enter amount to be withdrawn: \n>"))
    if user_bal >= amount:
        user_bal -= amount
        print(f"Amount withdrawn:\n{amount}\nPlease take your cash. \nBalance: {user_bal}")
        actions(user_data)
    else:
        print("Insufficient funds")
        actions(user_data)



def deposit(user_data):
    amount = float(input("Enter amount to be deposited: \n>"))
    user_data["bal"] += amount
    print(f" Amount Deposited: {amount}\n Balance: {user_data['bal']}")
    actions(user_data)


def balance(user_data):
    print(f"Balance: {user_data['bal']}")
    actions(user_data)


def transfer(user_data):
    print(data)
    # Get amount to transfer
    # Get recipients account number
    # If account number exists in the database
        # Deduct amount from user balance 
        # Increase recipients balance by amount
        # Show success
    # Invalid Account Number

    amount = int(input("Enter an amount you would like to transfer: \n>"))
    recipients_acc = (input("Enter recepients account: \n>"))
    # print(data[recipients_acc]['account'])
    if recipients_acc != data[recipients_acc]['account']:
        print("Invalid Account Number")
    else:
        user_data['bal'] -= amount
        data[recipients_acc]['bal'] += amount
        print(f"Transfer successful\nBalance: {user_data['bal']}")
    

    












if choice == 'l':
    logIn()

elif choice == 's':
    signUp()
else:
    print("Thanks for your patronage")


# Transfer
    
    

