#Movie Ticket Calculator
#Determines the ticket price based on the customer's age and whether they have a discount card

#Takes user input
age = int(input("How old are you: "))
discount = input("Do you have a discount card: ")

#Checks if user has a discount card
if discount == "yes":
  has_discount = True
else:
  has_discount = False

if age >= 65 or age <= 18:
  #Set student/senior discount
  ticket_price = 7

elif has_discount:
  #Set discount
  ticket_price = 9

else:
  #Set default price
  ticket_price = 12

#Print out the final price of the ticket
print("Ticket Price:", ticket_price)


# Review on Booleans
correct_password = "sunshine123"
attempts_left = 3
logged_in = False   # starts as False because we haven't logged in yet

while attempts_left > 0 and logged_in == False:
    entered_password = input("Enter password: ")

    if entered_password == correct_password:
        logged_in = True
        print("Access granted!")
    else:
        attempts_left = attempts_left - 1
        print("Wrong password. Attempts left:", attempts_left)

if logged_in == True:
    print("Welcome in!")
else:
    print("Account locked. Too many wrong attempts.")
