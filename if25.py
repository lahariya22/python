marks = eval(input('Enter marks(%): '))

if marks > 100 or marks < 0:
    print('Invalid Input:', marks)
    print('Min Marks is 0' if marks < 0 else 'Max Marks: 100')
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