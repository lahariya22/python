price = int(input('Enter Book Price: '))

t = 'Buy Now' if price <= 200 else 'Buy Later' if price <= 400 else 'Don\'t Buy'

print(t)