i = 1
j = 1

for j in range(1, 6):
    for i in range(1, j+1):
        print('*', end='')
        i += 1
    print('')
    j += 1

