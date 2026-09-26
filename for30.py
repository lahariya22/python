x = [41, 7, 121, 9, 13, 81, 3, 61, 21, 37]
#x = [41, 7, 12, 9, 13, 8, 3, 6, 21, 37]

for each in x:
    print('--------------------')
    if each % 2 == 0:
        print('The list contains even record')
        break
# this else is associated with for loop and
# it will execute when for loop is not breaked and 
# it will not execute when for loop is breaked.
else:        
    print('The list does not contain even record')
    # this is not associated with if statement and it will execute when for loop.