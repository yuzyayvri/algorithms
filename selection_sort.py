def selection_sort(arr):
    """
    Selection sorting to organize arrays in ascending order.
    Finds the minimum element and swaps it with the one at the current position.
    Repeats until it is finished with the entire array.
    
    Args:
        arr: Array to sort
        
    Returns:
        None (the given array is sorted directly)
    """
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]