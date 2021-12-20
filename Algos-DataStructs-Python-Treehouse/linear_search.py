def linear_search(list, target):
    """ 
    Returns the index value of the target if found, else returns None.
    """

    for i in range(0, len(list)):
        if target == list[i]:
            return i

    return None

def verify(index):
    """ 
    Checks if the index returned is not None, prints the index if found
    """

    if index is None:
        print("Target Not found in the list!")

    else: 
        print("Target found at the index" , index)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 6)
verify(result)
