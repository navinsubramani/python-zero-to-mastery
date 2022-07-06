import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)


my_file = open('sample.txt')
print(my_file)
print(my_file.read())
print(my_file.read())

my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()
