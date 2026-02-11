def linear_search(arr, trg):
    """
    Linear searching for iterables.
    
    Args:
        arr: Iterable to search (list, string, etc.)
        trg: Target element
        
    Returns:
        index of target if found
        -1 if target is not found
    """
    for i in range(len(arr)):
        if arr[i] == trg:
            return i
    return -1