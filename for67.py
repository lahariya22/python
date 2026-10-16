n = int(input('Enter a number: '))

for t in range(64+n, 64, -1):
    for s in range(n):
        print(chr(t), end=' ')
    print()