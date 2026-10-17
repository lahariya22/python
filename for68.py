n = int(input('Enter a number: '))

a = 65

for j in range(n):
    for i in range(n):
        print(chr(a), end=' ')
        a += 1

    print()