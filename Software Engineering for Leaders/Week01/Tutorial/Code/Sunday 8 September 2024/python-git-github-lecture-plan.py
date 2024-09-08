# Bank ATM Withdrawal Simulation
balance = 1000  # Starting balance
attempts = 3    # Maximum attempts

print("Welcome to the ATM!")

while attempts > 0:
    withdrawal_amount = float(input("Enter amount to withdraw: "))
    
    if withdrawal_amount <= balance and withdrawal_amount > 0:
        balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: £{balance:.2f}")
        break
    else:
        attempts -= 1
        if withdrawal_amount <= 0:
            print("Invalid input! Withdrawal amount must be greater than zero.")
        elif withdrawal_amount > balance:
            print("Insufficient funds! Please try a smaller amount.")
        
        if attempts > 0:
            print(f"You have {attempts} attempt(s) remaining.")
        else:
            print("You have reached the maximum number of attempts. Please try again later.")

print("Thank you for using the ATM!")