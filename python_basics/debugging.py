# Reading Error Messages

def find_first_nonzero_among(numbers):
    for n in numbers:   # numbers is not iterable
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0]) # too many arguments, expected list
find_first_nonzero_among([1])


# Weather Forecast

import random

def predict_weather():
    sunshine = random.choice([True, False]) # True and false in quotes

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
    
predict_weather()


# Multiply By Five

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) # input is string value

print(f"The result is {multiply_by_five(number)}!")


# Pets

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser') # code reassigned the values for the "dog" key.

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}


# Confucius Says

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')


# Populate List

numbers = []

for i in range(1, 6): # if no start index is provided it will start at 0
    numbers.append(i)

print(numbers)


# Dictionary Access

info = {'name': 'Srdjan', 'age': 38}

print((info['city'] if 'city' in info else 'Unknown'))
print(info.get('city', 'Unknown'))


# Matrix

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy()) # same list referenced again and again

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


# Find Maximum

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2


# Digit Product

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1 # multiplying with 0 istead of 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0