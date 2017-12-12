for i in range(5):
    for j in range(4-i):
        print(' ', j, end='')
    for j in range(i+1):
        print('*', j, end='')
    print('')
