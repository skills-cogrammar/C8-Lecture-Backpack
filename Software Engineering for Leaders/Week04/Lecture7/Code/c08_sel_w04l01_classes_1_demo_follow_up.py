class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def update_year(self, new_year):
        self.year = new_year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# Method Calls and Expected Outputs
print(my_car.display_info())
# Expected Output: "2020 Toyota Corolla"

my_car.update_year(2022)
print(my_car.display_info())
# Expected Output: "2022 Toyota Corolla"
