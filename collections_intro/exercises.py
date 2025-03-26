# 1 len(people)

# 2
stuff = ('hello', 'world', 'bye', 'now')
print(stuff)
stuff = list(stuff)

index = 0
for word in stuff:
    if word == 'bye':
        stuff[index] = 'goodbye'
    else:
        index += 1

stuff = tuple(stuff)
print(stuff)


"""
# 3. Lists vs Tuples

Differences:
1. mutable vs immutable
2. [] vs ()

Similarities:
1. ordered sequence of objects
2. can hold any data type

# 4. Strings are a sequence of characters

# 5. Sets hold unique values only and are not ordered

"""

# 6
pi = 3.141592
str_pi = str(pi)

""" 
# 7
range(7)        # 0-6
range(1, 6)     # 1-5
range(3, 15, 4) # 3, 7, 11
range(3, 8, -1) # 
range(8, 3, -1) # 8-4
 """

# 8
print(list(range(3, 17, 4)))

""" 
# 9

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

1. Are the lists assigned to my_list and another_list equal? YES
2. Are the lists assigned to my_list and another_list the same object? NO
3. Are the nested lists at index 3 of my_list and another_list equal? YES
4. Are the nested lists at index 3 of my_list and another_list the same object? YES

# 10. No, because names is a set and sets are unordered.
 """

# 11
print('### EXERCISE 11 ###')

people = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshikata': 'Japan',
}

print(f'{people['Francois']}')