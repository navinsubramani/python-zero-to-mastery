from functools import reduce
from hashlib import new

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def string_capitalize(input):
    return input.upper()


print(list(map(string_capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(sorted(list(zip(my_strings, my_numbers)), key=lambda x: x[1]))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def ispass(input):
    return input > 50


print(list(filter(ispass, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def sum(acc, num):
    return acc+num


new_numbers = my_numbers
for n in scores:
    new_numbers.append(n)

print(reduce(sum, new_numbers, 0))
