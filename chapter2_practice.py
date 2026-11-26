# Test 1

length = float(input("Please enter the length of the room in feet: "))
width = float(input("Please enter the width of the room in feet: "))
area = length*width

print(f"The total area of the room is {area} sqft.")


# Test 2

total_bill = float(input("Please enter the final bill amount: ")) 
number_of_people = int(input("Please enter the number of people you want to split the bill with: "))
split_amount = round(total_bill / number_of_people, 2)
whole_amount = total_bill // number_of_people
remainder = total_bill % number_of_people
print(f"Each person has to pay {split_amount}. The whole amount each one has to pay is {whole_amount}, and the remaining is {remainder}.")