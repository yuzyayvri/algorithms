def merge_sort(arr):
    """
    Recursive function for sorting the list using merge sort (divide and conquer) algorithm.
    Splits the list down the mid (which is rounded down, not nearest).
    Does this until each sublist contains only one element, then merges them in sorted order.
    Ends up with two sorted lists that are then given as args to merge(l, r)
    Original list is not modified. You have to get the sorted list by the return.
    
    Args:
        arr: The list to sort. (Floats, strings, integers, etc)
    
    Returns:
        list: The new sorted list with all the elements from the original list in ascending order.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l_half = merge_sort(arr[:mid])
    r_half = merge_sort(arr[mid:])
    return merge(l_half, r_half)

def merge(l, r):
    """
    Merging for the two sorted lists made by merge_sort(arr).
    Repeatedly compares the elements of each list starting from their 0 index.
    After that, it adds the smaller one to the result.
    Repeats until everything is merged into one complete sorted list.
    
    Args:
        l: The first sorted list, aka the left half.
        r: The second sorted list, aka the right half.
    
    Returns:
        The new sorted list with all the elements from both the sorted lists in order.
        If not sorted in ascending order, or not sorted with merge_sort(arr), may not function properly.
    """
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result