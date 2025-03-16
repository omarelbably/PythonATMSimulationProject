# Interactive ATM Banking System

Welcome to the Interactive ATM Banking System! This program simulates basic banking functionalities, allowing users to check their balance, deposit money, withdraw cash, and exit with ease.

## Features
- **Welcome Greeting**: A personalized greeting for each user.
- **User Authentication**: Secure PIN-based authentication (three attempts before the card is blocked).
- **Main Menu**:
  - Check Balance
  - Deposit Money
  - Withdraw Money
  - Exit
- **Error Handling**:
  - Prompts for valid numeric inputs.
  - Handles insufficient balance and invalid options gracefully.
- **Exit Greeting**: A polite farewell after banking tasks are completed.

## Requirements
- Python 3.x installed on your system.

## How to Run
1. Clone or download this script.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the script using:
   ```
   python atm_banking_system.py
   ```
5. Follow the on-screen instructions.

## Sample Walkthrough
1. **Step 1**: Enter your name.
   - You'll be greeted with a personalized welcome message.
2. **Step 2**: Enter your PIN.
   - Correct PIN: Access the main menu.
   - Incorrect PIN (3 attempts): Your card will be blocked.
3. **Step 3**: Explore menu options:
   - **Check Balance**: Displays current account balance.
   - **Deposit Money**: Enter the deposit amount to update your balance.
   - **Withdraw Money**: Specify an amount to withdraw, ensuring sufficient balance.
   - **Exit**: Conclude the session with a thank-you message.
4. **Step 4**: Interact further or exit based on your choices.

## Example Commands
- To check balance, type **1** or "check balance".
- For deposit money, type **2** or "deposit money".
- To withdraw money, type **3** or "withdraw money".
- To exit, type **4** or "exit".
