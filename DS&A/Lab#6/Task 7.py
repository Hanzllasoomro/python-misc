for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Multiple of both 3 & 5")
    elif i % 3 == 0:
        print("Multiple of 3")
    elif i % 5 == 0:
        print("Multiple of 5")
    else:
        print(i)
