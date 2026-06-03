# x = dict('name':'ram', 'age': 23, 'branch': 'CS')
# SyntaxError: invalid syntax

# x = dict(23, 45, 67)
# TypeError: dict expected at most 1 argument, got 3

x = dict(34)
# TypeError: 'int' object is not iterable

print(x, type(x), len(x))