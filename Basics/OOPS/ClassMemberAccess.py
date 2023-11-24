# Python code for accessing attributes of class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# creating an object of Car class
my_car = Car("Toyota", "Camry", 2018)

# using getattr() to access an attribute
make_attr = getattr(my_car, "make")
print("Make of my car is:", make_attr)

# using hasattr() to check if an attribute exists
if hasattr(my_car, "color"):
    print("My car has a color attribute.")
else:
    print("My car does not have a color attribute.")

# using setattr() to set a new attribute
setattr(my_car, "color", "red")
print("Color of my car is:", my_car.color)

# using delattr() to delete an attribute
delattr(my_car, "year")
print("Year of my car is:", my_car.year)