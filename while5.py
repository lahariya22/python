n = int(input('Enter a number: '))

x = 0
#reverse the number 
while n:
    print('+++++++++')
    r = n % 10
    x = x * 10 + r
    n = n // 10

print(x)