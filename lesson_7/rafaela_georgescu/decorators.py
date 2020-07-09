### 1 ###
def uppercase(func):
    func_name = func.__name__
    print('Decorating {} function'.format(func_name))
    def inner_function(*args):
        result = func(*args)
        return result.upper()
    return inner_function

@uppercase
def greet(name):
    return "Greetings, {}!".format(name)

### 2 ###
def self_divide(func):
    func_name = func.__name__
    print('Decorating {} function'.format(func_name))
    def inner_function(first_number, second_number):
        try:
            return round(first_number / second_number, 2)
        except ZeroDivisionError:
            print('You can not divide by zero')
    return inner_function

@self_divide
def divide(first_number, second_number):
    return first_number / second_number

### 3 ###
print_registry = []

def register(func):
    func_name = func.__name__
    print('Decorating {} function'.format(func_name))
    def inner_function(*args):
        print_registry.append(func_name)
        return func(*args)
    return inner_function

@register
def second_greet(name):
    return "Greetings, {}!".format(name)

def say_hello(name):
    return "Hello, {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye, {}!".format(name)

### 1 ###
# Uppercase the result
print(greet('Marius'))
print(greet('George'))

### 2 ###
first_number = 156
second_number = 23
print("{} / {} = {}".format(first_number, second_number, divide(first_number, second_number)))
first_number = 121
second_number = 0
print("{} / {} = {}".format(first_number, second_number, divide(first_number,second_number)))

### 3 ###
print(second_greet('Traveler'))
print(say_hello('Stranger'))
print(say_goodbye('Weird'))
print(print_registry)