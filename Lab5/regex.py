import re 
#1
print("Write a and b:")
AB = str(input())
print(re.match("ab*", AB))
#2
print("Write a and b:")
AB = str(input())
print(re.match("ab{2,3}", AB))

#3
print("Write:")
a_b = str(input())
print(re.findall(r"[a-z]+_[a-z]+", a_b))

#4
print("Write:")
Aa = str(input())
print(re.findall(r"[A-Z][a-z]+", Aa))

#5
print("Write a and b:")
AB = str(input())
print(re.match(r"^a.*b$", AB))

#6
print("Write:")
A = str(input())
print(re.sub("\s",";", A))

#7
import re

def snake_to_camel(text):

  return re.sub(r'(?<!^)_([a-z])', lambda match: match.group(1).upper(), text)

print(snake_to_camel('hello_world')) 
print(snake_to_camel('snake_case')) 

#8
print("Write:")
A_B = str(input())
print(re.findall(r"[A-Z][a-z]*|[a-z]", A_B)) #ItsAnExample ->['Its', 'An', 'Example']

#9
print("Write:")
A = str(input())
print(re.sub(r"(?<!^)(?=[A-Z])", "_", A)) #ThisIsAStringWithUppercaseLetters -> This_Is_A_String_With_Uppercase_Letters

#10
import re

def camel_to_snake(text):

  return re.sub(r'(?=[A-Z])', r'_', text).lower()

print(camel_to_snake('HelloWorld'))  #hello_world
print(camel_to_snake('SnakeCase'))  #snake_case



