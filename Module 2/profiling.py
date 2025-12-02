import cProfile

def internalMethod():
    temp = 0
    for i in range(100):
        temp += i
    return temp

def externalMethod():
    temp = 0
    for i in range(100):
        temp += internalMethod()
    print("total iterations: ", temp)
    return

cProfile.run("externalMethod()")