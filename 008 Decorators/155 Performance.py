from ast import Pass
from time import time

# decorator


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result

    return wrap_func


@performance
def slow_function(counts):
    for i in range(counts):
        Pass
    print('Done')


slow_function(1000000)
