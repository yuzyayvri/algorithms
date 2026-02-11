def linear_search(arr, trg):
    for i in range(len(arr)):
        if arr[i] == trg:
            return i
    return -1

print(linear_search([1,5,4,7,5], 7))