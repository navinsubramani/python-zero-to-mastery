# Square the list
my_list = [5, 4, 3]

print(list(map(lambda x: x*x, my_list)))

# List sorting based on second element

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(sorted(a, key=lambda x: x[1]))
