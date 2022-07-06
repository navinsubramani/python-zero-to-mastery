# generator is a subset of iterable
# for example: list is a iterable but not a generator, whereas range is a iterable and a generator


def gen_range(n):
    for i in range(n):
        yield i


for i in gen_range(100):
    print(i)
