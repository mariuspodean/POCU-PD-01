#1

def uppercase(func):
    def inner_uppercase(name):
        text = func(name)
        upp_case = text.upper()
        return upp_case
    return inner_uppercase


@uppercase

def greet(name):
     return "Greetings {}!".format(name)

print(greet("World"))

#2

def dec_safe_divide(func):
    def inner_safe_divide(first_number, second_number):
        if func is None:
            print('Opperation cannot be performed')
        return func(first_number,second_number)
    return inner_safe_divide


def divide(first_number, second_number):
    return first_number / second_number

print(divide(12,2))

#3

def register(func):
    func_name = func.__name__

    def inner_register(name):
        #print_registry.append(func_name)
        return func(name)
    return inner_register

print_registry = []

@register
def greet(name):
    return "Greetings {}!".format(name)

@register
def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print_registry.append(greet('aaa'))
print(print_registry)

print_registry.append(say_hello('aaa'))
print(print_registry)

print_registry.append(say_goodbye('aaa'))
print(print_registry)