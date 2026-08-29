x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))


if x > y and x > z:
    print(f'x: {x} is the greatest number...')
elif y > z:
    print(f'y: {y} is the greatest number...')
else:
    print(f'z: {z} is the greatest number...')
    