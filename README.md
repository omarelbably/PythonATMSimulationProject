---

# :bank: ATM Banking Service Program

This is a simple ATM banking service program written in Python. It allows users to interact with an ATM by checking balance, depositing money, withdrawing money, and exiting the service. The program includes a basic PIN verification system and ensures the user's account is secure by blocking the card after three incorrect PIN attempts.

## Features :sparkles:

- **User Authentication**: The user is prompted to enter a PIN. The program allows three attempts, after which the card is blocked.
- **ATM Services**:
  - **Check Balance** :moneybag: View the current account balance.
  - **Deposit Money** :money_with_wings: Deposit funds into the account.
  - **Withdraw Money** :bank: Withdraw funds from the account, provided there are sufficient funds.
- **Exit Service** :wave: Exit the ATM service and end the session.
- **Error Handling** :warning: Ensures users input valid data for amounts and PINs.

## :gear: How to Use

1. **Start the Program**: Run the script. It will prompt you to enter your name, and then greet you with a welcome message.
2. **Enter PIN**: The user is prompted to enter a PIN. The default PIN is `12345`, and you have three attempts to enter it correctly. If the PIN is incorrect three times, the card will be blocked.
3. **Main Menu**: Once authenticated, you'll be presented with the main menu:
   - **Option 1**: Check balance.
   - **Option 2**: Deposit money.
   - **Option 3**: Withdraw money.
   - **Option 4**: Exit the program.
4. **Additional Services**: After each action (checking balance, depositing, or withdrawing), the user will be asked if they want to perform another action or exit.

## Example Output :computer:

```
Please enter your name: John
Welcome to our banking service John
Please Enter your PIN: 12345
Main Menu:
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
Please enter your choice: 1
1000
Do you want to check any other service? Yes or No: no
Thanks for banking with us John!
```

## :clipboard: Code Structure

```python
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

# Main Program Flow
name = input("Please enter your name: ")
welcomeGreet(name)
balance = 1000
userPin = 12345
atmStatus = False
cardStatus = True
trials = 1

# PIN Authentication
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
        trials += 1

# ATM Menu Loop
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
```

## :warning: Requirements

- Python 3.x or higher
- No external libraries required.

## :page_with_curl: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
