def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]    
    return i + 1
    
    

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr)-1)
print(arr)





# In Simple Code:
print()

low = 0
high = len(arr) - 1

pivot = arr[high]
i = low - 1

print("Original Array:", arr)
print("Pivot:", pivot)

for j in range(low, high):
    if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

# Put pivot in its correct position
arr[i + 1], arr[high] = arr[high], arr[i + 1]

print("\nAfter Partition:")
print(arr)
print("Pivot Index:", i + 1)