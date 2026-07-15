marks = eval(input('Enter your marks(%): '))

x = 'Invalid Input' if marks < 0 or marks > 100 else \
    'Distinction' if marks >= 75 else \
    '1st Division' if marks >= 60 else \
    '2nd Division' if marks >= 45 else \
    '3rd Division' if marks >= 33 else 'Fail'

print(x)