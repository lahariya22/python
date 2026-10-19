n = int(input('Enter a number: '))

a = 65
b = 1

x = 0

for i in range(n):
    for j in range(n):
        if x % 2 == 0:
            print(chr(a), end=' ')
            a += 1
        else:
            print(b, end=' ')
            b += 1
        
        x += 1

    print()