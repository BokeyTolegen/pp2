print(10 > 9)
print(10 == 9)
print(10 < 9)

"""Print a message based on whether the condition is True or False:"""
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Следующее вернет True:
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Следующее вернет False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

"""Eщe одно значение или объект в данном случае оценивается как False, и это если у вас есть объект, созданный из класса с функцией __len__, которая возвращает 0 или False:"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

"""Вы можете создавать функции, которые возвращают логическое значение:"""
def myFunction() :
  return True

print(myFunction())

"""Python также имеет множество встроенных функций, которые возвращают логическое значение,
например функцию isinstance() , которую можно использовать для определения того, принадлежит ли объект к определенному типу данных:"""
x = 200
print(isinstance(x, int))

#EXERCISES
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("abc"))
print(bool(0))


























































