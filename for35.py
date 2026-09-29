list = [4, 7, 12, 92, 13, 8, 3, 6, 21, 37]

max = list[0]
# max value in list 
for each in list:
    if each > max:
        max = each

print(f'Max: {max}')