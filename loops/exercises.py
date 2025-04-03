# 1. Because the counter stays at 0 so the expression remains true forever.

# 2
print('### Exercise 2 ###')

age = 39 # redacted for future testing: int(input('How old are you? '))
print(f'\nYou are {age} years old.')
for years in range(10, 41, 10):
    print(f'In {years} years, you will be {age + years} years old.')

# 3
print('\n### Exercise 3 ###')

my_list = [6, 3, 0, 11, 20, 4, 17]

print('while loop:')
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print('\nfor loop:')
for num in my_list:
    print(num)

# 4
print('\n### Exercise 4 ###')

my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0
print('Even numbers:')
while i < len(my_list):
    num = my_list[i]
    if num % 2 == 0:
        print(num)
    i += 1

print('Odd numbers:')
for num in my_list:
    if num % 2 != 0:
        print(num)

# 5
print('\n### Exercise 5 ###')

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for num in list:
        if num % 2 == 0:
            print(num)

# 6
print('\n### Exercise 6 ###')

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
new_list = []
for num in my_list:
    if num % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    new_list.append(result)
print(new_list)

# 7
print('\n### Exercise 7 ###')

def find_integers(tuple):
    return [obj 
            for obj in tuple 
            if (type(obj) is int)]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)

# 8
print('\n### Exercise 8 ###')

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {item: len(item) 
           for item in my_set
           if len(item) % 2 != 0}
print(my_dict)

# 9
print('\n### Exercise 9 ###')

def factorial(num):
    result = 1
    for n in range(1, (num + 1)):
        result *= n
    return(result)

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

# 10
print('\n### Exercise 10 ###')

import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# 11
print('\n### Exercise 11 ###')

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < (len(my_list)):
    nested_list = my_list[index]
    nested_index = 0

    while nested_index < (len(nested_list)):
        if nested_list[nested_index] % 2 == 0:
            print(nested_list[nested_index])
        nested_index += 1
    
    index += 1