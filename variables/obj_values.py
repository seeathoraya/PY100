obj = 42

obj = 'ABcd'        # reassign  √
obj.upper()         # neither   √
obj = obj.lower()   # mutate    x   reassign
print(len(obj))     # neither   √
obj = list(obj)     # reassign  √
obj.pop()           # mutate    √
obj[2] = 'X'        # mutate    √
obj.sort()          # mutate    √
set(obj)            # mutate    x   neither
obj = tuple(obj)    # mutate    x   reassign