""" Describe the Purpose of Exception Handling and How it Improves Program Robustness """
# === Division operation without exception handling (program crashes on error).
def divide(a, b):
    return a / b

print(divide(10, 0))  # Program crashes with ZeroDivisionError

# === Division operation with exception handling (program continues running).
def divide(a, b):
    # Add the try-except into the code
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

print(divide(10, 0))  # Error handled, program continues

""" Write try-except Blocks to Catch and Handle Exceptions """
# === Simple try-except block to handle division errors.
try:
    # Add input to the code
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

""" Differentiate Between Various Built-in Exceptions and Handle Them Appropriately """
# === Handling both ZeroDivisionError and ValueError in a try-except block.
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
# Add the additional block below
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

""" Adding context to Built-in Exceptions """
def divide_numbers(a, b):
    # Check if the second argument is zero
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero!")  # Raise built-in exception

    return a / b

try:
    result = divide_numbers(10, 0)  # This will raise the exception
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")  # Catch the built-in exception

""" Explain the Role of the finally Block in the try-except Statement """
# === Using the finally block to perform an action regardless of 
# whether an exception occurs.
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block runs no matter what.")

""" Implement finally Blocks to Manage Clean-up Tasks Such as Closing Files or 
Releasing Resources """
# === Using the finally block to ensure a file is closed after being opened.
try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")

# From above, what if the file was never opened, then we don't want to get an error closing it.
# === Now we only want the file to be closed if the file was opened
file = None  # Initialise file variable

try:
    file = open("data.txt", "r")  # Attempt to open the file
    data = file.read()  # Read file content
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    if file:  # Check if the file was opened
        file.close()
        print("File closed.")

""" Discuss the Need for Custom Exceptions to Handle Specific Error Conditions 
in Programs """
# === Define a custom exception to handle age validation.
# Define a custom exception
class InvalidAgeError(Exception):
    """Custom exception to indicate invalid age input."""
    pass

# Function to validate age and raise the custom exception if necessary
def validate_age(age):
    try:
        if age < 0:
            # Raise the custom exception if the age is negative
            raise InvalidAgeError(f"Invalid age: {age}. Age cannot be negative.")
        else:
            print(f"Age {age} is valid.")
    except InvalidAgeError as e:
        # Catch and handle the custom exception
        print(e)

# Test the function with both valid and invalid ages
validate_age(16)  # Age is valid
validate_age(-5)  # Triggers custom exception

# === Adjust the invalid age example to test if a person is old enough
class NotOldEnoughError(Exception):
    """Custom exception to indicate the person is not old enough."""
    pass

# Function to validate age and raise the custom exception if necessary
def validate_age(age, required_age=18):
    try:
        if age < required_age:
            # Raise the custom exception if the person is not old enough
            raise NotOldEnoughError(f"Age {age} is not old enough. Must be at least {required_age} years old.")
        else:
            print(f"Age {age} is old enough.")
    except NotOldEnoughError as e:
        # Catch and handle the custom exception
        print(e)

# Test the function with both old enough and not old enough ages
validate_age(16)  # Triggers custom exception for being too young
validate_age(20)  # Age is old enough

""" Some additional full code examples """
# === Basic Try-Except Block to Handle Division by Zero 
# Function to divide two numbers with exception handling
def divide(a, b):
    try:
        # Try to divide the two numbers
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        # Catch the specific error where division by zero occurs
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Catch the error if inputs are not numbers
        print("Error: Both inputs must be numbers.")

# Test cases
divide(10, 2)  # Expected output: The result of 10 divided by 2 is 5.0
divide(10, 0)  # Expected output: Error: Cannot divide by zero.
divide(10, "two")  # Expected output: Error: Both inputs must be numbers.

# === Handling Multiple Exceptions in a Single Try Block
# Function to get two numbers from user input and divide them
def get_input_and_divide():
    try:
        # Get input from the user and convert to integers
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: You cannot divide by zero.")
    except ValueError:
        # Handle non-integer input
        print("Error: Please enter valid numbers.")
    finally:
        # This block always runs, whether an exception occurs or not
        print("Execution of the division operation complete.")

# Run the function
get_input_and_divide()

# === Using the else Clause in Exception Handling
# Function to calculate the square of a number with error handling
def calculate_square(number):
    try:
        # Attempt to calculate the square
        result = number ** 2
    except TypeError:
        # Handle the case where the input is not a number
        print("Error: The input must be a number.")
    else:
        # If no exception occurred, this block will run
        print(f"The square of {number} is {result}.")
    finally:
        # The final block will always execute
        print("Operation completed.")

# Test cases
calculate_square(5)  # Expected output: The square of 5 is 25.
calculate_square("five")  # Expected output: Error: The input must be a number.

# === Using the finally Block for Resource Cleanup
# Function to read from a file and demonstrate the use of 'finally' block
def read_file(file_name):
    try:
        # Attempt to open and read the file
        file = open(file_name, "r")
        data = file.read()
        print(data)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: File not found.")
    finally:
        # This block runs no matter what to ensure the file is closed
        print("Cleaning up: Closing the file.")
        try:
            file.close()  # Close the file if it was successfully opened
        except NameError:
            # Handle case where file wasn't successfully opened
            print("Error: No file to close.")

# Test the function
read_file("existing_file.txt")  # Replace with an actual file path to test
read_file("non_existent_file.txt")  # Expected output: Error: File not found.
