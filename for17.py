x = [4, 7, 12, 9, 13, 8, 3, 6, 21]

sum = 0
# in this we check the number is even or not if it is even then we add that number in sum variable
#and at the end we print the sum of all even number in the list.
for next in x:
    if next % 2 == 0:
        sum = sum + next

print(sum)