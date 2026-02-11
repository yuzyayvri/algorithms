def binary_search(arr, trg):
    """
    Binary searching for sorted iterables. Array should be ascending order.
    
    Args:
        arr: Sorted iterable to search (list, string, etc.)
        trg: Target element
        
    Returns:
        index of target if found
        -1 if target is not found
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == trg:
            return mid
        elif arr[mid] < trg:
            low = mid + 1
        else:
            high = mid - 1
    return - 1
    