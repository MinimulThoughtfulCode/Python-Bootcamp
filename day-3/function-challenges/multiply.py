#Multiply Machine
#Function multiplies two numbers

def multiply(a, b):
  #Multiplies
  calculation = a * b
  return calculation

#Takes user input
first = int(input("What is the first number: "))
second = int(input("What is the second number: "))

#Finds the answer
answer = multiply(first, second)
print(first, "multiplied by", second, "equals to", answer)
