# 1. First line evaluates whether the values of the objects are the same.
#    The second line evaluates if the variables are pointing to the same object.

# 2. The initial value of set1 because set 1 is then mutated 
#    and no longer the same objext as set2 points to.

# 3. 'The Life of Brian' since dict2 was created using a dict constructor, 
#    creating a new dict object.

# 4. It would print 42, since both dict1 and dict2 contain a reference to the 
#    list object [1, 2, 3] (pointer to the same address)

# 5
print('### Exercise 5 ###')

import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# All of these should print True
print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])

# 6
print('\n### Exercise 6 ###')

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)           # False
print(dict1['a']    is dict2['a'])      # False
print(dict1['a'][0] is dict2['a'][0])   # True
print(dict1['a'][1] is dict2['a'][1])   # True
print(dict1['b']    is dict2['b'])      # False
print(dict1['b'][0] is dict2['b'][0])   # True
print(dict1['b'][1] is dict2['b'][1])   # True