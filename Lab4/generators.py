#ex 1
def my_generator(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1

n = int(input())

for value in my_generator(n):
    print(value)

#2
def even_num(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
even = even_num(n)
print(*even, sep=', ')

#3
def divisible(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
numbers = divisible(n)
for num in numbers:
    print(num)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
        
a = int(input())
b = int(input())   

for var in squares(a, b):
    print(var)   

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
countdown_gen = countdown(n)
for num in countdown_gen:
    print(num)

 
 
 
 
 
 
 
 
    
    