x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))


if x == y and y == z:
    print(f'x: {x}, y: {y} and z: {z} are all same')
elif x == y:
    print(f'x: {x} and y: {y} are same and greater than z: {z}' if x > z else f'z: {z} is the greatest number...')
elif x == z:
    print(f'x: {x} and z: {z} are same and greater than y: {y}' if x > y else f'y: {y} is the greatest number...')
elif y == z:
    print(f'y: {y} and z: {z} are same and greater than x: {x}' if y > x else f'x: {x} is the greatest number...')
elif x > y and x > z:
    print(f'x: {x} is the greatest number...')
elif y > z:
    print(f'y: {y} is the greatest number...')
else:
    print(f'z: {z} is the greatest number...')
    