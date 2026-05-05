x = {34, 78, 45, 56}

print(x, id(x))

# x.remove(78)  # ok
# x.pop() # ok
x.discard(78)   # ok
# ------- ---------
# x.pop(78)  # not ok
# del  # not ok

print(x, id(x))
