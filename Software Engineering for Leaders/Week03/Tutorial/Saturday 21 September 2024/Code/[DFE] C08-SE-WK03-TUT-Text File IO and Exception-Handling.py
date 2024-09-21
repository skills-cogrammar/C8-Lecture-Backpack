"""
Title: ATM Simulator

Objective:
Create a program that simulates an ATM process. The customer can withdraw or deposit money based on their available balance. The program should:
- Allow the customer to input a withdrawal or deposit amount.
- Ensure the withdrawal amount is valid (a positive number and not exceeding the balance).
- Ensure the deposit amount is valid (a positive number).
- Update the customer's balance after each transaction (withdrawal or deposit).
- Log each transaction (successful or failed) into a transaction log file, including details like the transaction type, amount, remaining balance, and timestamp.
"""

# Initial customer balance
current_balance = 10000
# Name of the log file where transactions will be recorded
log_file_name = "transactions_logs.txt"

# Function to handle file operations such as logging messages to the file.
# The default file mode is 'a' (append) to ensure new transactions are added to the log
def file_operations(message, file_name=log_file_name, access_mode='a'):
    """
    This function handles writing to a file. 
    - message: the content to write to the file.
    - file_name: the name of the file where the log will be written (default is 'transactions_logs.txt').
    - access_mode: the mode in which to open the file ('a' for appending, 'w' for writing, etc.).
    
    Reason for design:
    - A function is used to centralize file operations to reduce repetitive code.
    - It allows flexibility to modify file handling in one place if needed.
    """
    with open(file_name, access_mode) as file:
        file.write(message)

# Infinite loop for continuous ATM operations until a user manually interrupts the program
while True:
    try:
        # Prompt the user to choose whether to withdraw (0) or deposit (1) money
        deposit_withdraw_decision = input("Would you like to withdraw (0) or deposit (1) money?: ")

        # Handling withdrawal process
        if deposit_withdraw_decision == '0':
            # Log the user's decision to the file
            file_operations(f"The user chose operation: Withdrawal\n")
            
            # Ask for the amount to withdraw and convert it to a float (raises ValueError if invalid input)
            amount = float(input("Enter the amount to withdraw: "))
            file_operations(f"The user attempted to withdraw {amount}\n")
            
            # Check if the withdrawal amount exceeds the current balance
            if amount > current_balance:
                error_message = "You don't have enough money to withdraw this amount."
                file_operations(f"Error Message: {error_message}\n")
                # Raising a NameError here to simulate custom handling for insufficient funds
                raise NameError(error_message)
            
            # Deduct the valid amount from the balance
            current_balance = current_balance - amount
            # Log the new balance to the file
            file_operations(f"New balance after withdrawal is: {current_balance}\n")
            # Optionally print the new balance for the user
            # print(f"New balance is: {current_balance}")

        # Handling deposit process
        elif deposit_withdraw_decision == '1':
            # Log the user's decision to the file
            file_operations(f"The user chose operation: Deposit\n")
            
            # Ask for the deposit amount and convert it to a float (raises ValueError if invalid input)
            amount = float(input("Enter the amount to deposit: "))
            file_operations(f"The user attempted to deposit {amount}\n")
            
            # For extremely large deposits, raise an OverflowError
            if amount > 1000000:  # Setting an arbitrary high limit to avoid overflow scenarios
                raise OverflowError("Deposit amount is too large. Please reduce the amount.")
            
            # Add the valid deposit amount to the balance
            current_balance = current_balance + amount
            # Log the new balance to the file
            file_operations(f"New balance after deposit is: {current_balance}\n")
            # Optionally print the new balance for the user
            # print(f"New balance is: {current_balance}")

        # Handling invalid input (neither '0' nor '1')
        else:
            file_operations("Error: Invalid operation code entered.\n")
            print("Invalid option! Please enter either '0' for withdrawal or '1' for deposit.")
        
        # Displaying the transaction log to the user
        with open("transactions_logs.txt", 'r') as file:
            content = file.read()
            print("Transaction Log:\n", content)

    # Custom exception handling for insufficient funds
    except NameError as en:
        print(f"Error encountered: {en}")
        print("Please try again ... :)")

    # Handle non-numeric inputs for the withdrawal or deposit amount (e.g., user enters 'abc' instead of a number)
    except ValueError as ev:
        print(f"Error encountered: {ev}")
        print("Invalid input! Please enter a valid number.")

    # Handling cases where the deposit amount exceeds the specified limit
    except OverflowError as eo:
        print(f"Error encountered: {eo}")
        print("Please try again with a smaller amount.")
