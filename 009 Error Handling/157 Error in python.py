# https://docs.python.org/3/library/exceptions.html

# error handling in python

from ast import Pass


while True:
    try:
        age = int(input('what is your age? '))
        div = 10/age
        # raise Exception('This is how we raise user errors')

    except (ValueError, ZeroDivisionError) as err:
        print('Error: please enter a valid number...' + str(err))

    else:
        print(f'Your age is : {age}')
        break

    finally:
        print('I\'m finally done')
