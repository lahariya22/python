x = {'name':'om', 'age': 23}

y = {'phone': '6787676756', 'email': 'om@gmail.com'}

print(x, id(x))
print(y, id(y))

z = x + y
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

print(z, id(z))