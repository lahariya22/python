n = int(input('Enter a number: '))

print(n, type(n))

s = str(n)

a = 0

ln = len(s)

k = 0

for i in s:
    a = a * 10 + int(i)

    if k + 1 == ln and a % 2 == 1:
        print(a)

        s = input('Enter a number: ')
        # s = str(n)
        a = 0
        ln = len(s)
        k = 0
        continue

    k += 1
    