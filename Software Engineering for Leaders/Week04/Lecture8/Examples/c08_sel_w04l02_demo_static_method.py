""" The following example demonstrates both calling static methods directly from 
the class and using them from an instance (to show that, while it's possible, 
it's unnecessary)."""

class Calculator:
    """
    This class provides various mathematical operations. 
    While instance methods can be used for object-specific data, 
    a static method can perform a general operation that doesn't need to 
    interact with instance-specific data.
    """
    
    def __init__(self, brand):
        """
        Initialises a Calculator object with a specified brand name.
        
        :param brand: The brand name of the calculator.
        """
        self.brand = brand

    @staticmethod
    def add(a, b):
        """
        This static method performs addition of two numbers and returns the result.
        
        Static methods don't rely on any instance variables (such as 'brand'), 
        meaning they can be called without creating an instance of the class.
        
        :param a: First number to add.
        :param b: Second number to add.
        :return: The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        This static method performs subtraction of two numbers and returns the result.
        
        Like the add method, this doesn't use any instance-specific data.
        
        :param a: The number to subtract from.
        :param b: The number to subtract.
        :return: The result of a - b.
        """
        return a - b


# Example usage of the static methods
print(f"Adding 5 and 3: {Calculator.add(5, 3)}")      # Output: 8
print(f"Subtracting 7 from 10: {Calculator.subtract(10, 7)}")  # Output: 3

# Creating an instance of the Calculator class
casio_calculator = Calculator("Casio")

# Accessing static methods through an instance 
# (though it's not necessary for static methods)
print(f"Using a {casio_calculator.brand} calculator to add 12 and 8: {casio_calculator.add(12, 8)}")  # Output: 20
