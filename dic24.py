x = {'name': 'raj', 'age': 34}
print(x, type(x), id(x))

y = dict(x)
print("~~~~~~~~~~~~~~~~~")

print(x, type(x), id(x))
print(y, type(y), id(y))