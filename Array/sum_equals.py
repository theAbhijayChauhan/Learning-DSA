# Find Two Numbers Whose Sum Equals a Target

from array import *

arr = array('i', [10, 20, 30, 40, 50])

target = 70

for i in range(len(arr)):
    
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j],"=", target)
            break
