x = [4, 7, 12, 9, 13, 8, 3, 6, 21, 37]

even_count = 0

for next in x:
    if next % 2 == 0:
        even_count += 1

print(even_count)