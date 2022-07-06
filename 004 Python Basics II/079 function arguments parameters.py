# function definition contains the parameters
# Default Parameters
def say_hello(name, emoji=':P'):
    print('Hellloooo '+name + ' ' + emoji)


# Arguments is the actual value provided to the function calls
say_hello('Matt')

# positional arguments
say_hello('Matt', ':)')

# Keyword arguments
say_hello(name='Kevin', emoji=':D')
