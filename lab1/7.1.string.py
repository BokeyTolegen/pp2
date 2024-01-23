#'hello' is the same as "hello".
print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x3 in "banana":
  print(x3)
  
#String Length
a1 = "Hello, World!"
print(len(a1))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present.")
  
#Check if NOT
txt2 = "The best things in life are free!"
print("expensive" not in txt2)

#Use it in an if statement:
txt3 = "The best things in life are free!"
if "expensive" not in txt3:
  print("No, 'expensive' is NOT present.")
  
  

  
