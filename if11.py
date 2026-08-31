marks = eval(input('Enter marks(%): '))

if marks > 100 or marks < 0:
    print('Invalid Input...')
elif marks >= 75:
    print('Distinction')
elif marks >= 60:
    print('First Division')
elif marks >= 45:
    print('Second Division')
elif marks >= 33:
    print('Third Division')
else:
    print('Fail...')