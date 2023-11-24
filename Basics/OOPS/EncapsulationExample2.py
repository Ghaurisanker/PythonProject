class Car:
    def __init__(self, make, model, year):
        self._make = make    # protected attribute
        self._model = model  # protected attribute
        self._year = year    # protected attribute

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @make.setter
    def make(self, make):
        self._make = make

    @model.setter
    def model(self, model):
        self._model = model

    @year.setter
    def year(self, year):
        if year > 0:
            self._year = year
        else:
            print("Year must be a positive value.")

# Creating an instance of the class
car = Car(make="Toyota", model="Camry", year=2022)
print()

# Accessing attributes using properties
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")

# Modifying attributes using setters
car.make = "Honda"
car.model = "Civic"
car.year = 2023

# Displaying updated information
print(f"Updated Make: {car.make}")
print(f"Updated Model: {car.model}")
print(f"Updated Year: {car.year}")
print()

car.make = "Hundai"
car.model = "i20"
car.year = 2020

print(f"Updated Make: {car.make}")
print(f"Updated Model: {car.model}")
print(f"Updated Year: {car.year}")
