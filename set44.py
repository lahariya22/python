x = {12, 34, 56, 78, 90, 22, 9, 45, 68, 89, 92}
y = {19, 32, 56, 78, 91, 22, 10, 45, 67, 89, 95}

print(x, id(x))
print(y, id(y))

# union
z = x | y 

print('##############')

print(x, id(x))
print(y, id(y))
print('~~~~~~~~~~~~~~~~')
print(z, id(z))