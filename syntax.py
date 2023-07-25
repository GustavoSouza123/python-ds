# variables
# python has no command for declaring a variable
name = "Gustavo"
age = 16
print(name, age)
print("my name is " + name + " and I am " + str(age) + " years old") # it is not possible to concatenate a string with an integer

# get the data type of a variable
print(type(name))
print(type(age))

# assign values to multiple variables
x, y, z = 1, 2, 3
print(x, y, z, sep=", ")

# random number
import random
print(random.randrange(1, 10)) # prints a random number between 1 and 9

# casting
print(int('1') + 1)
print(float('1.5') + 1.2)
print(str(20) + '07')

# multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)

# string length
str = "my str"
print(len(str))

# check if a phrase or character is present within a string
txt = "I am a programmer and I like to code"
print("code" in txt)
print("python" in txt)

# check if a phrase or character is not present within a string
print("code" not in txt)
print("python" not in txt)

# slicing strings
str = "Hello, World"
print(str[2:5])
print(str[:5]) # slice from the start
print(str[2:]) # slice to the end

# string methods
print(str.upper())
print(str.lower())

str = "    Hello, World  "
print(str)
print(str.strip()) # remove whitespace

str = "Hello, World"
print(str.replace("Hello", "Goodbye")) # replace string

# if statement
a = 10;
b = 8;
if a > b:
    print("{} greater than {}".format(a, b));
elif a == b:
    print("{} equals {}".format(a, b))
else:
    print("{} greater than {}".format(b, a))

# while loop
i = 1
while i < 5:
    print(i)
    i += 1

# for loop
for x in range(5):
    print(x)

for x in range(3, 8):
    print(x)

for x in range(5, 20, 4):
    print(x)

# iterating over a list
fruits = ["apple", "banana", "grapes"]
for fruit in fruits:
    print(fruit)