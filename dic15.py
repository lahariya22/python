x = {'name':'om', 'age': 23, 'college': 'global'}

# ok
# print(x['name'])

# KeyError: 'degree'
# y = x['degree']
# or
y = x.get('degree')

print(y, '~~~~')