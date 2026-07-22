from array import *

arr = array("i", [45, 12, 8, 60, 30])

# Start from the second element
for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    
    # Shift larger elements one position to the right
    while j >= 0 and arr[j] > current:
        arr[j+1] = arr[j]
        j -= 1
        
    # Insert the current element at its correct position
    arr[j+1] = current
        
print(arr)


# In Decending Form

# Start from the second element
for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    
    # Shift smaller elements one position to the right
    while j >= 0 and arr[j] < current:
        arr[j + 1] = arr[j]
        j -= 1
    
    # Insert the current element at its correct position
    arr[j + 1] = current

print(arr)