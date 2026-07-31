#Fortune Teller
#Build a simple function that takes a user's name and prints out that they will win a prize today!

def predict(name):
  #Tells the fortune
  print(name, ", you will win a prize today!")

#Takes user's name
name = str(input("What is your name: "))

#Runs the function
predict(name)
