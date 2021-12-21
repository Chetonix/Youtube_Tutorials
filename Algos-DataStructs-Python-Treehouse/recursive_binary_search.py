def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid_point = len(list)//2
        if target == list[mid_point]:
            return True
        else: 
            if target > list[mid_point]:
                return recursive_binary_search(list[mid_point+1:], target)
            else: 
                return recursive_binary_search(list[:mid_point], target)  

def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 6)
verify(result)