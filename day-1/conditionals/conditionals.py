# Example 1
score = 85

if score >= 90:
    grade = "A"
    message = "Outstanding performance!"
elif score >= 80:
    grade = "B"
    message = "Great job!"
elif score >= 70:
    grade = "C"
    message = "Good effort, keep practicing!"
elif score >= 60:
    grade = "D"
    message = "You passed, but review the material."
else:
    grade = "F"
    message = "Don't give up! Let's try again."

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Feedback: {message}")



# Example 2
age = 16

if age >= 18:
    access = "Full Access"
    status = "Adult account created."
elif age >= 13:
    access = "Teen Access"
    status = "Teen account created with parental consent options."
else:
    access = "Restricted Access"
    status = "Kids account created. Parental guidance required."

# 3. Output the result
print(f"User Age: {age}")
print(f"Access Level: {access}")
print(f"Status: {status}")
