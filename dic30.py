x = {'name':'om', 'age': 23, 'college': 'global'}

print(x, id(x))

x.discard('college')

print(x, id(x))


# AttributeError: 'dict' object has no attribute 'discard'