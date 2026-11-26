
print("Welcome to bill by py!")

item_name = input("Please enter the item name: ")
item_price = float(input("Please enter the price of the item: "))
item_qty = int(input("Please enter the item quantity: "))
item_total = item_price * item_qty
with_gst = item_total*1.18 

print(f"The total amount of {item_qty} x {item_name} is {item_total} and with gst its {with_gst}.")


