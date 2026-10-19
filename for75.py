n = int(input('Enter a number: '))

a = 65
b = 2
x = True

for i in range(n):
    for j in range(n):
        if x:
            print(chr(a), end=' ')
            a += 2
            x = False
        else:
            print(b, end=' ')
            b += 2
            x = True

    print()