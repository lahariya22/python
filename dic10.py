x = {'name':'om', 'age': 23, 'college': 'global', None: 'BTech'}

print(x, id(x))

x[None] = 'MTech'

print(x, id(x))