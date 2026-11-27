# 1. Number adder

total = 0
count = 0

while True:
    user_input = int(input("Please enter a number or type 0 to quit: "))

    if user_input == 0:
        print("Program closed.")
        break
    
    total = total + user_input
    count = count + 1
print(f"The number of times numbers were added is {count}, and the total is {total}")


# 2. The full gym program, your cold test:

count = 0
amount = 0

while True:
    user_input = input("Please type y to purchase the subscription or q to quit: ")
    
    if user_input == "q":
        print("See you again!")
        break
    elif user_input == "y":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        month = int(input("Enter the number of months you want to subscribe for: "))
        calc = month * 1000
        discount = calc * 0.8
        
        if age <18:
            print("Sorry under age.")
        elif age <60:
            count = count + 1
            amount = amount + calc
            print(f"Your total subscription fee is {calc}.")
        else:
            count = count + 1
            amount = amount + discount
            print(f"We provide discounts to people who are 60+ with an instant 20% discount so your total subscription fee is {discount}.")  
    else:
        print("Please type y or q")
print(f"Total subscribers are {count} and total amount collected is {amount}.")  