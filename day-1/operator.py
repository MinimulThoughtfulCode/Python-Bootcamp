balance = 50.00
transaction = "deposit"  # Options: "deposit", "withdrawal", "interest"
amount = 25.00

# 2. Update the balance using basic operators
if transaction == "deposit":
    # Add money to the balance
    balance = balance + amount
    print(f"Deposited ${amount:.2f}")

elif transaction == "withdrawal":
    # Check if there is enough money before subtracting
    if balance >= amount:
        balance = balance - amount
        print(f"Withdrew ${amount:.2f}")
    else:
        print("Insufficient funds!")

elif transaction == "interest":
    # Multiply balance by 1.05 (add 5% interest)
    balance = balance * 1.05
    print("5% interest added!")

# 3. Print the updated balance
print(f"Updated Balance: ${balance:.2f}")
