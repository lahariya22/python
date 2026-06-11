x = {'name':'om', 'age': 23}

y = {'phone': '6787676756', 'email': 'om@gmail.com'}

print(x, id(x))
print(y, id(y))

print('###################')
# x.extend(y)
x.update(y)
print('###################')

print(x, id(x))
print(y, id(y))