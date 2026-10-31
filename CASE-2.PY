units = float(input("Enter units: "))
if units < 0:
    print("Units cannot be negative")
elif units <= 100:
    bill = units * 1.5 + 50
    print("Bill:", bill)
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5 + 50
    print("Bill:", bill)
elif units <= 300:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4 + 50
    print("Bill:", bill)
else:
    bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6 + 50
    print("Bill:", bill)
