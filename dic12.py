x = {'name': 'om', 'age': 19, 'college': 'SRIT'}

print(x, id(x))

# x['college'] = 'JEC'
x.setdefault('college', 'JEC')

print(x, id(x))