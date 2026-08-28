x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if x == y:
    print(f'x: {x} and y: {y} both are same')
elif x > y:
    print(f'x: {x} is greater than y: {y}')
else:
    print(f'y: {y} is greater than x: {x}')