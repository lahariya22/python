n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        # print(f'({i},{j})', end=' ')
        print(f'{i+j}/{n-1}', end=' ')
    print()