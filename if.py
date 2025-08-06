price = 55000
if price > 50000:
    # noinspection PyRedeclaration
    off = 0.2
elif price in range(2001, 50001):
    off = 0.1
else:
    off = 0

print(f"Discount: {off*100}%")
print(f"Price after discount: {price - price*off}")


