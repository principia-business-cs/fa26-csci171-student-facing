price = float(input('Price: '))
quantity = int(input('Quantity: '))
discount = float(input('Discount as decimal: '))
subtotal = price * quantity
savings = subtotal * discount
print('Subtotal:', subtotal)
print('Savings:', savings)
print('Total:', subtotal - savings)
