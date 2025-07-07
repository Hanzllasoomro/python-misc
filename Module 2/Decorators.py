def extract_function_name(function):
    def internal_method(*args, **kwargs):
        print("The method is called :" ,function.__name__)
        returned_value = function(*args, **kwargs)
        print("The return value is", returned_value)
        return returned_value
    return internal_method

@extract_function_name
def sum_nums(num1, num2):
    print("This is sum_num insied the extract_function_name")
    return num1 + num2

@extract_function_name
def product(num1, num2):
    print("This is product insied the extract_function_name")
    return num1 * num2

a, b = 3, 4

print("Sum function value: ",sum_nums(a, b))
print("Product function value: ",product(a, b))
