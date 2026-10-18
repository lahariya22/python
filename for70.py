n = int(input('Enter a number: '))

for j in range(n):
    for i in range(n):
        print(chr(65+i+j), end=' ')
    
    print()