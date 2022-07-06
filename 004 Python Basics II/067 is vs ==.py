a = [1, 2, 3]
b = [1, 2, 3]

print(" ==: Testing the equality of value")
print(True == 1)  # True
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True
print(a == [1, 2, 3])
print(a == b)

print(" is: Testing the equality of reference. Finds if both are same object")
print(True is 1)  # False
print('' is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False
print(a is [1, 2, 3])
print(a is b)
