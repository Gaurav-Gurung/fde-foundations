# -------------- Functions ------------------------------#

def add_gst(amount):
    total = amount *1.18
    return total



def is_adult(age):
    if age<18:
        return False
    else:
        return True

def rectangle_area(length, width):
    area = length * width
    return area


def add_gst(amount):
    total = amount *1.18
    return total

# 1. Fill in the blanks


price = float(input("Price: "))
final = add_gst(price)
print(final)

# 1.  Like Step C: is_adult(age) returns True for 18 or more, else False. print(is_adult(17)) → False; print(is_adult(18)) → True.


user = int(input("Enter age: "))
result = is_adult(user)
print(f"You are an adult? - {result}")

# 2.  Like Step D: rectangle_area(length, width) returns the area. Ask the user for both. 12 and 10 → 120.0.


while True:
    user_input = int(input("Please type 1 to find the area or 0 to quit: "))
    if user_input == 0:
        print("Goodbye!")
        break
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    total_area = rectangle_area(length, width)
    print(f"The total area is: {total_area}")

    

# 3.  Like Step E: a café loop that asks for prices until 0, uses add_gst() on each, 
#     and prints the number of items and the grand total once at the end. 100, 200, 0 → 2 items, 354.0.


count = 0
g_total = 0

print("Welcome to the gst calculator!")

while True:
    user_input = int(input("Type 1 to find the gst included price or 0 to quit: "))
    if user_input == 0:
        print("Goodbye!")
        break
    if user_input != 1:
        print("Please type 1 or 0.")
        continue
    amount = float(input("Please enter the amount: "))
    gst_amount = add_gst(amount)
    count = count + 1
    g_total = g_total + gst_amount
    print(f"Price with 18% GST: {gst_amount:.2f}")
print(f"Items: {count}, grand total incl. GST: {g_total:.2f}")

