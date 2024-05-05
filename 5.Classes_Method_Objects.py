class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Accessing object attributes
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)   # Output: 2022
