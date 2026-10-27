n = int(input('Enter a number: '))

for i in range(n):
    print('  '*i+'* '*(n-i))

# for i in range(n, 0, -1):
#     print('  '*(n-i)+'& '*i)