n = int(input('Enter a number: '))

for t in range(n-1,-1,-1):
    for s in range(n-1,-1,-1):
        print(f'({t}-{s})', end='\t')
    print()