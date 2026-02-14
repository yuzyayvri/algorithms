def insertion_sort(arr):
    """
    In-place comparison-based sorting algorithm, also called 'slide and drop' algorithm.
    Slides larger elements to the right to make a hole for the current 'key'.
    Once j is not larger than the key, it's found the correct spot.
    And again, the original list is the one modified.
    
    Args:
        arr: The list to sort.
        
    Returns:
        None (The given list is sorted directly)
    """
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key