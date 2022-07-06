a = input('enter a number for looping: ')
itr = int(a)
i = 0

while i < itr:
    print(i)
    i += 1
    if i == 25:
        break
# break will be hit, only when the loop is done execution normally by failing the condition. If 'break', else will be skipped as well.
else:
    print('no break')
