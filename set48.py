x = {11, 12, 13, 14}
y = {3, 5, 11, 6, 14}

print(x, id(x))
print(y, id(y))

# symmetric-difference
z = x ^ y 

print('##############')

print(x, id(x))
print(y, id(y))
print('~~~~~~~~~~~~~~~~')
print(z, id(z))