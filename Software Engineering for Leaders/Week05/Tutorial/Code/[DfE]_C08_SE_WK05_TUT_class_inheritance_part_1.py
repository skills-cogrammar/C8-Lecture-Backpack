# Title: Class Inheritance Example
# Objective: Demonstrate how to use class inheritance to create specialized child classes.
# Description: This example shows how the `Car` and `Bicycle` classes inherit from the base class `Transport`.
#              They override the `travel_time()` method and add their own methods.
#              `Car` has a method to calculate fuel requirements and `Bicycle` has a method for calories burned.

# Base class (Parent)
class Transport:
    def travel_time(self, distance):
        # Calculate travel time in a generic way
        return f"Travel time for {distance} km: 1 hour (generic transport)"

# Derived class (Child 1)
class Car(Transport):
    def travel_time(self, distance):
        # Overridden method: Calculate travel time specific to a car
        return f"Travel time for {distance} km: {distance / 100} hours by car"
    
    def fuel_required(self, distance):
        # Method specific to Car: Calculate the amount of fuel required
        return f"Fuel required for {distance} km: {distance / 15} liters"

# Derived class (Child 2)
class Bicycle(Transport):
    def travel_time(self, distance):
        # Overridden method: Calculate travel time specific to a bicycle
        return f"Travel time for {distance} km: {distance / 20} hours by bicycle"
    
    def calories_burned(self, distance):
        # Method specific to Bicycle: Calculate calories burned
        return f"Calories burned for {distance} km: {distance * 50} kcal"

# Create instances of each class
transport = Transport()
car = Car()
bicycle = Bicycle()

# Output the results of method calls
print(transport.travel_time(200))  # Output: Travel time for 200 km: 1 hour (generic transport)

print(car.travel_time(200))        # Output: Travel time for 200 km: 2.0 hours by car
print(car.fuel_required(200))      # Output: Fuel required for 200 km: 13.33 liters

print(bicycle.travel_time(200))    # Output: Travel time for 200 km: 10.0 hours by bicycle
print(bicycle.calories_burned(200)) # Output: Calories burned for 200 km: 10000 kcal
