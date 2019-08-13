from collections import OrderedDict


def remove_duplicates_no_order(string):
    return "".join(set(string))


# Function to remove all duplicates from string
# and keep the order of characters same
def remove_duplicates_order(string):
    return "".join(OrderedDict.fromkeys(string))


# Driver program
if __name__ == "__main__":
    string = "geeksforgeeks"
    print("Without Order = ", remove_duplicates_no_order(string))
    print("With Order = ", remove_duplicates_order(string))
