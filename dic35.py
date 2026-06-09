x = {'name':'om', 'age': 23, 'college': 'global'}

print(x, id(x))

x.popitem()
x.popitem()
x.popitem()

print(x, id(x))