# sum the number in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for num in my_list:
    sum = num+sum

print(sum)

# using range: range output special type of object called 'Range'

print(range(100))
print(range(0, 10, 2))
print(range(10, 0, -2))
print(list(range(0, 10, 2)))

# enumerate: takes the iterable data and enumerate the item index and the value at the index
print(enumerate('Helloooo'))

for i, num in enumerate([100, 200, 300, 400, 500]):
    print(i, num)

# enumerate such that only the index of 50 is displayed
result = -1
for i, num in enumerate(list(range(100))):
    result = num if i == 50 else result
print(result)
