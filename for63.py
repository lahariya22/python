n = int(input('Enter a number: '))

for t in range(n):
    for s in range(n):
        print(f'({t}-{s})', end='\t')
    print()