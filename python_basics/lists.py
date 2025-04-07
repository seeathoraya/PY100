# First Element

def first(list):
    if len(list) > 0:
        return list[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))  # Earth


# Last Element

def last(list):
    if list:
        return list[-1]
    else:
        return None
    
print(last(['Earth', 'Moon', 'Mars']))  # Mars


# Add + Delete

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove('fossil')
energy.append('geothermal')
print(energy)


# Alphabet

alphabet = 'abcdefghijklmnopqrstuvwxyz'
characters = []

for char in alphabet:
    characters.append(char)

print(characters)


# Filter

scores = [96, 47, 113, 89, 100, 102]
count = 0

for score in scores:
    if score >= 100:
        count += 1

print(count)


# Vocabulary

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for meaning in vocabulary:
    for word in meaning:
        print(word)


# Equality

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)   # Should be true because the == operator compares the values and they are equal.


# Type

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(isinstance(some_value1, list))
print(isinstance(some_value2, list))


# Travel

def contains(str, seq):
    for item in seq:
        return item == str

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False


# Passcode

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

output = "-".join(passcode)
print(output) # Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs


# Checking items off the grocery list

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list.pop(0))

print(grocery_list)