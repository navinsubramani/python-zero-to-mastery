# *args and **kwargs can be used with any name like *hoo, but the standard is to use *args

def sum_all(*args, **kwargs):
    total = 0
    # kwargs are dictionary
    for item in kwargs.values():
        total += item
    # arge are tuple
    return sum(args) + total


print(sum_all(1, 2, 3, 4, 5, n1=10, n2=20))
