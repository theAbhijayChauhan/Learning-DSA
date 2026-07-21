from array import *

arr = array("i", [75, 21, 54, 2, 93, 67])

for i in range(len(arr)-1):
    swapped = False
    for j in range(len(arr)-i -1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        
        swapped = True
    
    if swapped == False:
        break
print(arr)