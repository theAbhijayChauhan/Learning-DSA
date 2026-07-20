##  Find Elements Present in the First Array but Not in the Second

from array import *

arr1 = array('i', [10, 20, 30, 40, 50])
arr2 = array('i', [20, 40])

result = array('i')

for i in range(len(arr1)):
    found = False
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            # result.append(arr1[i])
            found = True
            break
    
    if found == False:
        result.append(arr1[i])

print(result)

