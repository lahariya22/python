n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        if i+j == n-1 or j == n-1:
            print('@ ', end='')
        else:    
            print(' ', end='') if i+j < n-1 else print('  ', end='')
            
    print()