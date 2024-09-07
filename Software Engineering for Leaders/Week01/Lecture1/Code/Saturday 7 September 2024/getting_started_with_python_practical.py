# Step 1: Get customer inputs
name = input("Enter you name: ")
age = int(input("Enter your age: "))
total_price = float(input("Enter the total order price: £"))
balance = float(input("Enter your account balance: £"))

# Step 2: Determine discount based on age group
if 18 <= age <= 25:
    discount = 0.10  # 10% discount
    age_group = "18-25"
elif 26 <= age <= 60:
    discount = 0.05  # 5% discount
    age_group = "26-60"
else:
    discount = 0.0  # No discount
    age_group = "under 18 or over 60"

# Step 3: Calculate the final price after discount
discounted_price = total_price * (1 - discount)

# Display the name, age group, discount, and discounted total
print("Welcome "+ name + "! " + "You'll get something!")
print(f"Age group: {age_group}, Discount: {discount * 100}%")
print(f"Discounted total: ${discounted_price:.2f}")

# Step 4: Check if balance is sufficient to complete the purchase
if balance >= discounted_price:
    print("Order processed successfully!")
else:
    shortfall = discounted_price - balance
    print(f"Insufficient balance. You need an additional ${shortfall:.2f} to complete the purchase.")