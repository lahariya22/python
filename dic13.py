x = {'name': 'om', 'age': 19}

print(x, id(x))

# x['college'] = 'JEC'
x.setdefault('college', 'JEC')

print(x, id(x))