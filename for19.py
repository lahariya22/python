x = [4, 7, 12, 9, 13, 8, 3, 6, 21, 37]

odd_count = 0
# next %2 is used to check the number is odd or not .
# if it is odd then it give 1 and if it is even then it give 0.
# in if when next %2 == 0 it treated as false and when next %2 == 1 it treated as true.
for next in x:
    if next % 2:
        # odd_count = odd_count + 1
        odd_count += 1

print(odd_count)