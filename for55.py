n = int(input('Enter a number: '))
# alphabet from Z to A using for loop and range function.
for each in range(n):
    r = 65+n-each-1
    print(chr(r))