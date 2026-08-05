# 2 types of Loops: For and While

# For Loops for looping a specific NUMBER of time

# Example 1
nums = [5, 4, 3, 2, 1]

for num in nums:
    print(num)
print("Blastoff!")


# Example 2
fruits = ["apple", "banana", "orange", "pear"]

for fruit in fruits:
    print(f"I love to eat {fruit}!")


# Example 3 (Optional bc. HARD)
fruits = ["apple", "banana", "orange", "pear"]

i = 0

for fruit in fruits:
    print("Item", i, "->", fruit)
    i = i + 1



# While Loops for looping UNTIL a CONDITION is met

# Example 1
count = 1

while count <= 3:
    print("Count is:", count)
    count = count + 1

# Example 2
timer = 3

while timer > 0:
    print(timer)
    timer = timer - 1

print("Blastoff!")
