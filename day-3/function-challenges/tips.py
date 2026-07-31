#Tip Calculator
#Function returns a tip amount

def tip(n):
  #15% tip on top of the total
  answer = n * 1.15
  return answer

#Takes user input
amount = int(input("What is the amount: "))

#Finds total
total = tip(amount)
print("Your total is:", total)
