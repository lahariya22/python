x = {23, 45, 67, 78}
print(x, id(x), len(x))

del x

print(x, id(x), len(x))


# NameError: name 'x' is not defined