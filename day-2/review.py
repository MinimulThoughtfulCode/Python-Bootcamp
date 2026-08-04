# Variables Review

num = 5
str = "Hello, World!"
list = ["apple", "banana", "orange"] # A list is a group of stuff

# Use str(), float(), int() to change to a string, numerical value, etc.

# Conditionals Review

if num == 5:
    print(num)
elif num > 5:
    print(f"This is more than {num}.")
else:
    print(f"This is less than {num}.")

# Operators Review

# Logical Operators
if num > 0 and num < 10:
    print(num)
elif num < 0:
    print("This is less than 0.") 
else:
    print(str)

if num == 0 or num == 5:
    print(str)
else:
    print(str)

# Math Operators
ival = 6

ival = ival + 4
ival = ival - 2
ival = ival * ival
ival = ival / 3
ival = ival % 4
print(ival)

# Comparison Operators

int = 5

if int == 3:
    print("False")
elif int != 3:
    print("True")
else:
    print("ERROR")

# For LOOP

list = ["apple", "banana", "orange"]

for fruit in list:
    print(fruit)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# While LOOP
count = 5

while count <= 5 and >= 0:
        print(count)
        count = count - 1
        return
print("Blastoff!")













