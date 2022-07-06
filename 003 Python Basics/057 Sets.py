# unordered collection of unique objects


my_sets = {1, 2, 3, 4, 5, 5, 5}
print(my_sets)

my_sets.add(100)

print(my_sets)

# example: take a list and find out the unique elements
my_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
my_sets = set(my_list)
print(my_sets)
