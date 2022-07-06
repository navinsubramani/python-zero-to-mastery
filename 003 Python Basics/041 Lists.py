# In python, lists is a form of array.

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = ['a', 'b']
li3 = [1, 2, 'c']

# list unpacking
a, b, c, * other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(li3[0])
# print(li3[2])

# list slicing

print(li1[0:8:2])
li1[0] = -1
print(li1[0:8:2])

# When slicing, a new memory is created.

li4 = li1[0:8:2]
print(li4)
print(li1)

# when assigning, the list points the array memory to another variable

li4 = li1
li4[0] = -100
print(li4)
print(li1)
