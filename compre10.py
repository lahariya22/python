n = int(input('Enter a number: '))

x = []
# add all the multiples of n from 1 to 10 in x list by using for loop.
for i in range(1, 11):
    x.append(n * i)

print(x)