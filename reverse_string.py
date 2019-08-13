# Python code to reverse a string
# using a recursion

# Explanation : In the above code, string is passed as an argument to a recursive function to reverse the string. In
# the function, the base condition is that if the length of the string is equal to 0, the string is returned. If not
# equal to 0, the reverse function is recursively called to slice the part of the string except the first character
# and concatenate the first character to the end of the sliced string.


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "pythontutorial"

print("The original string is: ", end="")
print(s)

print("The reversed string (using loop) is: ", end="")
print(reverse(s))

if __name__ == "__main__":
    reverse(s)
