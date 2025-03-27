# 1
print('### Exercise 1 ###')
my_range = range(0, 25, 3)
print(my_range[6])

# 2
print('\n### Exercise 2 ###')
school = 'Launch School'
index = school.find('c')
print(school[index:index + 6])

# 3
print('\n### Exercise 3 ###')
init_tuple = (1, 2, 3, 4, 5)
my_list = list(init_tuple[1:4])
my_list.reverse()
new_tuple = tuple(my_list)
print(new_tuple)

# 4
print('\n### Exercise 4 ###')
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))


# 5
# 'cat'                           # OK
# (3, 1, 4, 1, 5, 9, 2)           # OK
# ['a', 'b']                      # List - mutable
# {'a': 1, 'b': 2}                # Dictionary - mutable
# range(5)                        # OK
# {1, 4, 9, 16, 25}               # Set - mutable
# 3                               # OK
# 0.0                             # OK
# frozenset({1, 4, 9, 16, 25})    # OK 


# 6
print('abc-def'.isalpha())      # falsy
print('abc_def'.isalpha())      # falsy
print('abc def'.isalpha())      # falsy
print('abc def'.isalpha() and
      'abc def'.isspace())      # falsy
print('abc def'.isalpha() or
      'abc def'.isspace())      # falsy
print('abcdef'.isalpha())       # truthy
print('31415'.isdigit())        # truthy
print('-31415'.isdigit())       # falsy
print('31_415'.isdigit())       # falsy
print('3.1415'.isdigit())       # truthy -- false
print(''.isspace())             # falsy


# 7
print('\n### Exercise 7 ###')

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
split_join = '+'.join(info.split(':'))
print(split_join)

replace = info.replace(':', '+')
print(replace)

# 8. Because the first line creates a slice where the first character has an
#    index of 0, while the second line merely limits the find method to the
#    provided start and end limits

# 9
print('\n### Exercise 9 ###')

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 'Six'
print(stuff)

# 10
print('\n### Exercise 10 ###')

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# 11
print('\n### Exercise 11 ###')

print('johnson' in 'Joe Johnson')       # False
print('sen' not in 'Joe Johnson')       # True
print('Joe J' in 'Joe Johnson')         # True
print(5 in range(5))                    # False
print(5 in range(6))                    # True
print(5 not in range(5, 10))            # False
print(0 in range(10, 0, -1))            # False
print(4 in {6, 5, 4, 3, 2, 1})          # True
print({1, 2, 3} in {1, 2, 3})           # True  -- False
print({3, 2} in {1, frozenset({2, 3})}) # False -- True

# 12
print('\n### Exercise 12 ###')

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

# 13
print('\n### Exercise 13 ###')
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')

print('Butterscotch' in cats)   # True
print('Butter' in cats)         # False
print('Butter' in cats[3])      # True
print('cheddar' in cats)        # False

# 14
print('\n### Exercise 14 ###')

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

result = list(zip(my_str, my_list, my_tuple, my_range))
print(result)

# 15. Would not print ['Cat', 'Dog', 'Bird'] -- keys' value is a dictionary
#     view object that returns the keys from the pets dictionary.