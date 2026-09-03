g = input('Enter gender(m/f): ')
a = int(input('Enter Age: '))

if (g == 'm' or g == 'f') and a >= 1:
    if g == 'f':
        if a <= 22:
            print('MB: 0 and RI: 4%')
        elif a >= 60:
            print('MB: 0 and RI: 12%')
        else:
            print('MB: 2000 and RI: 8%')
    elif g == 'm':
        if a <= 22:
            print('MB: 500 and RI: 2%')
        elif a >= 60:
            print('MB: 2000 and RI: 11%')
        else:
            print('MB: 5000 and RI: 6%')
elif g != 'm' and g != 'f':
    print('Invalid age and gender' if a < 1 else 'Invalid Gender')
else:
    print('-------')
