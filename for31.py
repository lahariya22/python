x = [4, 7, 12, 9, 13, 8, 3, 6, 21, 37]

odd_count = 0

for each in x:
    if each % 2 == 0:
        print(each)
        continue
    # in this when you  find the even number then it will print that number
    #  and then it will skip the rest of the code and it will go to next iteration of loop
    #  and when you find the odd number then it will execute the rest of the code and
    #  it will add 1 in odd_count variable.
    odd_count += 1

print('-----------------')
print(f'odd count: {odd_count}')


# S.py