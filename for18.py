x = [4, 7, 12, 9, 13, 8, 3, 6, 21]

odd_count = 0

for next in x:
    if next % 2 == 1:
        # odd_count = odd_count + 1
        odd_count += 1

print(odd_count)