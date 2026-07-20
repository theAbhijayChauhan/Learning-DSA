from array import *

arr = array("i", [1,2,3,4,6,7,8,9])

n = 5

for i in range(1, n+1):
    found = False
    
    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break
    if found == False:
        print(i)
        break