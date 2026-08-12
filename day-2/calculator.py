print("Calculator")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

operation = input("Enter operation (+, -, *, /): ")
print("")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Error: Invalid operation. Please use +, -, *, or /.")
