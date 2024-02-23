import math
#1 Write a Python program to convert degree to radian.
deg = int(input())
rad = deg * math.pi / 180
print(rad)

#2 Write a Python program to calculate the area of a trapezoid.
height = int(input())
base1 = int(input())
base2 = int(input())

semi_perimeter = (base1 + base2) / 2

area = semi_perimeter * height
print(area)

#3 Write a Python program to calculate the area of regular polygon.
num = int(input())
length = float(input())
apothem = length / (2 * math.tan(math.pi / num))
area = num * apothem * length // 2

print(int(area))

#4 Write a Python program to calculate the area of a parallelogram.
base = float(input())
height = float(input())
print(base * height)

























