n = int(input('Enter a number: '))
# when n is odd, print n and ask for another number. Repeat until n is even.
while n % 2 == 1:
    print(n)
    n = int(input('Enter a number: '))