"""
This combination of methods shows how Python enables flexible object creation 
and behaviour depending on the method type—whether class-specific, 
instance-specific, or completely independent (static).
"""

from datetime import datetime

# Get the current year
# This retrieves the current year using the datetime module and 
# assigns it to `current_year`.
current_year = datetime.now().year

class Person:
    def __init__(self, name, age):
        """
        Initialises a Person instance with a given name and age.
        
        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name  # Instance attribute 'name'
        self.age = age    # Instance attribute 'age'

    # A class method to create a Person object by their birth year
    @classmethod
    def fromBirthYear(cls, name, birth_year):
        """
        Creates a new Person instance by calculating the person's age from their birth year.

        :param cls: Refers to the class itself (Person).
        :param name: The name of the person.
        :param birth_year: The year the person was born.
        :return: A new instance of Person with the calculated age.
        """
        # Return a new Person instance, calculating age based on the current year
        return cls(name, current_year - birth_year)
    
    # A static method to check if a person is an adult based on their age
    @staticmethod
    def isAdult(age):
        """
        Determines if a person is an adult (age 18 or above) or a child.

        :param age: The age of the person.
        :return: A message indicating if the person is an adult or a child.
        """
        if age >= 18:
            print("This person is an adult.")
        else:
            print("This person is a child.")

# Create a Person instance using the standard initializer
person1 = Person("Bluey", 7)  # Person object created with age 7

# Create a Person instance using the class method 'fromBirthYear' 
# This automatically calculates the age from the birth year (2019)
person2 = Person.fromBirthYear("Bingo", 2019)

# Output the age of person1 (Bluey) and person2 (Bingo)
print(f"Person 1 age: {person1.age}")  # Output: 7
print(f"Person 2 age: {person2.age}")  # Output: Calculated based on current year - 2019

# Use the static method to check if a person is an adult
Person.isAdult(42)  # Static method that checks if 42-year-old is an adult

# ============  Description of the above follows below:
"""
Instance Method (__init__):

Class Method (fromBirthYear):

Static Method (isAdult):

This combination of methods shows how Python enables flexible object creation 
and behaviour depending on the method type—whether class-specific, 
instance-specific, or completely independent (static).
"""