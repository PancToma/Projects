Account = [
    ["name1", "password123"],
    ["name2", "pass456"],
    ["name3", "pas789"]
]

AccDetails = [
    [250.00, 100.00, 200.00],
    [300.00, 150.00, 250.00],
    [500.00, 200.00, 300.00]
]

Size = len(Account)

# Function to display the menu
def DisplayMenu():
    print("Menu:")
    print("1. Display balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

# Function to display balance
def DisplayBalance(account_id):
    print(f"Current balance: ${AccDetails[account_id][0]:.2f}")

# Function to withdraw money
def withdraw(account_id):
    amount = float(input("Enter amount to withdraw: "))
    balance = AccDetails[account_id][0]
    overdraft_limit = AccDetails[account_id][1]
    withdrawal_limit = AccDetails[account_id][2]

    if amount > withdrawal_limit:
        print("Error: Amount exceeds the withdrawal limit.")
    elif balance - amount < -overdraft_limit:
        print("Error: Insufficient funds, overdraft limit exceeded.")
    else:
        AccDetails[account_id][0] -= amount
        print(f"Withdrawal successful. New balance: ${AccDetails[account_id][0]:.2f}")

# Function to deposit money
def Deposit(account_id):
    amount = float(input("Enter amount to deposit: "))
    AccDetails[account_id][0] += amount
    print(f"Deposit successful. New balance: ${AccDetails[account_id][0]:.2f}")

# Function to verify account credentials
def verifyAccount(account_id, name, password):
    return Account[account_id][0] == name and Account[account_id][1] == password

# Main program function
def main():
    try:
        account_id = int(input("Enter your account ID: "))
        
        if account_id < 0 or account_id >= Size:
            print("Error: Account ID does not exist.")
            return

        name = input("Enter your name: ")
        password = input("Enter your password: ")
        
        if not verifyAccount(account_id, name, password):
            print("Error: Name or password is incorrect.")
            return

        while True:
            DisplayMenu()
            choice = int(input("Choose an action (1-4): "))

            if choice == 1:
                DisplayBalance(account_id)
            elif choice == 2:
                withdraw(account_id)
            elif choice == 3:
                Deposit(account_id)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please select a valid option.")
    except ValueError:
        print("Invalid input, please enter a number.")

main()
