#Secret Word Challenge
#The function should check if the user guesses the secret word


#Sets the secret word
secret = "Python"
run = True

#Asks for user input
guess = str(input("Enter your guess: "))

if guess == secret:
  #Correct Guess!!!
  print("You guessed the right word!")

else:
  #Incorrect Guess
  print("You guessed the wrong word!")

  while run:
    #Keep guessing until its correct
    new_guess = str(input("Enter your guess: "))
  
    if new_guess == secret:
      print("You guessed the right word")
      run = False

    print("You guessed the wrong word!")
