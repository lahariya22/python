x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
z = int(input('Enter third value: '))

t = f'x: {x}' if x > y and x > z else f'y: {y}' if y > z else f'z: {z}'

print(t)