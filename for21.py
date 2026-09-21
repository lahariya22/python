x = [4, 7, 12, 9, 13, 8, 3, 6, 21, 37]

even_count = 0
# not negotate the value of next % 2 if it is 0 
# then it treated as true and if it is 1 then it treated as false.
for next in x:
    if not next % 2:
        even_count += 1

print(even_count)