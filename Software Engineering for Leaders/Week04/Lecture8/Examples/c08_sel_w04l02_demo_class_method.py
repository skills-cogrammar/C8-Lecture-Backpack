"""
This example demonstrates the concept of class attributes and class methods 
in Python. Specifically, it illustrates how a class can keep track of the 
total number of instances created by maintaining a class attribute (total_people) 
and how this information can be accessed and displayed using a 
class method (display_total_people). 
The example also shows how instance attributes (like name) are assigned to 
individual objects while the class attribute is shared across all instances.
"""

class Archers:
    """
    The Archers class tracks the number of instances (archers) created and 
    provides functionality to display the total number of archers.
    
    Attributes:
        total_people (int): A class attribute that keeps a count of all instances 
        created from the class.
    """
    
    # This is a class variable that holds the total number of Archers created. 
    # It is shared among all instances of the Archers class.
    total_people = 0

    def __init__(self, name):
        """
        Initialises an Archer instance with a specific name and increments the 
        total_people class attribute by 1 whenever a new Archer is created.
        
        Args:
            name (str): The name of the archer.
        """
        self.name = name
        # Below increments the total number of Archers each time a new instance is created
        Archers.total_people += 1  

    @classmethod
    def display_total_people(cls):
        """
        A class method that prints the total number of Archer instances created. 
        
        The class method uses the `cls` parameter to access the 'total_people' 
        class attribute, which is shared among all instances.
        
        Args:
            cls: A reference to the class itself, allowing access to 
            class attributes and methods.
        """
        print(f"Total people: {cls.total_people}")


# Creating two instances of the Archers class with different names.
archer1 = Archers("Legolas")
archer2 = Archers("Robin Hood")

# Calling the class method to display the total number of Archers created.
# Since two instances were created, this will print "Total people: 2".
Archers.display_total_people()
