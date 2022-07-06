picture = [

    [0, 0, 0, 1, 0, 0, 0],

    [1, 0, 0, 0, 0, 0, 1],

    [0, 1, 0, 0, 0, 1, 0],

    [0, 0, 1, 0, 1, 0, 0],

    [0, 0, 0, 1, 0, 0, 0],

    [0, 0, 1, 0, 1, 0, 0]

]

# replace/print 0 with empty space and 1 with *
final_picture = []
for i, row in enumerate(picture):
    inner_row = []
    for j, cell in enumerate(row):
        inner_row.insert(j, ' ' if cell == 0 else '*')
    final_picture.insert(i, inner_row)

# draw the list
for row in final_picture:
    for column in row:
        print(column, end="")
    print('\n')
