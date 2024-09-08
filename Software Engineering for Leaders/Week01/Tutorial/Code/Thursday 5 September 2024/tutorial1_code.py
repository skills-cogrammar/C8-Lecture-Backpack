# Data Types & Input
name = input("Enter your name: ")  # String
age = int(input("Enter your age: "))  # Integer
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'  # Boolean

# Conditional Statements
if age < 18:
    print(f"Hello {name}, you are a minor.")
elif 18 <= age < 65:
    print(f"Hello {name}, you are an adult.")
else:
    print(f"Hello {name}, you are a senior citizen.")

# While Loop: Countdown
count = 3
while count > 0:
    print(f"Starting in {count}...")
    count -= 1
print("Go!")

# For Loop: Multiplication Table
print("\nMultiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("")  # Blank line for separation