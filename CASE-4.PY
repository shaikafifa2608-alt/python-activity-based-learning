price1 = float(input("Price of product 1: "))
quantity1 = int(input("Quantity of product 1: "))
price2 = float(input("Price of product 2: "))
quantity2 = int(input("Quantity of product 2: "))
subtotal = price1 * quantity1 + price2 * quantity2
if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0
final_amount = (subtotal - discount) * 1.05
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final amount with tax:", final_amount)
