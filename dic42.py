x = {'name':'om', 'age': 23}

y = {'phone': '6787676756', 'email': 'om@gmail.com'}

print(x, id(x))

print('#### All Keys #####')
for k in y.keys():
    print(k)

k = input('Enter one key from above list: ')
x.setdefault(k, y[k])

print(x, id(x))