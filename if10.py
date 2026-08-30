price = int(input('Enter book price: '))

if price <= 200:
    print('Buy Now...')
elif price <= 400:
    print('Buy Later...')
else:
    print('Don\'t Buy')