# Exercise 1
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)

# Exercise 2
num = '4936'

## my solution
one_place = num[-1]
ten_place = num[-2]
hundred_place = num[-3]
thousands_place = num[-4]

print('One place is ' + one_place)
print('Tens place is ' + ten_place)
print('Hundred place is ' + hundred_place)
print('Thousands place is ' + thousands_place)

## alternative solution
num = 4936
ones = num % 10
num = num // 10
tens = num % 10
num = num // 10
hundreds = num % 10
num = num // 10
thousands = num % 10

print('One place is', ones)
print('Tens place is', tens)
print('Hundred place is', hundreds)
print('Thousands place is', thousands)

# Exercise 3
print(int('5') + int('10'))