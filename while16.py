# x = [23, 57, 41, 13, 9, 45, 27, 19, 71, 93]
x = [23, 57, 42, 13, 9, 45, 27, 19, 71, 93]

ln = len(x)
i = 0

while i < ln:
    if x[i] % 2 == 0:
        print('Even Record Found...')
        break
    i += 1

else:
    print('Even Record Not Found...')