#Find the Biggest Number
#Function returns the larger number

def number(a, b):
  #Function checks which number is bigger
  if a > b:
    print("The first number is bigger")
  
  elif a < b:
    print("The second number is bigger")

  else:
    print("Both are equal")

a = int(input("What is the first number: "))
b = int(input("What is the second number: "))

number(a, b)
