n = int(input('Enter a number: '))

for i in range(n):
    print(f'{'  '*(n-i-1)}{'@ '*(i+1)}')