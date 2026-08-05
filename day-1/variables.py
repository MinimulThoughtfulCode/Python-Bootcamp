# Variables are names in place of data and values

x = 12.2
y = 15

# Use mnemonic names for variables, BAD to start with a number, sign, nor other characters

# 3 Types: String, Integers, Float-Point

str = "Hello, World"
int = 20
float = 98.4

# You can convert between values if they allow

str = "20"
int = int(str)
print(int + 5) # int() converts a float or string variable into a numerical value that can be used for math


int = 20
string = str(int)
print("I like the number " + string + ".") # str() converts an integer or a float number into a string used in combining lengths of texts

int = 20
float = float(int)
sum = float + 25.9
print(sum)  # float() converts an integer ONLY to a decimal number, which can be used in appropriate circumstances.
