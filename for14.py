x = [4, 7, 12, 9, 13, 8, 3, 6, 21]

sum = 0
# print only odd number sum in the list
for next in x:
    if next % 2 == 1:
        sum = sum + next

print(sum)