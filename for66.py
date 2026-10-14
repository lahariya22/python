n = int(input('Enter a number: '))

for t in range(n):
    for s in range(64+n, 64, -1):
        print(chr(s), end='-')
    print()