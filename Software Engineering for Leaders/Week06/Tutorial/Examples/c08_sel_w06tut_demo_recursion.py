# ============ Compute the product of two positive integers recursively using addition and subtraction
class Product:
    """
    Provides methods to compute the product of two positive integers recursively
    using only addition and subtraction.
    """
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def product(self, a=None, b=None):
        """
        Computes the product of two positive integers using recursion.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        # If 'a' or 'b' is not passed as an argument, use the instance variables
        if a is None:
            a = self.a
        if b is None:
            b = self.b

        # Base Case:
        if b == 0:
            return 0
        # Recursive Case:
        return a + self.product(a, b-1)

    def product_iterative(self, a=None, b=None):
        """
        Computes the product of two positive integers iteratively.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        if a is None:
            a = self.a
        if b is None:
            b = self.b

        # Initialise product to 0
        prod = 0

        # Add 'a' to 'prod' exactly 'b' times
        for _ in range(b):
            prod += a
        
        return prod
		
    def product_normal(self, a=None, b=None):
        """
        Computes the product of two positive integers using the '*' operator.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        if a is None:
            a = self.a
        if b is None:
            b = self.b

        return a * b


# Example usage of the Product class
print(Product().product(3, 5))  # Output: 15

"""
Recursive Calculation Breakdown:

product(3, 5) = 3 + product(3, 4)
product(3, 4) = 3 + product(3, 3)
product(3, 3) = 3 + product(3, 2)
product(3, 2) = 3 + product(3, 1)
product(3, 1) = 3 + product(3, 0)
product(3, 0) = 0 (base case)

Adding these up step by step:

3 + 0 = 3
3 + 3 = 6
3 + 6 = 9
3 + 9 = 12
3 + 12 = 15
"""

# ==== Using object instantiation and instance variables
my_product = Product(3, 5)

# Recursive method
print(my_product.product())         # Output: 15

# Using normal multiplication
print(my_product.product_normal())  # Output: 15

# Iterative method
print(my_product.product_iterative())  # Output: 15


# ============ Check if a string is a palindrome (Reads the same both directions)
class CheckIfPalindrome():
    """
    Provides methods to check if a string is a palindrome.
    """
    def __init__(self):
        pass

    def check_if_palindrome_iterative(self, word):
        """
        Checks if a string is a palindrome iteratively.

        Parameters:
            word (str): The string to be checked.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        last_char = len(word) - 1
        count = 0

        # While the two pointers are not crossing
        while count < last_char:  
            if word[count] == word[last_char]:
                count += 1          # Move forward from the start
                last_char -=1       # Move backward from the end
            else:
                return False        # Mismatch found, not a palindrome

        return True

    def check_if_palindrome_recursive(self, word, idx_start, idx_end):
        """
        Checks if a string is a palindrome recursively.

        Parameters:
            word (str): The string to be checked.
            idx_start (int): The starting index of the string.
            idx_end (int): The ending index of the string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Base Case: If pointers have crossed or met, it's a palindrome.
        if idx_start >= idx_end:
            return True
        
        # If characters at both ends don't match, it's not a palindrome.
        if word[idx_start] != word[idx_end]:
            return False
        
        # Recursive Case: Move pointers inward.
        return self.check_if_palindrome_recursive(word, idx_start + 1, idx_end - 1)


# ======= Even length palindrome
word = "gohangasalamiimalasagnahog"

# Test CheckIfPalindrome Iterative
print(CheckIfPalindrome().check_if_palindrome_iterative(word))  # Output: True

# Test CheckIfPalindrome Recursive
count = 0
last_char = len(word) - 1
print(CheckIfPalindrome().check_if_palindrome_recursive(word, count, last_char))  # Output: True

# ==== Using object instantiation and instance variables
my_checker = CheckIfPalindrome()

# Even length palindrome
count = 0
last_char = len(word) - 1

print(my_checker.check_if_palindrome_recursive(word, count, last_char))  # Output: True

# Odd length palindrome
print(my_checker.check_if_palindrome_recursive("racecar", 0, len("racecar") - 1))  # Output: True

# Non-palindrome
print(my_checker.check_if_palindrome_recursive("hello", 0, len("hello") - 1))  # Output: False