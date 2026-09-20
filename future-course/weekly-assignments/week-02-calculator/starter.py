print("Friendly Calculator Starter")

price = float(input("Item price: "))
quantity = int(input("Quantity: "))
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal:", round(subtotal, 2))
print("Tax:", round(tax, 2))
print("Total:", round(total, 2))
