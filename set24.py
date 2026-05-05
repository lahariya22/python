x = {23, 45, 67, 78}
print(x, id(x))

y = x.copy()

print(y, id(y))
print(x, id(x))