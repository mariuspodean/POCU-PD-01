
#Decorator to uppercase result 

def uppercase(fnc):

    def wrapper(name):
    
        initial_text = fnc(name)
        upper_text = initial_text.upper()

        return upper_text
    return wrapper

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

test = greet('test')
print(test)


#Decorator for division

def safe_divide(fnc):

    def wrapper(first_number, second_number):
        try:
            first_number % second_number
        except TypeError:
            return "One or both inputs is not a number!"

        if(first_number % second_number == 0):
             division_result = fnc(first_number, second_number)
        else:
            division_result = "Numbers cannot be divided to another integer."
        return division_result
    return wrapper

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

divided = divide("s", 2)
print(divided)


#Decorator to update print_registry with the function names

print_registry = []

def register(fnc):
    fnc_name = fnc.__name__

    def wrapper(name):
        print_registry.append(fnc_name)
        return fnc(name)
    return wrapper


@register
def greetings(name):
    return "Greetings {}!".format(name)

@register
def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

greetings('whatever')
say_hello('whatever else')
say_goodbye('running out of ideas')
print(print_registry)


