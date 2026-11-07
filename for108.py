x = [2, 8, 6, 4, 9, 2, 5, 1, 2, 3, 7, 8, 2, 4, 1, 5, 4, 11, 2]

print(x)


y = dict()

for i in x: 
    if i in y:
        y[i] = y[i] + 1
    else:
        y[i] = 1

for k,v in y.items():
    print(k, '.', v)