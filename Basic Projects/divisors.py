# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

try:
    number = int(input("Enter a number to find its divisors: "))
    divisors = find_divisors(number)
    print(f"Divisors of {number}: {divisors}")
except ValueError:
    print("Please enter a valid integer.")
