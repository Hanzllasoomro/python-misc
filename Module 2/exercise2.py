import math
from functools import wraps

def logger(operation):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"operation: {operation}")
            print(f"Inputs: {args[1:]}")
            result = func(*args, **kwargs)
            return "Result: " , result
        return wrapper
    return decorator

class Calculator:
    @logger("Addition")
    def add(self, a, b):
        return a+b

    @logger("Subtraction")
    def sub(self, a, b):
        return a - b

    @logger("Multiplication")
    def mul(self, a, b):
        return a *  b

    @logger("Division")
    def div(self, a, b):
        if b == 0:
            return "Undefined"
        return a / b

class ScientificCalculator(Calculator):

    def __init__(self):

        self.log = lambda x, base = math.e: math.log(x, base)
        self.power = lambda x, y : x ** y
        self.exponential = lambda x: math.exp(x)
        self.factorial = lambda x: math.factorial(x)

    @logger("Logarithm")
    def log(self, x, base = math.e):
        return self.log(x, base)

    @logger("Exponential")
    def exp(self, x):
        return self.exponential(x)

    @logger("Factorial")
    def factorial(self, x):
        return self.factorial(x)

    @logger("Power")
    def pow(self, x, y):
        return self.power(x, y)

if __name__ == "__main__":
    calculator = ScientificCalculator()
    print(calculator.add(1, 2))
    print(calculator.sub(5, 2))
    print(calculator.mul(5, 2))
    print(calculator.div(5, 2))
    print(calculator.log(5, 2))
    print(calculator.exp(5))
    print(calculator.factorial(5))
    print(calculator.pow(5, 2))

