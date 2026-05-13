x = {34, 56, 78}

print(x, id(x))

# x.add(999)
# x.add(56)

# x.add([2, 3, 4])
# TypeError: unhashable type: 'list'

x.add((2, 3, 4))

print(x, id(x))