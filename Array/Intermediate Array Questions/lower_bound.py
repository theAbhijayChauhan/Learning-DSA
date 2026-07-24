def lower_bound(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

arr = [2, 4, 4, 4, 7, 9]
print(lower_bound(arr, 4))