from array import *

arr = [45, 12, 8, 60, 30]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
        
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)



#  Decsending order
arr = [45, 12, 8, 60, 30]
# Traverse the array
for i in range(len(arr) - 1):
    # Assume current index has the largest element
    max_index = i
    # Find the actual largest element
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    # Swap the largest element with the current position
    temp = arr[i]
    arr[i] = arr[max_index]
    arr[max_index] = temp
print(arr)