from array import *

arr1 = array('i', [10, 20, 30, 40, 50, 20])
arr2 = array('i', [20, 40, 60, 80, 20])

common = array('i')

for i in range(len(arr1)):
    
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
                # To avoid duplicates in the array
                if arr1[i] not in common:
                    common.append(arr1[i])

print(common)