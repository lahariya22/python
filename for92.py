n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        if i == j or j == n - 1:
            print('@ ', end='')
        else:
            print(' ' if i > j else '  ', end='')
            
    print()