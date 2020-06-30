b = 15
def read_variables(a):
    global b
    print(a)
    print(b)
    # local variable b
    b = 25
read_variables(5)