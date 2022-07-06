# override the iterable functions to create a generator class

from distutils.command.build_scripts import first_line_re
from typing_extensions import Self


class my_range():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


for i in my_range(10, 20):
    print(i)
