some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n']

# print the duplicates
lookup = []
duplicate = []

for item in some_list:
    is_item = False
    for i in lookup:
        if i == item:
            is_item = True
            break
    if not is_item:
        lookup.insert(0, item)
    else:
        # This occurs if the item is duplicate. Check if the item is already detected as duplicate, then check for it and skip it
        is_doubleduplicate = False
        for i in duplicate:
            if i == item:
                is_doubleduplicate = True
                break
        if not is_doubleduplicate:
            duplicate.insert(0, item)

print(duplicate)

# Simple solution
duplicate = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate:
            duplicate.insert(0, item)
print(duplicate)
