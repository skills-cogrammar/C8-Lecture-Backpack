""" ****** Implementing a Class with Methods ****** """

# Creating a Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return f"{self.make} {self.model} is driving."

# Class instantiation - Creating an object or instance of the class
my_car = Car("Toyota", "Camry", 2022)

# Calling methods
print(my_car.drive())  # Output: Toyota Camry is driving.

""" ****** Preparing and accessing Controlled Attributes and Methods ****** """

# Preparing Attribute Access Control
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):          # Public Method using private attribute
        return self.__balance

# Preparing Method Access Control
    def __withdraw(self, amount):  # Private method
        self.__balance -= amount

# Accessing Controlled Attributes and Methods
account_pete = BankAccount(1000)
print(account_pete.get_balance())  # Output: 1000
account_pete.__withdraw(500)  
# Error: AttributeError: 'BankAccount' object has no attribute '__withdraw'

""" ****** Encapsulation ****** """

""" ==================================
Access Modifiers are used to specify the accessibility or visibility of a class, 
its members (methods and variables), and other entities. 
Access modifiers define the scope in which these elements can be accessed. 
They are essential for implementing encapsulation, 
one of the fundamental principles of OOP.
"""

# ================ 1. Public Variable
"""
Accessible from outside the class or module.
Part of the public interface.
"""
class MyClass:
    def __init__(self):
        self.public_variable = "Accessible Everywhere"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the public variable from outside the class
print(my_object.public_variable)

# ================ 2. Protected Variable
"""
No name mangling is applied.
Conventional indication that the variable is meant for internal use.
Still accessible from outside the class.
"""
class MyClass:
    def __init__(self):
        self._protected_variable = "Limited Access"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the protected variable from outside the class
print(my_object._protected_variable)

# ================ 3. Private Variable
"""
Name mangling is applied.
Accessible with a mangled name from outside the class.
Not a strict access control mechanism, more of a convention.
"""
class MyClass:
    def __init__(self):
        self.__private_variable = "Secret"

# Accessing the private variable from outside the class
my_object = MyClass()

print(my_object.__private_variable)             # Note this code gives error
# print(my_object._MyClass__private_variable)       # Name mangling must be applied

""" ==================================
Getter Methods:

Getter methods, are used to retrieve the values of private or protected attributes.
They provide read-only access to the internal state of an object.
The naming convention for a getter method is typically get_attribute(), ie. get_value
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())  # Output: 42

"""
Setter Methods:

Setter methods, are used to modify the values of private or protected attributes.
They provide a way to control the modification of internal state and 
enforce validation rules. The naming convention for a setter method is 
typically set_attribute().
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the setter method to modify the value
my_object.set_value(50)

"""
Setter & Getter combination to run.
"""
# Getter Method:
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value
    
    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())

# Setter Method:

# Using the setter method to modify the value
my_object.set_value(50)

# Using the getter method to access the modified value
print(my_object.get_value())
