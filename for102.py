n = int(input('Enter a number: '))

print(n, type(n))
# -----------------------

a = list(str(n))

a.reverse()

b = int(''.join(a))

# ----------------
print(b, type(b))