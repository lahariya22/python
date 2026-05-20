x = {11, 12, 13, 14}
y = {3, 5, 11, 6, 14}

print(x, id(x))
print(y, id(y))

# intersection
# z = x & y 
z = x.intersection(y)

print('##############')

print(x, id(x))
print(y, id(y))
print('~~~~~~~~~~~~~~~~')
print(z, id(z))