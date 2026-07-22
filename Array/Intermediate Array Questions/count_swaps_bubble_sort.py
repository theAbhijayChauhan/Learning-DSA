from array import *

arr = array("i", [32, 65, 94, 87, 13, 6, 48, 55])

swaps = 0
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1

print("Sorted Array:", arr)
print("Total Swaps:", swaps)