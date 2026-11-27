# 1. What does input() always return? How do you turn it into a whole number, and into a decimal?
# 2. The rules for if / elif / else: which one takes a condition, which doesn't, and what does "the first True wins" mean?
# 3. Why does age >= 18 and <= 59 fail? Write the correct version.
# 4. The gym bill decision without a loop: ask age and months, then sorry for under 18, full price for 18–59, and 20% off for 60+.

# Answers

# 1. input() always returns a string after a user enters something. We turn anything into a number or a whole number by using int and for decimal we will use float()  
# 2. if takes the condition, else, if the first rue wins then it prints the things that we have mentioned in the first condition
# 3. The first one age >=18 fails because <= 59 already covers anything below 59 unless we want to present something else below 18 and also it doesn't have the age variable I forgot the exact term name but it will show an error because <=59 doesn't have age beside it. 

# I'm just going to add the same condion given by you but I'd write it differently.

# age = int(input("Please enter your age: "))  

# if age >=18 and age <=59:
#     print("Hi person!")

# 4. age = int(input("What's your age?: "))
#    months = int(input("For how many months do you want to subscribe for?: "))
#    if age <18:
#       print("Sorry")
#    elif age <=59: 
#       print("Full Price")
#    else:
#       print("20% off for 60+")    

# The above is exactly coded for how you gave me but price per month is not mentioned so here is how I'd do it:

#    age = int(input("What's your age?: "))
#    months = int(input("For how many months do you want to subscribe for?: "))
#    monthly_fee = 1000   
#    normal_sub = months*monthly_fee
#    disc = normal_sub*0.8
#    if age <18:
#       print("Sorry")
#    elif age <=59: 
#       print(f"Your subscipiton total is {normal_sub}")
#    else:
#       print(f"20% off for 60+ so your subscription total is {disc}")   