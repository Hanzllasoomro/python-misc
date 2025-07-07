def powerRaiser(n):
      return lambda x : x**n

square = powerRaiser(2)
cube = powerRaiser(3)
quad = powerRaiser(4)

inputNumber = 3
print("input is: ", inputNumber)
print("square is: ", square(inputNumber))
print("cube is: ", cube(inputNumber))
print("quadratic is: ", quad(inputNumber))