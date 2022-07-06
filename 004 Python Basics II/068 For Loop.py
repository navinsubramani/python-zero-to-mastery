# for loop
# iterable - list, dictionary, tuple, set, string

b = '123'
for a in b:
    print(a)

b = (1, 2, 3)
for a in b:
    print(a)

b = [1, 2, 3]
for a in b:
    print(a)


user = {'name': 'Rick', 'age': 35, 'country': 'usa'}

for a in user:
    print(a)
for a in user.keys():
    print(a)
for a in user.values():
    print(a)
for a in user.items():
    print(a)
for a, b in user.items():
    print(a, b)
