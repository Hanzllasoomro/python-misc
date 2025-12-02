import inspect
import os

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
exp = lambda x: x*x

def show_name_age(first_name:str, last_name:str, age:int):
    print("{} {} is {} years old".format(first_name, last_name, age))

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

inspect.getmembers(myHero) #returns the members of the class myHero
print("\nChecking if os is a module:", inspect.ismodule(os))
print("\n ISMETHOD: \nshow_name_age:", inspect.ismethod(show_name_age), "exp:", inspect.ismethod(exp), "myHero.say_hi:", inspect.ismethod(myHero.say_hi))
#signature of a method access parameters, their inferred or fixed data types
sig = inspect.signature(show_name_age)
print(sig.parameters) #return a dictionary with parameter names as key and description as values
print(sig.parameters["first_name"].annotation) # print the type of this parameter
print(sig.return_annotation)
