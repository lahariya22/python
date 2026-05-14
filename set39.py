x = {34, 56, 78}

print(x, id(x))

x.extend([2, 3, 4])

print(x, id(x))


# AttributeError: 'set' object has no attribute 'extend'