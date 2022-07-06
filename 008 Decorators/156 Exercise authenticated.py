# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrap_fn(*args, **kwargs):
        if args[0].get('valid') == True:
            result = fn(*args, **kwargs)
            return result
    return wrap_fn


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
