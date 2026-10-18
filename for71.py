n = int(input('Enter a number: '))

a = n * n -1

for j in range(n):
    for i in range(n):
        print(chr(65+a), end=' ')
        a -= 1

    print()