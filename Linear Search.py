def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

l = [2,5,9,1,59,40,21]
key = 40
print(linear_search(l,key))