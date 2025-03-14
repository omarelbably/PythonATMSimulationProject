def welcomeGreet(name):
    print(f"Welcome to our banking service {name}")
def exitGreet():
    print(f"Thanks for banking with us {name}!")
def moreServiceChecker():
    global atmStatus
    while True:
        userInput = input("Do you want to check any other service? Yes or No ").lower()
        if userInput == "no":
            atmStatus = False
            exitGreet()
            break
        elif userInput == "yes":
            break
        else:
            print("Please select a valid option")

name = input("Please enter your name: ")
welcomeGreet(name)
# intial balance is 1000
balance = 1000
# the sample PIN is 12345
userPin = 12345
# recording the status of the ATM and the Card
atmStatus = False
cardStatus = True
# the user gets to try the pin 3 times, if incorrect the card will be blocked
trials = 1
while trials <= 3:
    while True:
        try:
            userPinCheck = int(input("Please Enter your PIN: "))
            break
        except ValueError:
            print("Please enter a valid number")
    if userPinCheck == userPin:
        atmStatus = True
        break
    elif trials == 3:
        print("Your card is blocked")
        cardStatus = False
        break
    else:
        print("PIN is incorrect")
        trials +=1
# the ATM program
while atmStatus and cardStatus:
    print("Main Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    userAction = input("Please enter your choice: ")
    if userAction.lower() == "check balance" or userAction.lower() == "1":
        print(balance)
        moreServiceChecker()
    elif userAction.lower() == "deposit money" or userAction.lower() == "2":
        while True:
            try:
                balance = balance + float(input("Please enter the deposited amount: "))
                break
            except ValueError:
                print("Please enter a valid number")
        print(f"Your new balance is {balance}")
        moreServiceChecker()
    elif userAction.lower() == "withdraw money" or userAction.lower() == "3":
        while True:
            try:
                withdrawalBalance = float(input("Please enter the amount to be withdrawn: "))
                break
            except ValueError:
                print("Please Enter a valid number")
        if balance > withdrawalBalance:
            balance = balance - withdrawalBalance
            print(f"Your new balance is {balance}")
        else:
            print("You don't have sufficient balance")
        moreServiceChecker()
    elif userAction.lower() == "exit" or userAction.lower() == "4":
        exitGreet()
        atmStatus = False
    else:
        print("Please choose the correct action")



