x = {'om': 56, 'raju': 89, 'ram': 71, 'raj': 92}

# o/p: name marks grade

for next in x:
    m = x[next]
# in m we store the value of the key and then we will check the value of m and then we will print the name marks grade.
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

    print(next, m, result, end='\n\n')