dictionary = {'a': 1, 'b': 2, 'c': [1, 2, 3],
              1001: 'Thousand and One', True: 'One'}
# print(dictionary[True])
# print(dictionary['a'])
# print(dictionary[1001])
# print(dictionary['c'][2])

print(dictionary.get('d', 4))

oxford = dict(name='navin')
print(oxford)

print(1001 in dictionary)
print(1001 in dictionary.keys())
