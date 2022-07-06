basket = [1, 2, 3, 4, 5, 6, 7]

print(basket.append(8))
basket.insert(8, 9)
new_basket = basket
print(basket)

print(basket.index(7))

# Sort Vs Sorted

basket.reverse()
print(basket)
print(sorted(basket))
print(basket.sort())
print(basket)
# print(sorted(basket))
