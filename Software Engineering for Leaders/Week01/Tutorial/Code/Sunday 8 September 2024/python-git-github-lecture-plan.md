### Practical Session: Python, The Terminal, Git & GitHub

#### **Session Agenda**
1. Terminal Basics
2. Python & Git Installation
3. GitHub Setup
4. Git Basics & Remote Repositories
5. Python Loops & Iterations
6. Comprehensive Coding Exercise
7. Pushing Code to GitHub
8. Intro to GitHub .dev Environment
9. Q&A and Wrap-up

**Total Duration: 115 mins**

---

### 1. **Terminal Usage and Manipulation**

**Guide:**
- Introduce basic terminal commands: `cd`, `ls/dir`, `pwd`, `mkdir`, `touch/new-item`, `rm`.
- Practice creating a directory and navigating:
  
```bash
mkdir PythonProject
cd PythonProject
pwd
```

- Explain the concept of the current working directory.

---

### 2. **Python Installation and Verification**

**Guide:**
- Download and install Python from [Python.org](https://www.python.org/).
- Verify installation by running:

```bash
python --version
```

- Demonstrate entering the Python interactive shell:

```bash
python
```

---

### 3. **Git Installation and Verification**

**Guide:**
- Download and install Git from [Git-SCM.com](https://git-scm.com/).
- Verify installation by running:

```bash
git --version
```

---

### 4. **Create a GitHub Account and Repository**

**Guide:**
- Walk through creating a GitHub account.
- Demonstrate creating a new repository named "PythonProject."
- Explain repository settings (public vs private, README, .gitignore, license).

---

### 5. **Connect Remote Repository to Local**

**Guide:**
- Initialize a local Git repository:

```bash
git init
```

- Connect to the remote repository:

```bash
git remote add origin https://github.com/yourusername/PythonProject.git
```

- Explain the concept of remote repositories.

---

### 6. **Checking Git Status**

**Guide:**
- Run and explain the output of:

```bash
git status
```

- Discuss untracked files, staged changes, and commits.

---

### 7. **Loops and Iterations**

**Objective:**
Simulate an ATM withdrawal process where a user can make a valid withdrawal. The system allows the user up to 3 attempts to enter a valid amount, ensuring the withdrawal is within their balance.

**Major Steps:**
1. **Initialize the balance**: Set a starting balance for the user (e.g., $1000).
2. **Set a maximum number of attempts**: Allow the user 3 attempts to enter a valid withdrawal amount.
3. **Check withdrawal validity**: Ensure the withdrawal is positive and less than or equal to the available balance.
4. **Update balance**: After a valid withdrawal, update the balance and show the new amount.
5. **Handle invalid inputs**: If the withdrawal is invalid, decrease the remaining attempts and notify the user.

**Code Example:**

```python
# Bank ATM Withdrawal Simulation

balance = 1000  # Starting balance in the account, set to £1000
attempts = 3    # The user gets a maximum of 3 attempts to make a valid withdrawal

# Greet the user
print("Welcome to the ATM!")

# Start a loop that continues while the user has attempts left
while attempts > 0:
    # Ask the user to input the amount they want to withdraw
    # Convert the input to a float (decimal number) to handle currency values
    withdrawal_amount = float(input("Enter amount to withdraw: "))
    
    # Check if the withdrawal amount is valid
    # It should be less than or equal to the balance and greater than zero
    if withdrawal_amount <= balance and withdrawal_amount > 0:
        # Deduct the withdrawal amount from the balance
        balance -= withdrawal_amount
        # Inform the user of a successful withdrawal and display the updated balance
        print(f"Withdrawal successful! Your new balance is: £{balance:.2f}")
        # Exit the loop after a successful withdrawal
        break
    else:
        # If the withdrawal is invalid, reduce the number of attempts by 1
        attempts -= 1
        
        # Check if the user entered an invalid amount (less than or equal to 0)
        if withdrawal_amount <= 0:
            print("Invalid input! Withdrawal amount must be greater than zero.")
        # Check if the withdrawal amount is greater than the available balance
        elif withdrawal_amount > balance:
            print("Insufficient funds! Please try a smaller amount.")
        
        # If the user still has attempts left, notify them of how many they have
        if attempts > 0:
            print(f"You have {attempts} attempt(s) remaining.")
        # If the user has no attempts left, display a message and end the loop
        else:
            print("You have reached the maximum number of attempts. Please try again later.")

# Say goodbye to the user after the transaction process
print("Thank you for using the ATM!")
```

#### 7.1. Explanation

- **`balance` and `attempts`**: Variables to store the starting account balance and track how many attempts the user has to make a valid withdrawal.
- **`while attempts > 0`**: Ensures the user gets 3 tries to enter a valid withdrawal amount.
- **`if withdrawal_amount <= balance and withdrawal_amount > 0`**: This checks if the amount is valid.
- **`balance -= withdrawal_amount`**: Updates the balance after a successful withdrawal.
- **`break`**: Exits the loop once a valid withdrawal is made.
- **Error messages**: Help guide the user if they enter an invalid withdrawal amount (too large, too small, or non-positive).

---

### 8. **Full Coding Exercise**

**Objective:**
Implement a full ATM withdrawal simulation, allowing the user up to 3 attempts to make a valid withdrawal. The program checks if the withdrawal amount is valid and ensures the balance is updated correctly.

**Major Steps:**
1. **Input data types**: Use `input()` for the withdrawal amount and ensure it's a valid float.
2. **Conditional statements**: Use `if-elif-else` to check for valid and invalid withdrawals.
3. **Loops**: Use a `while` loop to give the user up to 3 attempts.
4. **Output the result**: Show success or failure messages based on the withdrawal status and update the balance after a valid transaction.

**Code Example:**
- The same code from the **Loops and Iterations** section applies here.

---

### 9. **Push Code to GitHub**

**Guide:**
- Stage changes:

```bash
git add loops.py main.py
```

- Commit changes:

```bash
git commit -m "Add ATM withdrawal simulation example"
```

- Push to GitHub:

```bash
git push -u origin main
```

- View changes on the GitHub repository.

---

### 10. **GitHub .dev Environment**

**Guide:**
- Explain the concept of GitHub's .dev environment.
- Demonstrate how to access it:
  - Navigate to your GitHub repository.
  - Press the '.' key or change `.com` to `.dev` in the URL.

**Highlight Key Features:**
- Web-based VS Code environment.
- No need for local VS Code installation.
- Access to the full repository.
- Ability to edit, commit, and push changes directly from the browser.

---

Happy Coding!