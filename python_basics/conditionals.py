# Truthy vs. Falsy
"""
Falsy values in Python:
- False
- None
- [], (), {}
- 0, 0.0
- ''
- set()
- range(0)
"""


# Yes? No? Part 1

import random
random_number = random.randint(0, 1)

if random_number:
    print("Yes!")
else:
    print("No.")


# Yes? No? Part 2

print("Yes!" if random_number else "No.")


# Check the Weather, Part 1

weather = "cloudy"

if weather == "sunny":
    print("It's a beautiful day!")
elif weather == "rainy":
    print("Grab your umbrella.")
else:
    print("Let's stay inside")


# Match-Case
""" 
This would print 'neigh'.
"""


# Check the Weather, Part 2

weather = "snowy"

match weather:
    case "sunny":
        print("It's a beautiful day!")
    case "rainy":
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside")


# Logical Conditions 1
"""
The output would be "Yes!" because True is a truthy value.
"""


# Logical Conditions 2
"""
The output would be "No..." because the expression would always be No.
"""


# Logical Conditions 3
"""
The output would be "$3.99"
"""


# Are we moving?

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)