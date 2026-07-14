marks = float(input('Enter marks: '))

t = 'fail' if marks < 33 else '3rd Division' if marks < 45 else '2nd Division'if marks<60 else '1st Division' if marks < 75 else 'Distinction'

print(t)