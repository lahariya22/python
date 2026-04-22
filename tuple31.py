y = [12, 34, 56]
z = (12, 34, 56)

# x = tuple()
# x = tuple(y)
# x = tuple(z)
#  ~~~~~~~~~~~~~~~~~~~~~~
# x = tuple(12, 34, 56)  # not ok
x = tuple(12) # TypeError: 'int' object is not iterable

print(x, type(x), len(x))