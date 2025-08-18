import random

num = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))

if guess == num:
    print("Correct! You guessed it.")
else:
    print(f"Wrong! The number was {num}")
