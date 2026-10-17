n = int(input('Enter a number: '))

a = 0

for j in range(n):
    for i in range(n):
        print(chr(97+a), end=' ')
        a += 1

    print()