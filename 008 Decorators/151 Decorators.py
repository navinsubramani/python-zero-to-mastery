# In python, functions are first class citizens like the variables

# Higher order function either accepets a function as input or returns the function as output

def greet(func):
    print('hellloooooo')
    func()


def name():
    print('David')


greet(name)

# Decorators


def my_decorator(func):
    def wrap_func():
        print('super boost the method')
        func()
        print('Added functionality')
    return wrap_func


@my_decorator
def greet():
    print('heloooooo')


greet()
