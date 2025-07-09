# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# 1.	If the number is a multiple of 4, print out a different message.
# 2.	Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number: "))
result = "even" if num % 2 == 0 else "odd"
print(f"The number {num} is {result}.")

#extra 1
print("The number is a multiple of 4." if num % 4 == 0 else "The number is even." if num % 2 == 0 else "The number is odd.")


#extra 2
num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}.")
else:
    print(f"{check} does NOT divide evenly into {num}.")
