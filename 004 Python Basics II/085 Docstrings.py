def welcome(name):
    '''
    Info: This functions prints 'Welcome <name>' in the console 
    '''
    print(f'Welcome {name}')


welcome('Jack')

# doc string can retrieved by using help(method)

help(welcome)

# or

print(welcome.__doc__)
