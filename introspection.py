my_var = "This is a varaible"
my_num = 453.153

class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

myHero = Hero("My name", 45)

#check available methods

print("get id, type and available methods and attributes for Hero Class")
print(id(myHero))
print(type(myHero))
print(dir(myHero))

print("get id, type and available methods and attributes for string value")
print(id(my_var))
print(type(my_var))
print(dir(my_var))

print("get id, type and available methods and attributes for integer value")
print(id(my_num))
print(type(my_num))
print(dir(my_num))
