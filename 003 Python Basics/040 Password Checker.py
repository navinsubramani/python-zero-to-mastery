# this is a password checker assignment

user_name = input('Username: ')
password = input('Password: ')

display_password = len(password) * '*'

print(f'Your username is : {user_name}')
print(
    f'Your password is {display_password} and it is {len(password)} letter long')
