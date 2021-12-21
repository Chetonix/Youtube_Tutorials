def binary_search(list, target):
    """ 
    Returns the index value of the target if found, else returns None via a binary search algo.
    """
    # target_found = False
    # list_copy = list[:]
    first = 0
    last = len(list) - 1 
    
    while(first <= last):
        mid_point = (first + last) // 2
        if target == list[mid_point]:
            # target_found = True
            return mid_point
        else:
            if target > list[mid_point]:
                first = mid_point + 1

            else:
                end = mid_point - 1  
    
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
result = binary_search(numbers, 9)
verify(result)