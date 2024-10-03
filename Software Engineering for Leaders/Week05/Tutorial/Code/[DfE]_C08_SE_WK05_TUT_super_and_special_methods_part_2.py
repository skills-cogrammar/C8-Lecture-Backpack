# Title: Special Methods Example
# Objective: Demonstrate the use of special methods `__str__` and `__gt__` in classes, with a thorough explanation of the `super()` function.
# Description: This example shows how to use `__str__` for providing a string representation of objects and `__gt__` for comparing two objects.
#              It also highlights the role of `super()` in initializing the base class and ensuring proper attribute setup.

# Base class (Parent)
class Transport:
    def __init__(self, name, speed):
        # Initialize the name and speed of the transport
        self.name = name
        self.speed = speed  # Speed in km/h
    
    def travel_time(self, distance):
        # Calculate travel time based on speed
        return distance / self.speed

# Derived class (Child 1)
class Car(Transport):
    def __init__(self):
        # Use super() to call the __init__ method of the base class Transport
        # This is crucial because it ensures that the initialization logic of the Transport class is executed.
        # Specifically, it sets up the 'name' and 'speed' attributes with the values provided here.
        super().__init__(name="Car", speed=100)
    
    def __str__(self):
        # Return a string representation of the Car object
        return f"{self.name}: Speed = {self.speed} km/h"

    def __gt__(self, other):
        # Compare the speed of this Car object with another Transport object
        return self.speed > other.speed

# Derived class (Child 2)
class Bicycle(Transport):
    def __init__(self):
        # Use super() to call the __init__ method of the base class Transport
        # This ensures that the 'name' and 'speed' attributes are correctly initialized for the Bicycle object.
        # Without this, the Bicycle class would not have these attributes set up properly.
        super().__init__(name="Bicycle", speed=20)
    
    def __str__(self):
        # Return a string representation of the Bicycle object
        return f"{self.name}: Speed = {self.speed} km/h"

    def __gt__(self, other):
        # Compare the speed of this Bicycle object with another Transport object
        return self.speed > other.speed

# Create instances of Car and Bicycle
car = Car()
bicycle = Bicycle()

# Output the string representation of each vehicle
print(str(car))        # Output: Car: Speed = 100 km/h
print(str(bicycle))    # Output: Bicycle: Speed = 20 km/h

# Compare the speeds of Car and Bicycle
if car > bicycle:
    print("The car is faster than the bicycle.")
else:
    print("The bicycle is faster than the car.")
