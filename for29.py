x = [41, 7, 121, 9, 13, 81, 3, 61, 21, 37]
# x = [41, 7, 12, 9, 13, 8, 3, 6, 21, 37]

flag = False

for each in x:
    print('--------------------')
    if each % 2 == 0:
        flag = True 
        break

if flag:
    print('The list contains even record')
else:        
    print('The list does not contain even record')