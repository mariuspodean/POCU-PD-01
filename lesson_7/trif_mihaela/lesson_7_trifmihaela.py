# Create a decorator called uppercase that will uppercase the result
 
def decorator_uppercase(my_function):

    def inner_uppercase(*arg):
        return my_function(*arg).upper()
    return inner_uppercase

@decorator_uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet('World'))

# 2. # Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.
def decorator_safe_divide(my_function):

    def inner_safe_divide(*args):
        if my_function(*args) is None:
            print('The divizion cannot be preformed')
        return my_function(*args)
    return inner_safe_divide

@decorator_safe_divide
def divide(first_number, second_number):
     return first_number / second_number

print(divide(12,15))
# 3.Create a decorator called register that will update a list called print_registry with all the decorated functions names.
def register(my_function):
    
    def inner_registry(*args):
        my_function_name = my_function.__name__
        return my_function_name

    return inner_registry

print_registry = []
@register
def greet(name):
    return "Greetings {}!".format(name)
print_registry.append(greet())

def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)
print_registry.append(say_goodbye())

print(print_registry)



