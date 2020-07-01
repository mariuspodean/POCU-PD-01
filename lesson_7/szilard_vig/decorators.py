def join_args(args):
    return ','.join(repr(arg) for arg in args)

#Create a decorator calleduppercasethat will uppercase the result
def uppercase(fnc):
    fnc_name = fnc.__name__
    print('Decorating function {}'.format(fnc_name))
    def inner(*args):
        print('Decorated function {} got the following args: {}'.format(fnc_name, join_args(args)))
        text = fnc(*args)
        return text.upper()
    return inner

@uppercase
def greet1(name):
    return "Greetings {}!".format(name)

print(greet1('Earhling'))

print('-'*20)
#Create a decorator called safe_divide that will output a message if the division cannot be per-formed, othervise it will return the result.
def safe_divide(fnc):
    fnc_name = fnc.__name__
    print('Decorating function {}'.format(fnc_name))
    def inner(first_number, second_number):
        try:
            return first_number / second_number
        except:
            return 'Division can not be performed'
    return inner

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

number1 = 10
number2 = 3
number3 = 0
print(f'{number1} / {number2} = {divide(number1, number2)}')
print(f'{number1} / {number3} = {divide(number1, number3)}')
    
print('-'*20)
#Create a decorator called register that will update a list calledprint_registrywith all thedecorated functions names.

print_registry=[]
    
def register(fnc):
    fnc_name = fnc.__name__
    print('Decorating function {}'.format(fnc_name))
    def inner(*args):
        print('Decorated function {} got the following args: {}'.format(fnc_name, join_args(args)))
        print_registry.append(fnc_name)
    return inner

@register
def greet(name):
    return "Greetings {}!".format(name)
    
def say_hello(name):
    return "Hello {}!".format(name)
    
@register 
def say_goodbye(name):
    return "Goodbye {}!".format(name)


say_goodbye('to Hollywood')
greet('Master')
    
print('print_registry has been updated to: ', print_registry)