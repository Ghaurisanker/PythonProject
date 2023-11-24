#Day2: 30 days of python programming

first_name = "Ghaurisanker"
last_name = "Ezhilarasu"
full_name = "Ghaurisanker Ezhilarasu"
age = 25
date_of_birth = 1998
is_true = True
is_false = False

#type(first_name, last_name, full_name)
print(len(first_name))
print()

#Comparison of two strings using len()
if len(first_name) == len(last_name):
    print("True")
else:
    print("False")
print()

#Basic arithmetic operations
num_one = 5
num_two = 4
sum = num_one + num_two
print(sum)
difference = num_one - num_two
print(difference)
product = num_one * num_two
print(product)
quotient = num_one/num_two
print(quotient)
remainder = num_one % num_two
print(remainder)
floor_division = num_one // num_two
print(floor_division)
print()

#Calculate the area of circle
radius = 30
#radius = input("Enter the radius")
area = radius * radius
print(area)

circum_of_circle = 2*3.17*radius
print(circum_of_circle)

'''
Todo:
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
'''

