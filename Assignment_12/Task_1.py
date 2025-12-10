def linear_search(lst, target):
    """
    Perform linear search on a list to find the index of the target value.
    
    Parameters:
        lst (list): The list to search.
        target: The value to search for.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Example usage:
numbers = [4, 2, 7, 1, 9, 3]
value_to_find = 7

result = linear_search(numbers, value_to_find)
print("Index:", result) 
