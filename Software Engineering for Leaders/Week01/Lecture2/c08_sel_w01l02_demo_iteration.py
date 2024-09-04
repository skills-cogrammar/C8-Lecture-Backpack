# ============= While loop Examples
 
# Example 1 - Printing a count up to 4
count = 1

while count < 5:
    print(count)
    # count += 1
    count = count + 1

"""
This while loop continues to execute as long as the condition (count <= 5) 
is true, illustrating how a while loop can repeatedly execute a block of code.
"""
# Example 2 - Counting down from 5
count = 5

while count > 0:
    print(count)
    count -= 1
print("takeoff!")

# Example 3: Menu example

# Initialise the choice variable
choice = ""

# Continue looping until the user chooses to exit
while choice != "3":
    # Display the menu
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Sum")
    print("3. Exit")

    # Get the user's choice - NOTE: input is always of type string
    choice = input("Please choose an option (1-3): ")

    # Process the user's choice
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        # Calculate the sum of two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")


# ============= For loop Examples

# Example 1
fruit_list = ["apple", "orange", "peer", "litchi"]

print(fruit_list)
print("This is the list 👆")

for fruit in fruit_list:
    print("Current fruit: ", fruit)

""" 
This for loop iterates over each element in the fruits list and prints it, 
demonstrating the use of iteration to automate repetitive tasks.
"""

# Example 2
random_sent = "Hello there General Kenobi"

for letter in random_sent:
    print(letter)

# Example 3
# range(6) = [1, 2, 3, 4, 5] - natural list

for number in range(1, 6):
    print(number)

for number in range(0, 10, 2):
    print(number)

# Example 4
for i in range(1, 4):
    # print("Outer Loop postion: ", i)
    for j in range(1, 4):
        # print("Inner Loop position", j)
        print(i * j, end=" ")
    print()

# Example 5: Nested for loops to iterate over a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value)

# Example 6
random_sent = "Well, of course I know him. He's me"
random_sent_split = random_sent.split(" ")
print(random_sent_split)

for word in random_sent_split:
    print(word)
    
# ============= Trace Table Example

# Example 1: Some logic with a loop

total = 0
for i in range(1, 4):
    total += i
print(total)

"""
Trace Table:

|   Step	|   i	|   total   |
|-----------|-------|-----------|
|    1	    |   1	|   1       |
|    2	    |   2	|   3       |
|    3	    |   3	|   6       |

The trace table tracks the values of i and total after each loop iteration 
to debug and verify loop logic.
"""

# Example 2: Logic with a loop and conditional statement

count = 0
for i in range(5):
    if i % 2 == 0:
        count += i
print(count)

"""
Trace Table:

|   Step	|   i	|   i % 2 == 0	|   count   |
|-----------|-------|---------------|-----------|
|   1	    |   0	|   True	    |   0       |
|   2	    |   1	|   False	    |   0       |
|   3	    |   2	|   True	    |   2       |
|   4	    |   3	|   False	    |   2       |
|   5	    |   4	|   True	    |   6       |

Walk through the code using the trace table to debug and validate its logic, 
ensuring the correct flow and calculations.
"""
