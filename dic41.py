x = {'name':'om', 'age': 23}

y = {'phone': '6787676756', 'email': 'om@gmail.com'}

print(x, id(x))

x.setdefault('phone', y['phone'])

print(x, id(x))