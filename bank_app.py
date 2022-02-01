import random 

# print(a)



data = {

    "2051038492" : {
         "name": "Ralu",
         "dob" : "01-07-03",
         "bvn" : "00000000",
         "pin" : "2003",
         "bal": 0
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
        actions()
    else: print("Invalid Login")


def signUp():
    name = input("Enter your name: \n>")
    dob = int(input("Enter your date of birth: \n>"))
    bvn = int(input("Enter your bvn: \n>"))
    pin = int(input("Enter your pin: \n>"))
    balance = int(input("Enter your account balance: \n>"))

    a = random.randint(1111111111, 9999999999)

    new = {(a) : {
         "name": (name),
         "dob" : (dob),
         "bvn" : (bvn),
         "pin" : (pin),
         "bal": (balance)
    }}

    data.update(new)
    print(data)

    print(f"{a} is your new Account Number")

    print(f"Welcome {name}. \n Your account balance is {balance} ")
    actions()

def actions():
    actions = input("Would you like to do something else: Y/N \n>")
    if actions.lower() == 'y':
        prompt = int(input("Actions: \n1. Withdraw \n2. Deposit \n3. Check Balance \n4. Cancel"))
        if prompt == 1:
            withdrawal()
        elif prompt == 2:
            deposit()
        elif prompt == 3:
            print(data['bal'])
        elif prompt == 4:
            print("Thank you for your patronage!")
        else: print("Invalid Input")
    elif actions.lower() == 'n':
        print("Thank you for your patronage!")
    else:
        print("Invalid input")

        


def withdrawal():
    user_bal = data.get('bal')
    amount = int(input("Enter amount to be withdrawn: \n>"))
    if user_bal >= amount:
        user_bal -= amount
        print(f"Amount withdrawn:\n{amount}\nBalance: {data['a']['bal']}")
    else:
        print("Insufficient funds")


def deposit():
        amount = float(input("Enter amount to be deposited: \n>"))
        data["a"]["bal"] += amount
        print(f" Amount Deposited: {amount}\n Balance: {data['a']['bal']}")






if choice == 'l':
    logIn()

elif choice == 's':
    signUp()
else:
    print("Thanks for your patronage")
    
    





