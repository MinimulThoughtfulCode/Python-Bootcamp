#Random Item Picker
#Function randomly picks an object for the user

import random

#Takes User input
name = input("Enter your name: ")

#Sets the objects
tools = ["Bottle", "Keyboard", "Football", "Car"]

def get_random_object(items):
  #Randomly chooses an object
  chosen = random.choice(items)
  return chosen

#Gets an object chosen
result = get_random_object(tools)
print("Welcome", name, "! Your random object is:", result)
