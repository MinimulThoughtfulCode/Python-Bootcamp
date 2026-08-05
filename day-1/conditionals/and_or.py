age = 15
is_student = True
day_of_week = "Tuesday"

if age < 12 or age >= 65:
    ticket_price = 5.00
    category = "Senior / Child Discount"

elif is_student and (day_of_week == "Tuesday" or day_of_week == "Wednesday"):
    ticket_price = 7.00
    category = "Mid-week Student Discount"

else:
    ticket_price = 12.00
    category = "Standard Ticket"

print(f"Day: {day_of_week}")
print(f"Category: {category}")
print(f"Ticket Price: ${ticket_price:.2f}")
