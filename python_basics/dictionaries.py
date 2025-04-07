# First car

car = {
    "type": "sedan",
    "color": "blue",
    "mileage": 80_000,
}


# Adding the Year

car["year"] = 2003


# Broken Odometer

del car["mileage"]


# What Color?

print(car["color"])


# What's My Length?

print(len(car))


# Checking Key Existence

student = {
    'id': 123,
    'grade': 'B',
}

print("name" in student)
print("grade" in student)


# Multiple Cars

vehicles = {
    "car": {
        "type": "sedan",
        "color": "blue",
        "year": 2003,
    },
    "truck": {
        "type": "pickup",
        "color": "red",
        "year": 1998,
    }
}


# Which Collection?

car = [
    ["type", "sedan"],
    ["color", "blue"],
    ["year", 2003],
]


# Divided by Two

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []

for value in numbers.values():
    half_numbers.append(value // 2)

print(half_numbers)


# Labeled Numbers

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f"A {key} number is {value}.")