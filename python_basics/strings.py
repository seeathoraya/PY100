# Length

len("These aren't the droids you're looking for.")


# ALL CAPS

"confetti floating everywhere".upper()


# Ignoring Case

name = "Roger"
name2 = "RoGeR"
name3 = "DAVE"

print(name.casefold() == name2.casefold())
print(name.casefold() == name3.casefold())


# Multiline String

rhyme = """A pirate I was meant to be!
Trim the sails and roam the sea!"""

print(rhyme)


# Contains Character

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print("x" in char_sequence)


# Is Empty?

def is_empty(string):
    return len(string) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


# Is Empty or Blank?

def is_empty_or_blank(string):
    return (string.isspace() or string == "")

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


# Capitalize Words

def capitalize_words(string):
    words = string.split(" ")
    result = []

    for word in words:
         result.append(word.capitalize())
    
    print(" ".join(result))
    return " ".join(result)

string = "launch school tech & talk"

capitalize_words(string)


# Check Prefic

def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True


# Count Substrings

def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0