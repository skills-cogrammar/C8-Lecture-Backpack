# Title: Multiple Inheritance Example
# Objective: Demonstrate how to use multiple inheritance to combine functionalities from two base classes.
# Description: This example shows how the `ElectricCar` class inherits from both `Car` and `Electric` classes.
#              It combines methods from both base classes and introduces its own method.

# Base class (Parent 1)
class Car:
    def travel_time(self, distance):
        # Calculate travel time specific to a car
        return f"Travel time for {distance} km: {distance / 100} hours by car"

# Base class (Parent 2)
class Electric:
    def battery_status(self):
        # Return the battery status
        return "Battery at 80%"

# Derived class using Multiple Inheritance
class ElectricCar(Car, Electric):
    def charge_time(self):
        # Method specific to ElectricCar: Calculate charging time
        return "Charging time: 2 hours"

# Create an instance of ElectricCar
electric_car = ElectricCar()

# Output the results of method calls
print(electric_car.travel_time(200))      # Output: Travel time for 200 km: 2.0 hours by car
print(electric_car.battery_status())      # Output: Battery at 80%
print(electric_car.charge_time())         # Output: Charging time: 2 hours
