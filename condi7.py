x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
z = int(input('Enter third value: '))

t = x if x > y and x > z else y if y > z else z

print(t)