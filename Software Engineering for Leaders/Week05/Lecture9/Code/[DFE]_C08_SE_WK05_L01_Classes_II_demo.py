# Base class for vehicles
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"

    def rent(self):
        return "This vehicle is available for rent."

    def calculate_rental_cost(self, days, base_rate = 20):
        try:
            if not isinstance(days, int):
                raise TypeError("Number of days must be an integer.")
            if days <= 0:
                raise ValueError("Number of days must be greater than 0.") 
            return base_rate * days
        except (TypeError, ValueError) as e:
            return str(e)

# Subclass for cars
class Car(Vehicle):
    def __init__(self, make, model, year, seating_capacity):
        super().__init__(make, model, year)
        self.seating_capacity = seating_capacity

    def rent(self):
        return f"Renting a car: {self.get_details()} with seating for {self.seating_capacity} people."

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days, base_rate = 40)

# Subclass for bikes
class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def rent(self):
        return f"Renting a {self.bike_type} bike: {self.get_details()}."

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days, base_rate = 10)

# Example usage
car = Car("Toyota", "Corolla", 2022, 5)
bike = Bike("Yamaha", "MT-07", 2021, "sports")

print(" ")
print(car.rent())
print(" ")

print(f"Cost to rent the car for 3 days: ${car.calculate_rental_cost(3)}")
print(f"Cost to rent the car for -1 days: {car.calculate_rental_cost(-1)}")
print(f"Cost to rent the car for 'three' days: {car.calculate_rental_cost('three')}")
print(" ")
print(bike.rent())
print(" ")
print(f"Cost to rent the bike for 2 days: ${bike.calculate_rental_cost(2)}")

