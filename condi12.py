g = input('Enter gender(m/f): ')
a = int(input('Enter Age: '))

r = ('MB: 0 and RI: 4%' if a <= 22 else 'MB: 0 and RI: 12%' if a > 60 else 'MB: 2000 and RI: 8%')if g == 'f'  else ('MB: 500 and RI: 2%' if a <= 22 else 'MB: 2000 and RI: 11%' if a > 60 else 'MB: 5000 and RI: 6%')

print(r)