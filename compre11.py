n = int(input('Enter a number: '))
# add all the multiples of n from 1 to 10 in x list by using comprehension.

x = [n*i for i in range(1, 11)]

print(x)