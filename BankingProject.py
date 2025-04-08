# Global arrays and variable size
Account = [
[&quot;name1&quot;, &quot;password123&quot;],
[&quot;name2&quot;, &quot;pass456&quot;],

[&quot;name3&quot;, &quot;pas789&quot;]
]

AccDetails = [
[250.00, 100.00, 200.00],
[300.00, 150.00, 250.00],
[500.00, 200.00, 300.00]
]

Size = len(Account)

# Function to display the menu
def display_menu():
print(&quot;\nMenu:&quot;)
print(&quot;1. Display balance&quot;)
print(&quot;2. Withdraw money&quot;)
print(&quot;3. Deposit money&quot;)
print(&quot;4. Exit&quot;)

# Function to display balance
def display_balance(account_id):
print(f&quot;Current balance: ${AccDetails[account_id][0]:.2f}&quot;)

# Function to withdraw money
def withdraw_money(account_id):
amount = float(input(&quot;Enter amount to withdraw: &quot;))
balance = AccDetails[account_id][0]
overdraft_limit = AccDetails[account_id][1]
withdrawal_limit = AccDetails[account_id][2]

if amount &gt; withdrawal_limit:
print(&quot;Error: Amount exceeds the withdrawal limit.&quot;)
elif balance - amount &lt; -overdraft_limit:
print(&quot;Error: Insufficient funds, overdraft limit exceeded.&quot;)
else:
AccDetails[account_id][0] -= amount
print(f&quot;Withdrawal successful. New balance: ${AccDetails[account_id][0]:.2f}&quot;)

# Function to deposit money
def deposit_money(account_id):
amount = float(input(&quot;Enter amount to deposit: &quot;))
AccDetails[account_id][0] += amount
print(f&quot;Deposit successful. New balance: ${AccDetails[account_id][0]:.2f}&quot;)

# Function to verify account credentials
def verify_account(account_id, name, password):
return Account[account_id][0] == name and Account[account_id][1] == password

# Main program function
def main():
try:
account_id = int(input(&quot;Enter your account ID: &quot;))

if account_id &lt; 0 or account_id &gt;= Size:
print(&quot;Error: Account ID does not exist.&quot;)
return

name = input(&quot;Enter your name: &quot;)
password = input(&quot;Enter your password: &quot;)

if not verify_account(account_id, name, password):
print(&quot;Error: Name or password is incorrect.&quot;)
return

while True:
display_menu()

choice = int(input(&quot;Choose an action (1-4): &quot;))

if choice == 1:
display_balance(account_id)
elif choice == 2:
withdraw_money(account_id)
elif choice == 3:
deposit_money(account_id)
elif choice == 4:
print(&quot;Exiting the program.&quot;)
break
else:
print(&quot;Invalid choice, please select a valid option.&quot;)
except ValueError:
print(&quot;Invalid input, please enter a number.&quot;)

# Run the main function
if __name__ == &quot;__main__&quot;:
main()