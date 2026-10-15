n = int(input('Enter a number: '))

for t in range(n):
    for s in range(n-1,-1,-1):
        print(chr(65+s), end=' ')
    print()