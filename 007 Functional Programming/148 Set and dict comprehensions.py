# create a set of char from a string using compreshensions
name = 'navin'

my_name = {char for char in name}
print(my_name)

# on dictionary

simple_dict = {'a': 1, 'b': 2}
print({key: value*2 for key, value in simple_dict.items()})

# convert the list into a dict where key = item, value = item*2
li = [1, 2, 3, 4]
print({x: x*2 for x in li})
