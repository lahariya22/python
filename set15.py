x = {34, 56, 12}

print(x, id(x))

x.append(99)

print(x, id(x))

# AttributeError: 'set' object has no attribute 'append'