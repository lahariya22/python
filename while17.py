x = [23, 57, 42, 13, 9, 28, 27, 19, 12, 93]

ln = len(x);
i = 0;
odd_count = 0;

while i < ln:
    if x[i] % 2 == 0:
        print(x[i]);
    else:
        odd_count += 1;
    i += 1

print('odd count: ', odd_count); 