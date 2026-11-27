# 1. Ask for a number and print its times table from 1 to 10, like 7 x 3 = 21.

user_input = int(input("Please enter the number of which you want to see the table: "))

for count in range (1, 11):
    print(f"{user_input} X {count} = {user_input * count}")


# 2. Add up all the numbers from 1 to 100 with a for loop and a running total. Check: the answer is 5050.

num = 0

for i in range (1, 101):
    num = num + i
print(f"Check: the answer is {num}")

# 3. Ask for a word and count how many vowels (a, e, i, o, u) it has. Hint: for letter in word:, then if letter in "aeiou":. The word in also checks whether something is inside a string. For "education" the answer is 5.

count = 0

user_input = input("Please enter a word of which you want to count vowels of: ")

for letter in user_input.lower():

    if letter in "aeiou":
        count = count + 1
print(f"Vowels: {count}")
