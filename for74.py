n = int(input('Enter a number: '))

a = 65
b = 1
x = True

for i in range(n):
    for j in range(n):
        if x:
            print(chr(a), end=' ')
            a += 1
            b += 1
            x = False
        else:
            print(b, end=' ')
            a += 1
            b += 1
            x = True

    print()