x = ['mohan','dinesh','ravi','binson']
# add all elements of x list in y list by using comprehension with 1st letter in capital letter.
y = [each.title() for each in x] 
#or
y = [each.capitalize() for each in x]
print(y)