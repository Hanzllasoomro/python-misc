# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# •	Keep the game going until the user types “exit”
# •	Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 9 (or type 'exit' to quit).")

# Generate a random number between 1 and 9
number = random.randint(1, 9)
guess_count = 0

while True:
    user_input = input("Your guess: ")

    if user_input.lower() == "exit":
        print(f"You exited the game after {guess_count} guess(es).")
        break

    if not user_input.isdigit():
        print("Please enter a valid number or 'exit'.")
        continue

    guess = int(user_input)
    guess_count += 1

    difference = abs(guess - number)

    if difference == 0:
        print(f"Exactly right! 🎉 It took you {guess_count} guess(es).")
        break
    elif difference >= 5:
        print("Way too low!" if guess < number else "Way too high!")
    elif difference >= 3:
        print("Too low!" if guess < number else "Too high!")
    else:
        print("Very close! Just a bit too low!" if guess < number else "Very close! Just a bit too high!")

