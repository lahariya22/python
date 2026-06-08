x = {'name':'om', 'age': 23, 'college': 'global'}

print(x, id(x))

y = x.pop('global')

print(x, id(x))
print(y)

# KeyError: 'global'