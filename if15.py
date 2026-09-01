g = input('Enter gender(m/f): ')
a = int(input('Enter Age: '))

if a <= 22:
    if g == 'f':
        print('MB: 0 and RI: 4%')
    elif g == 'm':
        print('MB: 500 and RI: 2%')
    else:
        print('Invalid Gender...')
elif a >= 60:
    if g == 'f':
        print('MB: 0 and RI: 12%')
    elif g == 'm':
        print('MB: 2000 and RI: 11%')
    else:
        print('Invalid Gender...')    
else:
    if g == 'f':
        print('MB: 2000 and RI: 8%')
    elif g == 'm':
        print('MB: 5000 and RI: 6%')
    else:
        print('Invalid Gender...')    
    