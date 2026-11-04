n = int(input('Enter a number: '))

print(n, type(n))

x = str(n)

print(x, type(x))

y = list(x)

print(y, type(y))

y.reverse()

print(y, type(y))

a = ''.join(y)

print(a, type(a))

b = int(a)

print(b, type(b))