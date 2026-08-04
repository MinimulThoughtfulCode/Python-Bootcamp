is_logged_in = True
has_permission = False


if is_logged_in:
    print("Welcome back to your dashboard!")
else:
    print("Please log in first.")



user_age = 16
age_limit = 18

can_vote = user_age >= age_limit  

if can_vote:
    print("You are eligible to vote!")
else:
    print("You are not old enough to vote yet.")
