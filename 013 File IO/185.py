from pathlib import Path
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '\sample.txt'

with open(FILE_PATH, mode='r') as my_file:
    print(my_file)
    print("READ FROM THE FILE")
    print(my_file.read())
    print(my_file.read())

    my_file.seek(0)
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())

with open(FILE_PATH, mode='a') as my_file:
    print("WRITE TO THE FILE")
    my_file.write('hi.. I wrote this!!!')

with open(FILE_PATH, mode='r') as my_file:
    print("READ FROM THE FILE")
    print(my_file.read())
