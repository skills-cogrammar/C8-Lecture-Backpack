# Simple Bank Account Class Example

# Define the BankAccount class to model a bank account
class BankAccount:
    
    # Constructor (__init__) method to initialize the account number and balance
    # The default balance is set to 0, so a new account starts with a balance of 0 unless otherwise specified
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Account number is a public attribute that stores the account identifier
        self._balance = balance  # _balance is a private attribute to store the account balance (private by convention with _)
        self.transactions = []  # List to keep track of all transactions (deposits and withdrawals) made on this account
    
    # Method to deposit money into the account
    # This method adds the specified deposit amount to the balance and records the transaction
    def deposit(self, amount):
        self._balance += amount  # Increase the account balance by the deposit amount
        self.transactions.append(f"Deposit: {amount}")  # Log the deposit transaction in the transactions list
    
    # Method to withdraw money from the account
    # This method checks if there is enough balance before allowing the withdrawal
    def withdraw(self, amount):
        if self._balance >= amount:  # Only withdraw if the current balance is enough to cover the withdrawal
            self._balance -= amount  # Reduce the balance by the withdrawal amount
            self.transactions.append(f"Withdrawal: {amount}")  # Log the successful withdrawal
        else:
            # If balance is insufficient, record an unsuccessful withdrawal without changing the balance
            self.transactions.append(f"Unsuccessful Withdrawal: {amount}")
    
    # Method to return the current balance of the account
    def get_balance(self):
        return self._balance  # Returns the private _balance attribute which holds the current balance
    
    # Method to return the transaction history as a list of all transactions (deposits and withdrawals)
    def get_transaction_history(self):
        return self.transactions  # Returns the list of all transactions made on the account
    
    # Method to get a summary of the account
    # This method returns the account number, current balance, and all transactions
    def get_summary(self):
        return (f"\nAccount Number: {self.account_number}\n"  # Display the account number
                f"Current Balance: {self.get_balance()}\n"  # Display the current balance
                f"Transactions History: {', '.join(self.transactions)}\n")  # Display the transaction history


# Example usage of the BankAccount class:

# Create a new bank account with account number "12345"
account_1 = BankAccount("12345")

# Perform some operations on account_1
account_1.deposit(100)  # Deposit £100 into the account
account_1.withdraw(200)  # Attempt to withdraw £200 (this will fail since the balance is only £100)
account_1.deposit(200)  # Deposit another £200, bringing the balance to £300
account_1.withdraw(200)  # Withdraw £200 successfully, leaving £100 in the account

# Print a summary of account_1
print(account_1.get_summary())  # Should show the account number, balance, and transaction history


# Create a second account with account number "4567"
account_2 = BankAccount("4567")

# Deposit £100 into account_2 and print the summary
account_2.deposit(100)  # Deposit £100
print(account_2.get_summary())  # Should show the account number and balance with one deposit transaction
