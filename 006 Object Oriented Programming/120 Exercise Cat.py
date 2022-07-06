class cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_oldest_cat(*args):
    old_age = 0
    old_cat = ''
    for n in args:
        if old_age < n.age:
            old_age = n.age
            old_cat = n
    return old_cat


tom = cat('tom', 10)
mike = cat('mike', 15)
john = cat('john', 18)

old_cat = find_oldest_cat(tom, mike, john)
print(f'The oldest cat is {old_cat.name} and it is {old_cat.age} years old.')
