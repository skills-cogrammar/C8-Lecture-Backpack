'''
Write a Python script that continuously accepts numbers entered by the user. 
The program should sum only the positive numbers. 
Once the user enters a negative number, the script should stop and display:
   1. the sum of the positive numbers 
   2. the total count of valid (positive) values entered.
'''

# Initialise variables to store sum and count
sum_of_numbers = 0
count = 0

# While loop to continuosly prompt the user
while True:
    number = int(input("Enter a positive number (or a negative number to stop): "))

    # If negative number is entered, break the loop
    if number < 0:
        break

    sum_of_numbers += number
    count += 1

# Print the sum and count
print(f"The total sum: {sum_of_numbers} and the total valid numbers entered: {count}")
    