g = input('Enter gender(m/f): ')
a = int(input('Enter Age: '))

if g != 'm' and g != 'f':
    print('Invalid Gender...', g)
elif a < 1:
    print('Invalid Age... ', a)
else:
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