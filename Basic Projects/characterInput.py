# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# 1.	Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2.	Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import datetime

# Main inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate the year when the user will turn 100
current_year = datetime.now().year
year_turn_100 = current_year + (100 - age)

# Create the message
message = f"Hey {name}, you will turn 100 years old in the year {year_turn_100}."

# Print the main message
print(message)

# Extras
copies = int(input("Enter a number of times to print this message: "))

# Print multiple copies on separate lines
print((message + "\n") * copies)
