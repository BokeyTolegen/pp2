carname = "Volvo"
x = 50
x = 5
y = 10
print(x + y)


x1 = 5
y1 = 10
print(x1 + y1)

x2 = 5
y2 = 10
z = x2 + y2
print(z)

x3 = 5
y3 = "John"
print(x3)
print(y3)

x4 = 4       # x is of type int
x4 = "Sally" # x is now of type str
print(x4)

x5 = str(3)    # x will be '3'
y5 = int(3)    # y will be 3
z5 = float(3)  # z will be 3.0

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"

"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x6, y6, z6 = "Orange", "Banana", "Cherry"
print(x6)
print(y6)
print(z6)

"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:"""
x7 = y7 = z7 = "Orange"
print(x7)
print(y7)
print(z7)

"""Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking."""
fruits = ["apple", "banana", "cherry"]
x8, y8, z8 = fruits
print(x8)
print(y8)
print(z8)

"""The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:"""
x9 = 5
y9 = "John"
print(x9, y9)

"""Global Variables"""
x10 = "awesome"

def myfunc():
  print("Python is " + x10)

myfunc()