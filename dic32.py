x = {'name':'om', 'age': 23, 'college': 'global'}

print(x, id(x))

y = x.pop('college')

print(x, id(x))
print(y)