# set can shrink
# set is mutable

x = {34, 56, 12}

print(x, id(x))

x.remove(56)

print(x, id(x))