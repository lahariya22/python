x = {'name':'om', 'age': 23, 'college': 'global'}

print(x, id(x))
print('###################')
print(x.popitem())
print(x.popitem())
print(x.popitem())

# print(x.popitem())
# KeyError: 'popitem(): dictionary is empty'
print('###################')

print(x, id(x))