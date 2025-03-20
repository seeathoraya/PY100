# using single expression
balance = 1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(f'Balance after 5 years: ${balance}')

# using augmented assignment
balance = 1000.00
for i in range (0, 5):
    balance *= 1.05
print(f'Balance after 5 years: ${balance}')