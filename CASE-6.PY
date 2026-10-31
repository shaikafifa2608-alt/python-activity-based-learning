balance = float(input("Balance: "))
kind = input("D for deposit, W for withdrawal: ")
amount = float(input("Amount: "))
if kind == "D":
    balance = balance + amount
    print("Deposit accepted")
elif kind == "W" and amount <= balance:
    balance = balance - amount
    print("Withdrawal accepted")
else:
    print("Transaction rejected")
print("Final balance:", balance)
