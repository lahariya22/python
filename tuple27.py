x = 11
y = 23

print(f'x: {x} - y: {y}')

x = x ^ y
y = x ^ y
x = x ^ y

print(f'x: {x} - y: {y}')