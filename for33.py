x = {'om': 56, 'raju': 89, 'ram': 71, 'raj': 92}

# o/p: name marks grade

result = None
di = x.items()

for n,m in di:    
    if m >= 75:
        result = 'Distinction'
    elif m >= 60:
        result = '1st Division'
    elif m >= 45:
        result = '2nd Division'
    elif m >= 33:
        result = '3rd Division'
    else:
        result = 'Fail'

    print(n, m, result, end='\n\n')