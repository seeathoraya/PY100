# Multiply

def multiply(num_1, num_2):
    return num_1 * num_2

multiply(12, 4)


# Print Quote

def bruce_eckel_quote():
    print("Python is executable pseudocode.")

bruce_eckel_quote() # Returns None


# Cite the Author

def cite(author, quote):
    print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')


# Squared Number

def squared_number(num):
    return num * num    # can also be num**2

squared_number(3)


# Display Division
"""
It wont print anything as the function is never invoked,
since it lacks the () next to the function name.
"""


# Three-way Comparison

def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0


# Transformation

print("Captain Ruby".replace("Ruby", "Python"))


# Internationalization 1

def greet(lang):
    match lang:
        case "en":
            return "Hi!"
        case "fr":
            return "Salut!"
        case "pt":
            return "Olá!"
        case "de":
            return "Hallo!"
        case "sv":
            return "Hej!"
        case "af":
            return "Haai!"

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!


# Locale Part 1

def extract_language(locale):
    return locale[:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko


# Locale Part 2

def extract_region(locale):
    return locale[3:5]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR


# Internationalization 2

print("# Internationalization 2")

def local_greet(locale):
    region = extract_region(locale)
    lang = extract_language(locale)

    if lang == "en":
        match region:
            case "US":
                return "Hey!"
            case "GB":
                return "Hello!"
            case "AU":
                return "Howdy!"
    else:
        return greet(lang)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!