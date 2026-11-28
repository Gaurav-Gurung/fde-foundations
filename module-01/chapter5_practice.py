# 1.  Print every even number from 2 to 20 using range with a step.

for skip in range (2, 21, 2):
    print(skip)

# 2.  Ask for a sentence and count how many spaces it has, then print the number of words (spaces + 1).

gaps = 0

user_input = input("Please type a sentence: ")

for letter in user_input:
    if letter == " ":
        gaps = gaps + 1
print(f"letters: {gaps}, Words: {gaps + 1}")

# 3.  Countdown: print 10 down to 1, then "Lift off!". Hint: range(10, 0, -1).


for count in range (10, 0, -1):
    print(count)
print("Lift off!")