# 1.  Keep asking for expenses until the user types 0. Then print how many expenses, the total, and the average (total ÷ count).

count = 0
total = 0
average = 0

while True:
    user_input = float(input("Please type the amount to add an expense or 0 to quit: "))

    if user_input == 0:
        print("Goodbye!")
        break
    count = count + 1
    total = total + user_input
    average = total/count 
print(f"Your total number of expenses are {count}, the total amount is {total}, and the average is {average}.")





# 2.  A PIN check: the correct PIN is 4321. Allow at most 3 tries; print "Unlocked" on a correct try, or "Locked" after 3 wrong ones.

pin = "4321"
pin_try = 0

while True:
    user_input = input("Please enter the password: ")
    pin_try = pin_try + 1

    if user_input == pin:
        print("Unlocked")
        break
    elif pin_try == 3:
        print("Locked")
        break
    else:
        print("Try again.")
    
    


    