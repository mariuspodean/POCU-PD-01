# Create a decorator called uppercase that will uppercase the result
 
def decorator_uppercase(my_function):

    def inner_uppercase(*arg):
        return my_function(*arg).upper()
    return inner_uppercase

@decorator_uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet('World'))

# 2. Given the following function:
# def divide(first_number, second_number):
#      return first_number / second_number
# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.