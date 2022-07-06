my_age = 10

if my_age < 10:
    print('I\'m a kid')

elif 10 <= my_age and my_age < 20:
    print('Teenage')

elif 20 <= my_age < 30:
    print('Adult')

else:
    print('I\'m an grown up')


# Truthy and Falsy : Conditions evaluates any data to see if they are truthy or falsy

name = 'a'

if name:
    print('nice name')
else:
    print('empty name')
