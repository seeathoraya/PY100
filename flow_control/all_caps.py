def all_caps(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
all_caps(str(input('Enter some text: ')))