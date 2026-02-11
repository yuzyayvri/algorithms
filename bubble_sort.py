def bubble_sort(arr):
    """
    Bubble sorting to organize number arrays in ascending order by swapping two adjacent elements.
    Extremely inefficient... but if you're still firm on using this, good luck.
    
    Args:
        arr: Number array to sort
        
    Returns:
        None (the given array is sorted directly)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]