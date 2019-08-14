from string import digits


# initializing the string
string_one = "Geeks123for127geeks"

# print the initial string
print("The initial string: ", string_one)

# using translate and digits
# to remove numeric digits from string
remove_digits = str.maketrans('', '', digits)
string_two = string_one.translate(remove_digits)

# print the altered string
print("The initial string: ", string_two)
