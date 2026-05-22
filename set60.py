x = (34, 56, 67)

y = frozenset(x)

y.add(99)

# AttributeError: 'frozenset' object has no attribute 'add'