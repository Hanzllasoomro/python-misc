# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# 1.	Randomly generate two lists to test this
# 2.	Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = list(set(a) & set(b))  # Set intersection removes duplicates
print(f"Common elements: {common}")

#extra 1
import random

a = random.sample(range(1, 50), 10)  # 10 unique random numbers between 1–49
b = random.sample(range(1, 50), 15)  # 15 unique random numbers

print(f"List A: {a}")
print(f"List B: {b}")
print(f"Common elements: {list(set(a) & set(b))}")

#extra 2
print(list(set(a) & set(b)))
