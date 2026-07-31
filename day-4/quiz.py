#Text based quiz game
#Asks Python related questions to the user like a trivia game

#Variables
count = 0

#Question 1
print("Which keyword is used to define a function in Python?")
print("A) func")
print("B) define")
print("C) def")
print("D) function")
question1 = str(input("Answer: "))

if question1 == "C":
  print("Correct!")
  count = count + 1
else:
  print("Incorrect!")


#Question 2
print("What is the correct way to output text in Python?")
print("A) print('Hello')")
print("B) echo('Hello')")
print("C) system.out.print('Hello')")
print("D) display('Hello')")
question2 = str(input("Answer: "))

if question2 == "A":
  print("Correct!")
  count = count + 1
else:
  print("Incorrect!")


#Question 3
print("Which data type is used to store text in Python?")
print("A) int")
print("B) str")
print("C) float")
print("D) boolean")
question3 = str(input("Answer: "))

if question3 == "B":
  print("Correct!")
  count = count + 1
else:
  print("Incorrect!")

#Score revealed
print("You got", count, "out of 3 correct!")
if count == 3:
  print("Congratulations")
else:
  print("Keep trying")
