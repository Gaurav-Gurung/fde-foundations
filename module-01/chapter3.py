# Task 1

age = int(input("Please enter your age: "))

if age <13:
    print("Child")
elif age<=17:
    print("Teen")
elif age<=59:
    print("Adult")
else:
    print("Senior") 

# Task 2

username = "Gaurav"
password = "fde2026"

user_input_username = input("Please enter the username: ")
user_input_password = input("Please enter the password: ")

if user_input_username == username and user_input_password == password:
    print("Welcome!")
else:
    print("Access Denied.")

# Task 3

age = int(input("Enter your age: "))
months = int(input("Enter months: "))
fees = 1000
bill_calculation = months * fees
discounted_price_SS = bill_calculation*0.80

if age <18:
    print("Sorry Access denied.")
elif age >= 18 and age <= 59:
    print(f"Your fees is {bill_calculation}.")
else:
    print(f"You are a senior citizen your actual bill is {bill_calculation} but since you are a senior citizen we are providing a discount of 20% and now your final bill is {discounted_price_SS}.")