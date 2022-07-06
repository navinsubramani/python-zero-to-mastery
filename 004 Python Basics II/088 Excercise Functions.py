# Find the highest even number

def highest_even(li):
    even_li = []
    for num in li:
        if num % 2 == 0:
            even_li.insert(0, num)
    return max(even_li)


print(highest_even([1, 3, 5]))
