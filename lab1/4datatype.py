#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

"""EXAMPLES:
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""

"""Getting the Data Type"""
x = 5
print(type(x))

x2 = "Hello World"
print(type(x2))

x3 = 20.5
print(type(x3))

x4 = ["apple", "banana", "cherry"]
print(type(x4))

x5 = ("apple", "banana", "cherry")
print(type(x5))

x6 = {"name" : "John", "age" : 36}
print(type(x6))


"""Type Conversion"""
x1 = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x1)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""Random Number
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:"""
import random

print(random.randrange(1, 10))

