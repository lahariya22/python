x = (34, 56, 67)

y = frozenset(x)

t = [2,3,4]
y.update(t)


# AttributeError: 'frozenset' object has no attribute 'update'